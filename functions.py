import time
from tkinter import *
from tkinter import messagebox, filedialog
import os
import threading
import vlc
import customtkinter
import PIL.Image
import yt_dlp
import sqlite3
import uuid


def create_database():
    connection = sqlite3.connect("data/setting.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_settings (
            user_id TEXT NOT NULL,
            setting_key TEXT NOT NULL,
            setting_value TEXT NOT NULL,
            PRIMARY KEY (user_id, setting_key)
        )
    ''')
    connection.commit()
    connection.close()


def get_user_id():
    name = "userID.txt"
    if os.path.exists(name):
        with open(name, "r") as file:
            id = file.read().strip()
            if id:
                return id
    else:
        with open(name, "w") as file:
            id = str(uuid.uuid4())
            file.write(id)
            return id


def is_table_empty(table_name):
    connection = sqlite3.connect("data/setting.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    count = cursor.fetchone()[0]
    connection.close()
    return count == 0


def default_setting(id, setting_dict):
    if is_table_empty('user_settings'):
        connection = sqlite3.connect("data/setting.db")
        cursor = connection.cursor()
        cursor.executemany('''
            INSERT INTO user_settings (user_id, setting_key, setting_value)
            VALUES (?, ?, ?)
        ''', [(id, key, value) for key, value in setting_dict.items()])
        connection.commit()
        connection.close()


def update_setting(id, setting_dict):
    connection = sqlite3.connect("data/setting.db")
    cursor = connection.cursor()
    for key, value in setting_dict.items():
        cursor.execute('''
            UPDATE user_settings
            SET setting_value = ?
            WHERE user_id = ? AND setting_key = ?
        ''', (value, id, key))
    connection.commit()
    connection.close()


def get_setting(id, setting_key):
    connection = sqlite3.connect("data/setting.db")
    cursor = connection.cursor()
    cursor.execute('''
        SELECT setting_value FROM user_settings
        WHERE user_id = ? AND setting_key = ?
    ''', (id, setting_key))
    value = cursor.fetchone()
    connection.close()
    return value[0] if value else None


download_icon_con = False
download_icon = customtkinter.CTkImage(
    PIL.Image.open("Icons/download_icon.png"), size=(20, 20)
)
download_icon_light = customtkinter.CTkImage(
    PIL.Image.open("Icons/download_icon_light.png"), size=(20, 20)
)
total_mb = 0


class text_animation:
    def __init__(self, label):

        self.label = label
        self.bool = True
        self.value = "Download\nYoutube video\nfor free..."

        self.animation = threading.Thread(target=self.skeleton, daemon=True)
        self.animation.start()

    def skeleton1(self):

        i = 0
        while True:

            self.label.configure(text=f"{i}")
            time.sleep(0.2)

            i += 1
            if i == 10:
                self.label.configure(text="")
                i = 0
            if self.bool == False:
                break
        raise SystemExit()

    def skeleton(self):

        i = 0
        while True:

            self.label.configure(text=self.value[: i + 1])
            time.sleep(0.2)

            i += 1
            if i == len(self.value):
                self.label.configure(text="")
                i = 0
            if self.bool == False:
                break

    def stop(self):

        if self.bool:
            self.bool = False
            self.label.configure(text=self.value)

    def start(self):
        if not self.bool:
            self.bool = True
            self.animation = threading.Thread(target=self.skeleton)
            self.animation.daemon = True
            self.animation.start()


def type(b):
    b.entry.delete(0, END)


class Download_UI:
    def __init__(self, parent, video_url, pv_frame):
        self.id = get_user_id()
        pv_frame.player.stop()
        pv_frame.root.destroy()

        self.parent = parent
        self.video_url = video_url

        self.cancel = False

        self.download_frame = customtkinter.CTkFrame(
            self.parent.tab, fg_color=("white", "black"), height=80, width=400
        )
        self.download_frame.place(relx=1, rely=0.08, anchor="e")

        self.size = customtkinter.CTkLabel(self.download_frame, text=" / ")
        self.size.grid(row=1, column=1)

        self.download_label = customtkinter.CTkLabel(
            self.download_frame,
            text="Downloading...",
            font=("Roboto mono", 15),
        )
        self.download_label.grid(row=0, column=2, sticky="s")

        icon_download = customtkinter.CTkLabel(
            self.download_frame,
            text="",
        )
        icon_download.grid(row=1, column=0)
        if get_setting(self.id, "theme") == "Light":
            icon_download.configure(image=download_icon)
        else:
            icon_download.configure(image=download_icon_light)

        self.progressBar = customtkinter.CTkProgressBar(
            self.download_frame, width=200)
        self.progressBar.grid(row=1, column=2)
        self.progressBar.set(0)
        self.percent = customtkinter.CTkLabel(self.download_frame, text=" % ")
        self.percent.grid(row=1, column=3)

        # cancel button
        customtkinter.CTkButton(
            self.download_frame,
            text=" X ",
            font=("", 15, "bold"),
            width=15,
            fg_color=("white", "black"),
            hover_color=("#808080"),
            text_color=("black", "white"),
            command=self.cancel_download,
        ).grid(row=1, column=4)

        threading.Thread(target=self.download).start()

    def download(self):
        try:
            ql_data = get_setting(self.id, "ql")
            location = get_setting(self.id, "location")
            quality = ql_data.strip("p")
            if quality[0] == "2":
                quality = 2160
            if ql_data == "1440p(2k)":
                quality = 1440

            if get_setting(self.id, "type") == "Mp4":

                option = {
                    "progress_hooks": [self.progress_hook],
                    "format": f"bestvideo[height={quality}]+bestaudio/best",
                    "outtmpl": rf"{location}\({ql_data})%(title)s.%(ext)s",
                }

            else:
                option = {
                    "progress_hooks": [self.progress_hook],
                    "format": "bestaudio/best",
                    "outtmpl": rf"{location}\(audio)%(title)s.%(ext)s",
                }
            with yt_dlp.YoutubeDL(option) as yld:

                infos = yld.extract_info(self.video_url, download=True)
                filename = yld.prepare_filename(infos)

                messagebox.showinfo(
                    "Download Complete",
                    f"Your video was downloaded successfully at {filename}",
                )

            current_time = time.time()
            os.utime(filename, (current_time, current_time))
            self.download_frame.after(500, self.download_frame.destroy)
        except Exception as e:
            messagebox.showinfo("Download Cancelled", e)
            if self.download_frame.winfo_exists():
                self.download_frame.after(500, self.download_frame.destroy)

    def progress_hook(self, d):

        global total_mb
        if self.cancel:
            raise Exception("Download Cancelled")

        if d["status"] == "downloading":
            total_bytes = d.get("total_bytes")
            downloaded_bytes = d.get("downloaded_bytes")
            downloaded_mb = int(downloaded_bytes / 1000000)
            total_mb = int(total_bytes / 1000000)

            if total_bytes is not None and downloaded_bytes is not None:
                progress = int(downloaded_bytes / total_bytes * 100)

                self.size.configure(text=f" {downloaded_mb}/{total_mb} MB ")
                self.percent.configure(text=f" {progress}% ")

                self.progressBar.set(progress / 100)
                self.parent.frame.update_idletasks()

        elif d["status"] == "finished":

            self.progressBar.set(1)
            self.parent.frame.update_idletasks()
            self.download_label.configure(text="Download Complete")
            self.percent.configure(text=" 100% ")

    def cancel_download(self):
        self.cancel = True
        self.download_frame.after(500, self.download_frame.destroy)


def search(c):
    threading.Thread(target=Search, args=(c,)).start()


class Search:
    def __init__(self, c):
        self.id = get_user_id()
        self.root = customtkinter.CTkToplevel()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.after(10, self.root.lift)
        self.root.title("Preview Video")
        self.root.geometry("600x400")

        self.is_playing = True
        self.video_frame = customtkinter.CTkFrame(self.root)
        self.video_frame.pack(fill="both", expand=True)

        if get_setting(self.id, "theme") == "Light":

            self.play = customtkinter.CTkImage(
                PIL.Image.open("Icons/play-button_724963.png"), size=(20, 20)
            )
            self.pause_icon = customtkinter.CTkImage(
                PIL.Image.open("Icons/pause _icon.png"), size=(20, 20)
            )
        else:
            self.play = customtkinter.CTkImage(
                PIL.Image.open("Icons/play-button-White.png"), size=(20, 20)
            )
            self.pause_icon = customtkinter.CTkImage(
                PIL.Image.open("Icons/pause _icon_white.png"), size=(20, 20)
            )
        self.play_pause_button = customtkinter.CTkButton(
            self.root,
            text=None,
            image=self.pause_icon,
            fg_color=("#ebebeb", "#242424"),
            hover_color=("#ebebeb", "#242424"),
            state = DISABLED,
            command=self.stop_video,
        )
        self.play_pause_button.pack()

        download_button = customtkinter.CTkButton(
            self.root,
            text="Download",
            image=(
                download_icon
                if get_setting(self.id, "theme") == "Light"
                else download_icon_light
            ),
            compound="left",
            font=("Roboto mono", 15),
            fg_color=("#D3D3D3", "#2d2d2d"),
            hover_color=("white", "#383838"),
            text_color=("black", "white"),
            state = DISABLED,
            command=lambda: Download(c, video_url, self),
        )
        download_button.pack(pady=5)
        null = customtkinter.CTkLabel(
            self.root, text=" ", height=10).pack()

        video_url = c.entry.get()
        player_url = link(video_url)
        if player_url:
            self.player = vlc.MediaPlayer(player_url)

            self.player.set_hwnd(self.video_frame.winfo_id())
            self.player.play()
            self.play_pause_button.configure(state = NORMAL)
            download_button.configure(state = NORMAL)

    def stop_video(self):
        if self.is_playing:
            self.player.pause()
            self.is_playing = False
            self.play_pause_button.configure(image=self.play)
        else:
            self.play_pause_button.configure(image=self.pause_icon)

            self.player.play()
            self.is_playing = True

    def on_closing(self):
        self.player.stop()
        self.root.destroy()


def link(url):
    option = {"format": "best"}

    with yt_dlp.YoutubeDL(option) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            video_url = info.get("url", None)
            return video_url
        except Exception as e:
            messagebox.showerror("Error", e)
            return None


def Download(root, url, preview_frame):
    Download_UI(root, url, preview_frame)
