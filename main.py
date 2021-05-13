import pytube
from pytube import YouTube
from pytube import Playlist
import pandas as pd
#Specify the path where the file will be saved
SAVE_PATH = "E:/"

'''
def single_dl():
    for downloading single videos and saving them in the SAVE_PATH
    returns title of the video

'''

def single_dl(link):


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

def txtdownload():
    #Make sure each new line has a new link in the .txt file
    txtpath=input("Enter the full path of the txtfile(D:\\myfiles\welcome.txt) in this foemat :")
    f = open(txtpath, "r")
    for x in f:
        v = single_dl(x)
        if (v != 0):
            print("Downloaded the video in--------------- " + SAVE_PATH + v)

def csvdownload():
    #Edit the file path section
    df=pd.read_csv('AdultData - Sheet1.csv')
    list_link=df['Link']
    for l in list_link:
        v = single_dl(str(l))
        if (v != 0):
            print("Downloaded the video in--------------- " + SAVE_PATH + v)



if __name__ == '__main__':
    choice=int(input("Enter 1 for downloading playlist \n2 for downloading single video \n3 for downloading through .txt file\n4 for downloading through csv\n-------------------"))
    if(choice == 1):
        v=playlistDl();
        if(v!=0):
            print("Downloaded the playlist in --------------- "+SAVE_PATH)
    elif(choice==2):
        link = input("Enter the video link :")
        v=single_dl(link)
        if(v!=0):
            print("Downloaded the video in--------------- "+SAVE_PATH+v)
    elif(choice == 3):
        txtdownload()
    elif(choice == 4):
        csvdownload()



