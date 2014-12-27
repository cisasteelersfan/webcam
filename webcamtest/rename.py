#!/usr/bin/env python3

import os
import shutil
import time
import sys

webcam = os.path.expanduser('~')+'/webcam/'
filetime = time.strftime("%m_%d_%y__%H-%M-%S/")
newpath = webcam+filetime
numPics = 0

def main():
    if len(sys.argv) >= 2:#If an argument is passed:
        if sys.argv[1] == '-h':
            print("Usage: rename [folder][bitrate][fps]")
            return 
        createVid()
    else: #No argument
        renamePics()
        sys.argv.append('')
        sys.argv[1] = newpath
        createVid()

def createVid():
    if len(sys.argv) >=3: #If bitrate is passed:
        bitrate = sys.argv[2]
    else:
        bitrate = input("Enter bitrate (default 1000k): ")
        if bitrate=='': bitrate = '1000k'
    if len(sys.argv) >=4: #If framerate passed:
        fps = sys.argv[3]
    else:
        while True:
            fps = input("Enter fps (default 15): ")
            if fps=='': fps='15'
            time = int(len(os.listdir(sys.argv[1])))/int(fps)
            var = input("Video will be "+str(time)+"seconds long. Enter new \
fps? (enter to continue): ")
            if var == '': break
            else:
                fps = var
    argument = "avconv -r "+fps+" -f image2 -i "+sys.argv[1]+\
              "%07d.jpg -b "+bitrate+" "+webcam+"video"+sys.argv[1][-19:-1]\
              +".avi"
    os.system(argument)
        
def renamePics():
    counter = 0
    files = [f for f in sorted(os.listdir(webcam+'temp'))]
    numPics = len(files)
    os.mkdir(newpath)
    print("Newpath is", newpath)
    for file in files:
        #print("oldname =",file)
        number = (format(counter, "07d"))+str('.jpg')
        #print("newname =", number)
        #print("")
        #print(webcam+'temp/'+file, newpath+number)
        os.rename(webcam+'temp/'+file, newpath+number)
        counter += 1
    #print(len(files))

main()
