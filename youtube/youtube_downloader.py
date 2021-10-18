from pytube import Playlist
from pytube import YouTube
import os

playlist = Playlist("your youtube playlist")

urls = []
i = 1
for url in playlist.video_urls:
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    destination = r"download destination here"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = f"{i}.mp3"
    os.rename(out_file, new_file)
    i += 1
