# YouTube Downloader 🎬

A simple Python-based YouTube downloader built with **Python, yt-dlp, and FFmpeg**. It allows users to download individual YouTube videos in supported formats, preferring MP4 and video quality up to 720p when available.

## ✨ Features

- Download YouTube videos using a URL.
- Select video quality up to 720p when available.
- Download a single video instead of an entire playlist.
- Save downloaded videos to a specified folder.
- Use FFmpeg for media processing and format merging when needed.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Main programming language |
| yt-dlp | Extracts media information and downloads videos |
| FFmpeg | Processes and merges audio/video formats |
| VS Code | Code editor and development environment |

## 📋 Requirements

- Python 3.13 or compatible Python version
- yt-dlp
- FFmpeg

## ⚙️ Installation and Setup

### 1. Install yt-dlp

Open your terminal and run:

```bash
python -m pip install -U yt-dlp
```

### 2. Install FFmpeg

On Windows, FFmpeg was installed using Windows Package Manager (`winget`):

```powershell
winget install --id Gyan.FFmpeg.Shared -e
```

Verify the installation:

```bash
ffmpeg -version
```

### 3. Verify yt-dlp

```bash
python -m yt_dlp --version
```

If both commands display version information, the tools are ready to use.

## 📁 Project Structure

```text
Youtube/
├── Video.py
├── Downloads/
├── README.md
└── LICENSE
```

- `Video.py` — Main Python downloader script.
- `Downloads/` — Folder where downloaded videos are saved.
- `README.md` — Project documentation.
- `LICENSE` — MIT License for the project.

## ▶️ How to Run

1. Open the project folder in VS Code.
2. Open the integrated terminal.
3. Run the downloader:

   ```bash
   python Video.py
   ```

4. Enter the YouTube video URL.
5. Wait for the download to complete.
6. Find the downloaded video in the `Downloads` folder.

## 🧰 Terminal Commands

| Command | Purpose |
|---|---|
| `python -m pip install -U yt-dlp` | Install or update yt-dlp |
| `winget install --id Gyan.FFmpeg.Shared -e` | Install FFmpeg |
| `ffmpeg -version` | Verify FFmpeg |
| `python -m yt_dlp --version` | Verify yt-dlp |
| `python Video.py` | Run the downloader |

## 🐛 Troubleshooting

### FFmpeg is not recognized

- Reopen the terminal.
- Run `ffmpeg -version` again.
- Check that FFmpeg's `bin` directory is included in the Windows PATH environment variable.

### YouTube asks for sign-in verification

YouTube may sometimes block downloads and request additional verification.

- Update yt-dlp.
- Retry later if the issue is temporary.
- Consult the [official yt-dlp FAQ](https://github.com/yt-dlp/yt-dlp/wiki/FAQ).

### The downloader tries to download a playlist

Check that the downloader is configured to download individual videos rather than entire playlists.

### The downloaded video stutters or lags

- Try playing the video in [VLC Media Player](https://www.videolan.org/vlc/).
- Try a lower video resolution.
- Check whether the issue occurs in other video players.

## 🔒 Safety and Responsible Use

- Download yt-dlp and FFmpeg from official websites or trusted sources.
- Never commit passwords, authentication data, or other private information.
- Respect copyright, YouTube's terms, and applicable permissions.
- Use this project for content you own or are authorized to download.

## 🚀 Future Improvements

- Add a graphical user interface using CustomTkinter.
- Allow users to select video resolution.
- Display download progress and status.
- Allow users to choose the destination folder.
- Improve error handling and user feedback.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

**Built with Python, yt-dlp, and FFmpeg.**
