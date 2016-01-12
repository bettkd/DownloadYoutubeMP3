import csv
from parse_youtube import getURI


YOUTUBE_URL = "https://youtube.com"

def getVideoURLs(fname):
	videoURLs = []
	playlist = csv.reader(open(fname, 'rU'), dialect=csv.excel_tab)
	for row in playlist:
		artist, song = row
		query = "/results?search_query="+artist.strip().replace(" ", "+")+"+-+"+song.strip().replace(" ", "+")
		URI = getURI(YOUTUBE_URL + query)
		videoURL = YOUTUBE_URL + URI
		print videoURL
		videoURLs.append(videoURL)
	return videoURLs

fname = "playlist.txt"
getVideoURLs(fname)