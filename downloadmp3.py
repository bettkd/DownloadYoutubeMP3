from __future__ import unicode_literals
import youtube_dl
import csv
from parse_youtube import getURI
import sys, os, getopt

YOUTUBE_URL = "https://youtube.com"

def getVideoURLs(fname):
	videoURLs = []
	playlist = csv.reader(open(fname, 'rU'), dialect=csv.excel_tab)
	for row in playlist:
		artist, title = row
		videoURLs.append(getVideoURL(artist, title))
	return videoURLs

def getVideoURL(artist="Jason Mraz", title="I'm yours"):
	query = "/results?search_query="+artist.strip().replace(" ", "+")+"+-+"+title.strip().replace(" ", "+")
	print ("\nNow loading %s by %s..."%(title, artist))
	URI = getURI(YOUTUBE_URL + query)
	videoURL = YOUTUBE_URL + URI
	return videoURL

def downloadMusic(videoURLs, downloadPath="~/Downloads/YoutubeDownload/"):
	if '~' in downloadPath:
		downloadPath = os.path.expanduser(downloadPath)
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

def main(argv):
	playlistFile = ''
	outputDirectory = ''
	title = ''
	artist = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:a:t:",["playlistFile=","outputDir=", "title=", "artist="])
	except getopt.GetoptError:
		print 'Error: Invalid arguements....\n'\
					'Usage: downloadmp3.py -i <playlistFile> -o <outputDirectory>\n'\
					'Other options:\n'\
					'\t -t <title> --> downloads a specific title\n'\
					'\t -a <artist> --> downloads a specific artist (single title)\n'\
					'\t -h --> help.\n'\
					'Default: '\
					"downloadmp3.py -a Jason Mraz -t I'm yours -o ~/Downloads/YoutubeDownload/"
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Usage: downloadmp3.py -i <playlistFile> -o <outputDirectory>\n'\
					'Other options:\n'\
					'\t -t <title> --> downloads a specific title\n'\
					'\t -a <artist> --> downloads a specific artist (single title)\n'\
					'\t -h --> help.\n'\
					'Default: '\
					'downloadmp3.py -a "Jason Mraz" -t "I\'m yours" -o ~/Downloads/YoutubeDownload/'
			sys.exit()
		elif opt in ('-i', '--playlistFile'):
			playlistFile = arg
		elif opt in ('-o', '--outputDirectory'):
			outputDirectory = arg
		elif opt in ('-t', '--title'):
			title = arg
		elif opt in ('-a', '--artist'):
			artist = arg

	try:
		if playlistFile:
			videoURLs = getVideoURLs(fname=playlistFile)
			if outputDirectory:
				downloadMusic(videoURLs, downloadPath=outputDirectory)
			else:
				downloadMusic(videoURLs)
		elif title or artist:
			videoURL = getVideoURL(title=title, artist=artist)
			if outputDirectory:
				downloadMusic([videoURL,], downloadPath=outputDirectory)
			else:
				downloadMusic([videoURL,])
		else:
			videoURL = getVideoURL()
			downloadMusic([videoURL])
	except Exception as e:
		print (e)
		pass

	print ("Done!")


if __name__ == '__main__':
	main(sys.argv[1:])