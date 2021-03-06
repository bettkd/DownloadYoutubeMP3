# DownloadYoutubeMP3
Downloads all the right mp3 from youtube from a given artist(s) and/or song name

## INSTALLATION
Clone the project (although it would be preferable to fork it so that you can contribute & fix issues)
```bash
$git clone git@github.com:bettkd/DownloadYoutubeMP3.git
```

To install dependancies, run the following on the terminal
```bash
$sudo pip install -r requirements.txt
```

## USAGE:

```bash
Usage:
	$python downloadmp3.py -i <playlistFile> -o <outputDirectory>
	or
	$python downloadmp3.py -a <artist> -t <title> -o <outputDirectory>
Options:
	-i	specify input (path to a playlist file)
	-o	provide the destination folder other (default: ~/Downloads/YoutubeDownload/)
	-t	specify the title (default: "Jason Mraz")
	-a 	specify artist (default: "I'm yours")
	-h	help
```

### Example text file ```playlist.txt```
|				Song   			                 	|
|:----------------:--------------------------------:|
|MercyMe          Greater                           |
|Newsboys         We Believe                        |
|MercyMe          I Can Only Imagine                |
|Chris Tomlin     Amazing Grace (My Chains Are Gone)|
|Matt Redman      "10,000 Reasons"                  |
|Newsboys         God's Not Dead                    |
|Chris Tomlin     How Great Is Our God              |
|MercyMe          Word ofGod Speak                  |
|Casting Crowns   Who Am I                          |
|Matthew West     "Hello, My Name Is"               |

> Test Run 
```bash
	python downloadmp3.py -i Playlists/playlist_top100Kenya_2016.txt -o ~/Desktop/KENYAN_MUSIC
```

## STORY
I love listening to contemporary christian music. So I went online to find the top 100 music to download, but all I found was a list. An amazing list of all the songs I wanted on my iPod. Now the challenge what do I do so that I can download not just all the songs in the list, but the best/verified versions of the songs. Popular web apps such as http://www.youtube-mp3.org/ need approximately 3-4 minutes to per video. That is the time I have tp download 100 songs. I know, right? Instinctively, I wrote these scripts to automate the proccess. Now all I need is the list of songs I want, and I got it in MP3 format! Yaay!

I hope this hack can help you too..
