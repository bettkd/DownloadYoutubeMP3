from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
import sys
import csv
import cookielib
from cookielib import CookieJar
import random
import re

# Beautiful Soup Initial Func
def make_soup(url):
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	agents = ["Chrome/19.0.1084.52", "Safari/536.5", "Mozilla/5.0", "Chrome/19.0.1084.52"]
	opener.addheaders = [('User-agent', random.choice(agents))]
	data = opener.open(url).read()
	soup = BeautifulSoup(data, "html.parser")
	soup.prettify()
	return (soup)

# Func to extract info(URIs) from the "Soup"
def getURI(url):
	soup = make_soup(url)
	
	videos = soup.find_all("div",
        {"class": lambda x: x and x == "yt-lockup-content"})
	
	# Get the first verified video or the most viewd video
	my_video = ""
	views = 0
	for video in videos:
		if "Verified" in str(video) or "itunes" in str(video):
			my_video = video
			break
		else:
			results = re.findall(r"ago</li><li>(.*) views</li>", str(video))
			if results :
				_views = int(results[0].replace(",", ""))
				if _views > views:
					views = _views
					my_video = video

	URI = my_video.find_all("a")[0].get("href")
	return URI