import config,youtube_dl

class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_options = {
    "outtmpl": f"{config.mp3_dest}/%(title)s.%(ext)s",
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    "logger": Logger(),
    "progress_hooks": [my_hook]

}
ydl = youtube_dl.YoutubeDL(ydl_options)