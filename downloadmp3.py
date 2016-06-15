#from __future__ import unicode_literals
import youtube_dl
import csv
from parse_youtube import getURI
import sys, os, getopt
import threading
import Queue

reload(sys)
sys.setdefaultencoding('utf8') # Set default encoding to UTF-=8

YOUTUBE_URL = "https://youtube.com" # Youtube root url

q = Queue.Queue() # Thread queue

# Function to read multiple YouTube URLs
def getVideoURLs(fname):
	videoURLs = []
	playlist = csv.reader(open(fname, 'rU'), delimiter=" ")
	for row in playlist:
		song = '+'.join(row)
		t = threading.Thread(target=getVideoURL, args=(song,))
		t.start()
		t.join()
		videoURL = q.get()
		videoURLs.append(videoURL)
	return videoURLs

# Function to fetch the YouTube music URL. Uses the parse_youtube module to extract the information
def getVideoURL(song="I'm yours"):
	"""
	"""
	query = "/results?search_query="+song.strip().replace("\"", "").replace("\'", "")[:40]
	print ("\nRetrieving link for %s "%song)
	URI = getURI(YOUTUBE_URL + query)
	videoURL = YOUTUBE_URL + URI
	q.put(videoURL)
	#return videoURL

# Function to download and proceess music. Takes in the Youtube URL and destination folder as params
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
			'preferredquality': '256',
		}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(videoURLs)

def main(argv):
	playlistFile = ''
	outputDirectory = ''
	song = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:s:",["playlistFile=","outputDir=", "song="])
	except getopt.GetoptError:
		print 'Error: Invalid arguements....\n'\
					'Usage: downloadmp3.py -i <playlistFile> -o <outputDirectory>\n'\
					'Other options:\n'\
					'\t -t <song> --> downloads a specific song\n'\
					'\t -h --> help.\n'\
					'Default: '\
					"downloadmp3.py -s 'Jason Mraz I'm yours' -o ~/Downloads/YoutubeDownload/"
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Usage: downloadmp3.py -i <playlistFile> -o <outputDirectory>\n'\
					'Other options:\n'\
					'\t -t <song> --> downloads a specific song\n'\
					'\t -h --> help.\n'\
					'Default: '\
					'downloadmp3.py -s "Jason Mraz I\'m yours" -o ~/Downloads/YoutubeDownload/'
			sys.exit()
		elif opt in ('-i', '--playlistFile'):
			playlistFile = arg
		elif opt in ('-o', '--outputDirectory'):
			outputDirectory = arg
		elif opt in ('-s', '--song'):
			song = arg

	try:
		if playlistFile:
			videoURLs = getVideoURLs(fname=playlistFile)
			if outputDirectory:
				for videoURL in videoURLs:
					t = threading.Thread(target=downloadMusic, args=([videoURL], outputDirectory))
					t.start()
			else:
				downloadMusic(videoURLs)
		elif title or artist:
			videoURL = getVideoURL(song=song)
			if outputDirectory:
				downloadMusic([videoURL], downloadPath=outputDirectory)
			else:
				downloadMusic([videoURL])
		else:
			videoURL = getVideoURL()
			downloadMusic([videoURL])
	except Exception as e:
		print (e)
		pass

	print ("Loading...")


if __name__ == '__main__':
	main(sys.argv[1:])