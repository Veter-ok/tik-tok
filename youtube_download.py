import pytube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

with open('urls.txt', 'r') as file: 
	for url in file:
		youtube = pytube.YouTube(url)
		video = youtube.streams.get_highest_resolution()

		video.download('../')
		print(f"{url[:-1]} - Done!")