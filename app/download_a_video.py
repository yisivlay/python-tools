from pytube import YouTube


def download_video_from_youtube(link_video, path):
    youtube_object = YouTube(link_video, use_oauth=True, allow_oauth_cache=True)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download(path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link_video = input("Enter the YouTube video URL: ")
# Target file path
download_video_from_youtube(link_video, 'your_target_path')
