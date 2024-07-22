from functions import *

default_path = os.path.join(os.path.expanduser("~"), "Downloads")


class Window:
    def __init__(self, frame):
        create_database()
        self.id = get_user_id()

        customtkinter.set_appearance_mode("light")
        self.frame = frame
        font = ("Roboto mono", 15)
        self.notebook = customtkinter.CTkTabview(
            self.frame,
            fg_color=("#EBEBEB", "#242424"),
            text_color=("#242424", "#EBEBEB"),
            segmented_button_fg_color=("#EBEBEB", "#242424"),
            segmented_button_selected_color=("#EBEBEB", "#242424"),
            segmented_button_selected_hover_color=("#EBEBEB", "#242424"),
            segmented_button_unselected_color=("#EBEBEB", "#242424"),
            segmented_button_unselected_hover_color=("#EBEBEB", "#242424"),
        )

        self.notebook.pack(fill="both", expand=True)
        self.notebook._segmented_button.configure(font=font)

        self.notebook.add("Home")
        self.tab = self.notebook.tab("Home")

        self.frame.title("Youtube downloader")
        self.frame.geometry("800x600")
        self.label = customtkinter.CTkLabel(
            self.tab, text="", font=("Roboto mono", 50), justify="left"
        )
        self.label.place(relx=0.05, rely=0.35, anchor="w")

        self.search_icon = customtkinter.CTkImage(
            PIL.Image.open("Icons/search-interface-symbol_54481.png"), size=(25, 25)
        )
        self.entry = customtkinter.CTkEntry(
            self.tab, font=("Roboto mono", 20), width=500
        )
        self.entry.place(relx=0.15, rely=0.7, anchor="w")
        self.entry.insert(0, "Type video url here...")

        self.button = customtkinter.CTkButton(
            self.tab,
            text=None,
            image=self.search_icon,
            width=50,
            fg_color=("#EBEBEB", "#242424"),
            hover_color=("white", "#383838"),
            command=lambda: search(self),
        )
        self.button.place(relx=0.79, rely=0.7, anchor="w")

        self.entry.bind("<Button-1>", lambda event: type(self))

        self.entry.bind("<Return>", lambda event: search(self))

        customtkinter.CTkLabel(
            self.tab,
            text=None,
            image=customtkinter.CTkImage(
                PIL.Image.open("Icons/sticker1.png"), size=(350, 200)
            ),
        ).place(relx=1, rely=0.35, anchor="e")


class setting(Window):
    def __init__(self, Frame):
        super().__init__(frame=Frame)

        self.t = StringVar()
        self.x = StringVar()
        self.ex = StringVar()
        self.ql = StringVar()
        self.ac = IntVar()
        self.animate = StringVar()

        # default value

        setting_dict = {
            "type": "Mp4",
            "theme": "Light",
            "ql": "720p",
            "location": str(default_path),
            "text": "Enable",
        }
        default_setting(self.id, setting_dict=setting_dict)
        self.ex.set(get_setting(self.id, "type"))
        self.x.set(get_setting(self.id, "theme"))
        self.ql.set(get_setting(self.id, "ql"))
        self.t.set(get_setting(self.id, "location"))
        self.animate.set(get_setting(self.id, "text"))

        self.notebook.add("Setting")
        self.setting = self.notebook.tab("Setting")

        self.setting.grid_columnconfigure((2, 4), weight=1)

        # theme
        customtkinter.CTkLabel(
            self.setting, text="Set theme: ", font=("Roboto mono", 15, "bold"), anchor=W
        ).grid(row=0, column=0, padx=10, pady=15, sticky="ew")
        option = ["Light", "Dark"]
        place = 0
        for i in option:
            place += 1
            self.theme_option = customtkinter.CTkRadioButton(
                self.setting, text=i, font=("Roboto mono", 15), value=i, variable=self.x
            )
            self.theme_option.grid(row=0, column=place, pady=15)

        # quality
        customtkinter.CTkLabel(
            self.setting,
            text="Set video quality: ",
            font=("Roboto mono", 15, "bold"),
            anchor=W,
        ).grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.quality_option = customtkinter.CTkComboBox(
            self.setting,
            values=("2160p(4k)", "1440p(2k)", "1080p", "720p", "480p", "360p"),
            font=("Roboto mono", 15),
            state="readonly",
            variable=self.ql,
        )
        self.quality_option.grid(row=4, column=1, pady=5)

        customtkinter.CTkLabel(
            self.setting,
            text="Set default download folder: ",
            font=(
                "Roboto mono",
                12,
            ),
        ).grid(row=3, column=0, padx=10)
        self.directory = customtkinter.CTkEntry(
            self.setting,
            font=("Roboto mono", 12),
            textvariable=self.t,
            state=DISABLED,
            width=40,
        )
        self.directory.grid(row=3, column=1, columnspan=2, sticky="ew")
        Browse = customtkinter.CTkButton(
            self.setting,
            text="...",
            width=10,
            fg_color="light grey",
            hover_color="dark grey",
            text_color="black",
            command=self.browse,
            state=DISABLED,
        )
        Browse.grid(row=3, column=3, sticky="w")

        # directory
        self.allow_change = customtkinter.CTkCheckBox(
            self.setting,
            text="I wish to change directory",
            font=("Roboto mono", 15, "bold"),
            variable=self.ac,
            command=lambda: (
                Browse.configure(state=NORMAL)
                if self.ac.get()
                else Browse.configure(state=DISABLED)
            ),
        )
        self.allow_change.grid(row=2, column=0, padx=10, sticky="ew")

        # type
        customtkinter.CTkLabel(
            self.setting,
            text="Set file type: ",
            font=("Roboto mono", 15, "bold"),
            anchor=W,
        ).grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.type = customtkinter.CTkComboBox(
            self.setting,
            values=("Mp4", "Mp3"),
            font=("Roboto mono", 15),
            state="readonly",
            variable=self.ex,
            command=lambda e: (
                (self.quality_option.configure(state="readonly"), self.ql.set("720p"))
                if self.ex.get() == "Mp4"
                else (
                    self.quality_option.configure(state="disabled"),
                    self.ql.set("Mp3 quality"),
                )
            ),
        )
        self.type.grid(row=1, column=1, pady=5)
        # text animation
        customtkinter.CTkLabel(
            self.setting,
            text="Text Animation: ",
            font=("Roboto mono", 15, "bold"),
            anchor=W,
        ).grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        option = ["Enable", "Disable"]
        place = 0
        for i in option:
            place += 1
            self.theme_option = customtkinter.CTkRadioButton(
                self.setting,
                text=i,
                font=("Roboto mono", 15),
                value=i,
                variable=self.animate,
            )
            self.theme_option.grid(row=5, column=place, pady=20)

    def browse(self):
        self.t.set(filedialog.askdirectory())


class change(setting, Window):
    def __init__(self, frame):
        super().__init__(Frame=frame)

        self.background_text = text_animation(self.label)

        customtkinter.CTkButton(
            self.setting,
            text="Apply",
            command=self.apply,
            font=("Roboto mono", 15),
        ).grid(row=6, column=2, sticky="e")
        customtkinter.CTkButton(
            self.setting,
            text="Cancel",
            fg_color="white",
            text_color="black",
            font=("Roboto mono", 15),
            border_color=("black"),
            border_width=1.5,
            hover_color="light grey",
        ).grid(row=6, column=3)

    def apply(self):
        # update setting

        setting_dict = {
            "type": self.ex.get(),
            "theme": self.x.get(),
            "ql": self.ql.get(),
            "location": self.t.get(),
            "text": self.animate.get(),
        }
        update_setting(self.id, setting_dict=setting_dict)
        # theme
        if get_setting(self.id, "theme") == "Light":
            customtkinter.set_appearance_mode("light")

            self.search_icon = customtkinter.CTkImage(
                PIL.Image.open("Icons/search-interface-symbol_54481.png"), size=(25, 25)
            )

        else:
            customtkinter.set_appearance_mode("dark")
            self.search_icon = customtkinter.CTkImage(
                PIL.Image.open("Icons/search-interface-symbol-white.png"), size=(25, 25)
            )

        self.button.configure(image=self.search_icon)

        if get_setting(self.id, "text") == "Enable":
            self.background_text.start()
        else:

            self.background_text.stop()


class credit(change):
    def __init__(self, frame):
        super().__init__(frame)
        self.notebook.add("Credit")
        self.credit = self.notebook.tab("Credit")

        credit_frame = customtkinter.CTkScrollableFrame(
            self.credit, orientation="horizontal"
        )
        credit_frame.pack(fill="both", expand=True)
        text = customtkinter.CTkTextbox(
            credit_frame, font=("Roboto mono", 15), width=1920, height=1080
        )
        text.pack(fill="both", expand=True)
        with open("Credit.txt", "r") as f:
            text.insert("1.0", f.read())


def close(frame, a):

    a.bool = False
    a.background_text.stop()

    frame.destroy()


root = customtkinter.CTk()


window = credit(root)
window.apply()

root.protocol("WM_DELETE_WINDOW", lambda: close(root, window))
root.resizable(False, False)


root.mainloop()
