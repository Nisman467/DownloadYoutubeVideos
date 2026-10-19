# YouTube Downloader 🎬

A simple Python-based YouTube downloader using **yt-dlp** and **FFmpeg**. This project downloads YouTube videos in supported formats and can also be configured to download audio as MP3.

## 📌 Features

- Download YouTube videos using a URL.
- Select video quality up to 720p when available.
- Download a single video instead of an entire playlist.
- Save downloaded videos to a specified folder.
- Use FFmpeg to process and merge media formats when needed.
- Support audio-only downloads and MP3 conversion.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Main programming language |
| yt-dlp | Extracts media information and downloads videos and audio |
| FFmpeg | Processes, merges, and converts audio/video |
| VS Code | Code editor and development environment |

## 📋 Requirements

Before running this project, install:

1. **Python 3.13** — [Official Python website](https://www.python.org/downloads/)
2. **FFmpeg** — [Official FFmpeg website](https://ffmpeg.org/download.html)
3. **yt-dlp** — Installed using Python's package manager, pip.

## ⚙️ Installation and Setup

### 1. Install yt-dlp

Open your terminal and run:

```bash
python -m pip install -U yt-dlp
```

This installs or updates yt-dlp.

### 2. Install FFmpeg

On Windows, FFmpeg was installed using Windows Package Manager (`winget`):

```powershell
winget install --id Gyan.FFmpeg.Shared -e
```

Verify the installation:

```bash
ffmpeg -version
```

If version information appears, FFmpeg is accessible from the terminal.

If `ffmpeg` is not recognized, reopen the terminal and check whether FFmpeg's `bin` directory is included in the Windows PATH environment variable.

### 3. Verify yt-dlp

Run:

```bash
python -m yt_dlp --version
```

If a version number appears, yt-dlp is installed correctly.

## 📁 Project Structure

```text
Youtube/
├── Video.py
├── Downloads/
└── README.md
```

- `Video.py` — Python script that downloads YouTube videos.
- `Downloads/` — Destination folder for downloaded videos.
- `README.md` — Project documentation.

Create the `Downloads` folder if it does not already exist.

## 💻 Python Code

The following example downloads a single video, preferring MP4 and selecting a format up to 720p when available.

```python
import yt_dlp

url = input("YouTube URL: ")

ydl_opts = {
    "format": "best[height<=720][ext=mp4]/best[height<=720]",
    "noplaylist": True,
    "outtmpl": r"D:\Youtube\Downloads\%(title)s.%(ext)s",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

Save the script as `Video.py`.

### Understanding the Code

- `import yt_dlp` — Imports the downloader library.
- `input()` — Asks the user to enter a YouTube URL.
- `format` — Selects a suitable video format up to 720p.
- `noplaylist` — Prevents downloading an entire playlist.
- `outtmpl` — Defines the destination folder and filename.
- `YoutubeDL()` — Creates a downloader using the specified options.
- `download()` — Starts the download.

**Note:** The available video quality and format depend on the source video.

## ▶️ How to Run

1. Open the project folder in VS Code.
2. Open the integrated terminal.
3. Run:

```bash
python Video.py
```

4. Enter the YouTube video URL.
5. Wait for the download to finish.
6. Open the `Downloads` folder to find your file.

## 🔊 Optional: Download Audio as MP3

To download audio instead of video, configure yt-dlp to use FFmpeg for audio extraction and conversion.

```python
import yt_dlp

url = input("YouTube URL: ")

ydl_opts = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "outtmpl": r"D:\Youtube\Downloads\%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

This downloads the best available audio and converts it to MP3 with a target quality setting of 192 kbps.

## 🧰 Terminal Commands Used

| Command | Purpose |
|---|---|
| `python -m pip install -U yt-dlp` | Install or update yt-dlp |
| `winget install --id Gyan.FFmpeg.Shared -e` | Install FFmpeg using winget |
| `ffmpeg -version` | Check the FFmpeg installation |
| `python -m yt_dlp --version` | Check the yt-dlp version |
| `python Video.py` | Run the downloader |

## 🐛 Common Problems

### FFmpeg is not recognized

- Verify the installation using `ffmpeg -version`.
- Reopen the terminal.
- Check the Windows PATH configuration if necessary.

### YouTube asks for sign-in verification

YouTube may sometimes require additional verification and block a download.

- Update yt-dlp using `python -m pip install -U yt-dlp`.
- Retry later if the issue appears temporary.
- Consult the [official yt-dlp FAQ](https://github.com/yt-dlp/yt-dlp/wiki/FAQ) for troubleshooting.

### The downloader tries to download an entire playlist

Ensure this option is present:

```python
"noplaylist": True,
```

### The downloaded video stutters or lags

- Try playing the video in [VLC Media Player](https://www.videolan.org/vlc/).
- Try downloading at a lower resolution.
- Check whether the problem occurs in other video players.

## 🔒 Safety and Responsible Use

- Download yt-dlp and FFmpeg from official websites or trusted distribution sources.
- Never upload passwords, authentication data, or other private information to GitHub.
- Respect copyright, YouTube's terms, and the permissions applicable to downloaded content.
- Use this project for content you own or are authorized to download.

## 🚀 Future Improvements

- Add a graphical user interface using CustomTkinter.
- Allow users to select video resolution.
- Add download progress and status messages.
- Support audio-only and MP3 downloads.
- Allow users to choose the destination folder.
- Add clearer error messages and improved error handling.

## 📄 License

This project is provided for educational purposes. A license has not yet been specified. Choose an appropriate license and add a `LICENSE` file if you want to grant others permission to use, modify, or distribute your code.

---

**Built with Python, yt-dlp, and FFmpeg.**
