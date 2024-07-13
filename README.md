# 4K YouTube Downloader with UI

By using this customtkinter GUI application, you can download YouTube videos up to 4K resolution.


![Screenshot of the Home tab with light theme](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/Home_tab_light.png)


![Screenshot of the Home tab with dark theme](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/Home_tab_dark.png)



By pasting a YouTube video URL, you will be able to preview the video before downloading it in the pop-up preview window.
You will also be able to pause and play the video, as well as download it in any available resolution, by clicking the download button.



![Screenshot of the preview window](https://github.com/S0KPiseth/4k-youtube-downloader-with-UI/blob/main/Screenshots/Video_preview.png)](https://www.youtube.com/watch?v=CY5WLrSYPzo)


After clicking the download button, it will pop up a new frame on the home tab to show the process of the download, and you can also cancel the download by clicking the "X" button.
## Installation

To install and set up the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/S0KPiseth/4k-youtube-downloader-with-UI.git
    cd 4k-youtube-downloader-with-UI
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Install ffmpeg:
   - **Linux**: Install via package manager (e.g., `apt-get install ffmpeg` on Debian-based systems).
   - **macOS**: Install using Homebrew (`brew install ffmpeg`).
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

## Usage

To use this project, run the following command:

```bash
python UI.py
```
Or run UI.py file directly from your IDE
