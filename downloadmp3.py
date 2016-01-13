from __future__ import unicode_literals
import youtube_dl
import csv
from parse_youtube import getURI
import os

YOUTUBE_URL = "https://youtube.com"

def getVideoURLs(fname):
	videoURLs = []
	playlist = csv.reader(open(fname, 'rU'), dialect=csv.excel_tab)
	for row in playlist:
		artist, title = row
		videoURLs.append(getVideoURL(artist, title))
		break
	return videoURLs

def getVideoURL(artist, title):
	query = "/results?search_query="+artist.strip().replace(" ", "+")+"+-+"+title.strip().replace(" ", "+")
	print ("\nNow loading %s by %s..."%(title, artist))
	URI = getURI(YOUTUBE_URL + query)
	videoURL = YOUTUBE_URL + URI
	return videoURL

def downloadMusic(videoURLs, downloadPath="~/Downloads/YoutubeDownload/"):
	if not os.path.exists(os.path.dirname(downloadPath)):
		os.makedirs(os.path.dirname(downloadPath))
	ydl_opts = {
		'outtmpl': os.path.join(downloadPath, '%(title)s.%(ext)s'),
		'nocheckcertificate': True,
		'noplaylist' : True,
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(videoURLs)

def main():
	fname = "playlist.txt"
	videoURLs = getVideoURLs(fname)
	downloadMusic(videoURLs)

	print ("Done!")


if __name__ == '__main__':
	main()