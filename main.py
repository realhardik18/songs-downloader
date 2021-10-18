from googlesearch import search
from pytube import YouTube
import os
from name_getter import track_name_getter

playlist_idee = 'playlist id goes here'
songz = track_name_getter("spotify", playlist_idee)

for song in songz:
    song_name_for_search = song + " youtube"
    results = []
    for j in search(song_name_for_search, tld="co.in", num=1, stop=1, pause=2):
        results.append(j)
    vid_link = results[0]
    yt = YouTube(vid_link)
    video = yt.streams.filter(only_audio=True).first()
    destination = r"D:\songs"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = f"{song}.mp3"
    os.rename(out_file, new_file)
