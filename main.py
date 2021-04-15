import pytube
from pytube import YouTube
from pytube import Playlist
#Specify the path where the file will be saved
SAVE_PATH = "E:/"

'''
def single_dl():
    for downloading single videos and saving them in the SAVE_PATH
    returns title of the video

'''

def single_dl():

    link =input("Enter the video link :")
    try:
        yt=YouTube(link)
    except:
        print("Video might be unavailable")
        return 0
    else:
        print(f'Downloading video: {yt.title}')
        yt.streams.first().download(SAVE_PATH)
        return yt.title

'''
def playlistDl()
    for downloading entire playlist and saving them in the SAVE_PATH
    :returns title of the playlist

'''
def playlistDl():
    link=input("Enter the playlist link:")
    try:
        p= Playlist(link)
    except:
        print("Playlist might be unavailable")
        return 0

    else:
        print(f'Downloading: {p.title}')
        for video in p.videos:
            video.streams.first().download(SAVE_PATH)
            print("Downloaded video :",video.title)
        return p.title




if __name__ == '__main__':
    choice=int(input("Enter 1 for downloading playlist 2 for downloading single video: "))
    if(choice == 1):
        v=playlistDl();
        if(v!=0):
            print("Downloaded the playlist in --------------- "+SAVE_PATH)
    elif(choice==2):
        v=single_dl()
        if(v!=0):
            print("Downloaded the video in--------------- "+SAVE_PATH+v)


