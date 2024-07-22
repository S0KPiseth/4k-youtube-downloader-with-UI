![image](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/hometab.gif)
# 4K YouTube Downloader with UI

By using this customtkinter GUI application, you can download YouTube videos up to 4K resolution.


<a href="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/Home_tab_dark.png">
    <img src="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/Home_tab_dark.png" alt="Home Tab Dark" width="600" />
</a>

## Setting Tab

<a href="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/setting_tab.png">
    <img src="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/setting_tab.png" alt="Setting Tab" width="600" />
</a>

By pasting a YouTube video URL, you will be able to preview the video before downloading it in the pop-up preview window.
You will also be able to pause and play the video, as well as download it in any available resolution, by clicking the download button.

<a href="https://www.youtube.com/watch?v=CY5WLrSYPzo">
    <img src="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/Video_preview.png" alt="Video Preview" width="600" />
</a>

After clicking the download button, it will pop up a new frame on the home tab to show the process of the download, and you can also cancel the download by clicking the "X" button.

<a href="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/download.png">
    <img src="https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/download.png" alt="Download Process" width="600" />
</a>


## Installation

To install and set up the project, follow these steps:

1. Install ffmpeg:
   - **Linux**: Install via package manager (e.g., `apt-get install ffmpeg` on Debian-based systems).
   - **macOS**: Install using Homebrew (`brew install ffmpeg`).
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

2. Install VLC
   - download VLC at [videolan.org](https://www.videolan.org/vlc/download-windows.html)
3. Clone the repository:
    ```bash
    git clone https://github.com/S0KPiseth/4k-youtube-downloader-with-UI.git
    cd 4k-youtube-downloader-with-UI
    ```

4. Run the following command to install the required library:
   
    ```bash
    pip install python-vlc customtkinter Pillow yt-dlp
    ```
## Usage

After finishing the installation step, to use this application, run the following command:
```bash
python UI.py
```
Or run UI.py file directly from your IDE
