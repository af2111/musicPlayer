import json
from youtube_search import YoutubeSearch
from constants import ydl
from os import listdir, system, name
from time import sleep
import config
import vlc

def clear():
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")
def downloadMP3(path):
    ydl.extract_info(path)

def search(query):
    return YoutubeSearch(query, max_results=10).to_dict()

def idToYtURL(id):
    return "https://www.youtube.com/watch?v=" + id

def playSong(path):
    p = vlc.MediaPlayer(path)
    p.play()
    sleep(0.1)
    sleep(p.get_length() // 1000 - 0.1)

action = input(
"""
What do you want to do?
(1) Download a song
(2) Play a song
(3) Play all songs
(4) Play a playlist
""")

if action == "1":
    #take query from user
    searchquery = input("input a query\n")
    results = search(searchquery)
    clear()
    #print every results title
    for i in range(len(results)):
        print(f"({i + 1}): {results[i]['title']}")
    #take one song and download it
    num = int(input("which one do you want to download?\n")) - 1
    downloadMP3(idToYtURL(results[num]["id"]))

elif action == "2":
    #get all files in the music folder
    songs = listdir(config.mp3_dest)
    #print all the names without the extension
    for i in range(len(songs)):
        print(f"({i + 1}): {songs[i].split('.mp3')[0]}")
    num = int(input("which one do you want to play?\n")) - 1
    #play the users chosen song as a thread
    playSong(f"{config.mp3_dest}/{songs[num]}")

elif action == "3":
    for song in listdir(config.mp3_dest):
        playSong(f"{config.mp3_dest}/{song}")

elif action == "4":
    playlistfile = open("playlists.json", )
    playlists = dict(json.load(playlistfile))
    for i in range(len(list(playlists.keys()))):
        print(f"({i + 1}) {list(playlists.keys())[i]}")
    chosen = int(input("which playlist do you wanna play"))
    playlist = playlists[list(playlists.keys())[chosen - 1]] 
    for song in playlist:
        playSong(f"{config.mp3_dest}/{song}")
