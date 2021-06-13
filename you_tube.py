from pytube import YouTube

video_list = []

for i in video_list:
    try:
        yt = YouTube(i)
        print("Downloading the link: "+i)
        print("Downloading the video: "+yt.streams[0].title)
    except:
        print("Connetion error")
        
    stream = yt.streams.filter(res="480p").first()
    stream.download("Downloads/")

print("Task Completed")