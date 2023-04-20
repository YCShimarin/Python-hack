from pytube import YouTube
from moviepy.editor import *
import os

# YouTube video URL
url = "https://youtu.be/Eoa82dr2qqQ"


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size * 100
    print(f"Download progress: {progress:.2f}%")


try:
    # Mendownload video dan mengambil audio
    video = YouTube(url, on_progress_callback=on_progress)
    audio = video.streams.filter(only_audio=True).first()

    # Mengunduh audio dan menyimpan dalam format webm
    audio_file = audio.download()
    webm_file = audio_file.split(".")[0] + ".webm"
    os.rename(audio_file, webm_file)

    # Mengubah format audio ke mp3 dan menyimpannya dalam file mp3
    mp3_file = audio_file.split(".")[0] + ".mp3"
    AudioFileClip(webm_file).write_audiofile(mp3_file)

    # Menghapus file audio sementara
    os.remove(webm_file)

    print("Download dan konversi berhasil")
except Exception as e:
    print("Terjadi kesalahan: ", e)
