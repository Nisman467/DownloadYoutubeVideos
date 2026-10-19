
import yt_dlp

url = input("YouTube URL: ")


ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "noplaylist": True,
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
