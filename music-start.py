#-*- cording: utf-8 -*-
import os
import sys
import subprocess

def start():
    pathToMP3 = "mp3/*.MP3"
    p = subprocess.call("mpg321 --loop 0 --shuffle -K " + pathToMP3, shell=True).getpid()
    f = open('pid.txt', 'w')
    f.write(str(p))
    f.close()

start()
