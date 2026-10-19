
import yt_dlp

url = input("YouTube URL: ")

ydl_opts = {
    "format": "bestaudio/best",
    "cookiesfrombrowser": ("firefox",),
    "noplaylist": True,
    "outtmpl": r"D:\Youtube\Downloads\%(title)s.%(ext)s",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
