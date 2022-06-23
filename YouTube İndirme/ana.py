from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    print("İndiriliyor...")

def on_complete(stream, file_path):
    print("İndirildi")

yt = YouTube(
        url=input("Video linkini giriniz:\n"),
        on_progress_callback=on_progress,
        on_complete_callback=on_complete,
        use_oauth=False,
        allow_oauth_cache=True
    )

yt.streams.get_highest_resolution().download()




