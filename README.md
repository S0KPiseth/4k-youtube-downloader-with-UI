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


## Installing

### Prerequisites

- Windows operating system
- [VLC Media Player](https://www.videolan.org/vlc/index.html)
- [FFmpeg](https://ffmpeg.org/download.html) (added to the system path)

### Option 1: Running from the Python Code

#### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

#### Installation Steps

1. **Install VLC Media Player:**
    - Download and install VLC from [here](https://www.videolan.org/vlc/index.html).

2. **Install FFmpeg:**
    - Download the appropriate version for Windows from [here](https://ffmpeg.org/download.html).
    - Extract the downloaded zip file to a location of your choice, e.g., `C:\ffmpeg`.

3. **Add FFmpeg to the System Path:**
    - Open the Start Menu and search for "Environment Variables".
    - Click on "Edit the system environment variables".
    - In the System Properties window, click on the "Environment Variables" button.
    - In the Environment Variables window, find the `Path` variable under System variables and select it, then click "Edit".
    - Click "New" and add the path to the `bin` folder inside your FFmpeg directory, e.g., `C:\ffmpeg\bin`.
    - Click "OK" to close all windows.

4. **Clone the repository:**
    ```sh
    https://github.com/S0KPiseth/4k-youtube-downloader-with-UI.git
    cd 4k-youtube-downloader-with-UI
    ```

5. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

6. **Activate the virtual environment:**
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

7. **Install the required dependencies using pip:**
    ```sh
    pip install python-vlc customtkinter Pillow yt-dlp
    ```
8. **Run the application:**
    ```sh
    python UI.py
    ```

### Option 2: Running from the Executable File

1. **Download the executable file from the [releases page](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/releases/tag/v1.1).**

2. **Install VLC Media Player:**
    - Download and install VLC from [here](https://www.videolan.org/vlc/index.html).

3. **Install FFmpeg:**
    - Download the appropriate version for Windows from [here](https://ffmpeg.org/download.html).
    - Extract the downloaded zip file to a location of your choice, e.g., `C:\ffmpeg`.

4. **Add FFmpeg to the System Path:**
    - Open the Start Menu and search for "Environment Variables".
    - Click on "Edit the system environment variables".
    - In the System Properties window, click on the "Environment Variables" button.
    - In the Environment Variables window, find the `Path` variable under System variables and select it, then click "Edit".
    - Click "New" and add the path to the `bin` folder inside your FFmpeg directory, e.g., `C:\ffmpeg\bin`.
    - Click "OK" to close all windows.

5. **Run the executable file:**
    - Locate the downloaded `.exe` file.
    - Double-click the `.exe` file to run the installer.
    - Follow the on-screen instructions to complete the installation.
    - After installation, you can launch the application from the Start menu or the desktop shortcut.
## How to Contribute

We welcome contributions to this project! Here are some ways you can contribute:

### Reporting Bugs

If you find a bug, please report it by opening an issue on the [GitHub issues page](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/issues). Please include details about the bug, including steps to reproduce it and any relevant log messages.

### Suggesting Features

Have an idea for a new feature? We would love to hear about it! Open an issue on the [GitHub issues page](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/issues) and describe your idea.

### Submitting Pull Requests

To contribute code, fork the repository, create a new branch, make your changes, and open a pull request. 

