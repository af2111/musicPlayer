from youtube_search import YoutubeSearch
from constants import ydl
from os import listdir, system, name
from playsound import playsound
import config
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

action = input(
"""
What do you want to do?
(1) Download a song
(2) Play a song
(3) Play all songs
""")
if action == "1":
    searchquery = input("input a query\n")
    results = search(searchquery)
    clear()
    for i in range(len(results)):
        print(f"({i + 1}): {results[i]['title']}")
    num = int(input("which one do you want to download?\n")) - 1
    downloadMP3(idToYtURL(results[num]["id"]))
elif action == "2":
    songs = listdir(config.mp3_dest)
    for i in range(len(songs)):
        print(f"({i + 1}): {songs[i]}")
    num = int(input("which one do you want to play?\n")) - 1
    playsound(f"{config.mp3_dest}/{songs[num]}")
elif action == "3":
    for song in listdir(config.mp3_dest):
        playsound(f"{config.mp3_dest}/{song}")