#-*- cording: utf-8 -*-
import os
import sys
import subprocess


def start():
    pathToMP3 = "mp3/*.MP3"
    print("===================="+str(os.getpid()))
    statusCode = subprocess.call("mpg321 --loop 0 --shuffle -K " + pathToMP3, shell=True)

start()
