
import pafy
import os
from pydub import AudioSegment


def downloadSound(videourl):

    url = str(videourl)
    video = pafy.new(url) 
    
    bestaudio = video.getbestaudio() 
    print(video.title, video.author, video.length)
    bestaudio.download() 

def linklister(linklist):

    f = open('links.txt','r')

    for line in f:
        linklist.append(line.strip())

    f.close()    

def converter():
    dirlist = os.listdir()

    songlist = []

    for i in dirlist:
        if ".webm" in i:
            songlist.append(i)

    for i in songlist:

        sound = AudioSegment.from_file(i)

        imp3 = i.replace(".webm", ".mp3") 

        sound.export(imp3, format="mp3", bitrate="192k")

        print (i, "DONE")

def main():
    ytlinks = []

    linklister(ytlinks)

    for i in ytlinks:
        downloadSound(i)

    print ("downlad complete, proceeding to conversion")

    converter()




try:
    main()

except Exception as e:
    print (e)
    print ("OPPS")

else:
    pass    
        

