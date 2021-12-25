import pytube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

url = 'https://www.youtube.com/watch?v=8r7fXLlBUsg'

youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()

video.download()
print("Done!")