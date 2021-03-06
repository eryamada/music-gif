import json

import audioLyricSyncer
import lyricScraper
import youtubeToAudio
import gifAPI
import os.path
import pprint


def get_timestamped_gifs(youtube_url):
    song_filename = youtubeToAudio.youtube_to_audio(youtube_url)  # download audio, get the filename
    lyricScraper.scrape_lyrics(song_filename)  # scrape Bing for lyrics and output to txt
    audioLyricSyncer.sync_lyrics_to_audio(song_filename)  # sync lyrics with audio and output to JSON

    song_title = os.path.splitext(song_filename)[0]  # remove extension from title

    # Read in JSON to get synced lyrics
    with open(song_title + '.json', "r") as data_file:
        syncedLyricsJson = json.load(data_file)

    # Get the GIFs from Giphy
    timed_gifs = gifAPI.parse_lyrics(syncedLyricsJson)  # get the tuples of (time, gif_url)
    print 'Found GIFs, here they are with associated times: '
    pprint.pprint(timed_gifs)
    print 'DONE'
