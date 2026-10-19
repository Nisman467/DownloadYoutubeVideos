
import yt_dlp

url = input("YouTube URL: ")


ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "cookiesfrombrowser": ("firefox",),
    "noplaylist": True,
    "outtmpl": r"D:\Youtube\Downloads\%(title)s.%(ext)s",
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
