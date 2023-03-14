from pytube import YouTube
import os


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        video_file = youtubeObject.download()
        base, ext = os.path.splitext(video_file)
        audio_file = base + '.wav'
        os.rename(video_file, audio_file)

    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")

Download(link)