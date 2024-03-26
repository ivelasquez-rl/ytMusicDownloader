from pytube import YouTube
from moviepy.editor import *
import glob
import os


def download_music(url):
    yt = YouTube(url)
    streams = yt.streams.filter(only_audio=True, mime_type="audio/mp4")
    if len(streams) > 0:
        streams[0].download()


def convert_to_mp3():
    files = [f for f in glob.glob("*.mp4")]
    for file in files:
        AudioFileClip(file).write_audiofile(file.split(".")[0] + ".mp3")
        os.remove(file)


if __name__ == '__main__':
    music_list = [
        "insert YT links here, one by string"
    ]

    for i in music_list:
        download_music(i)
        convert_to_mp3()
