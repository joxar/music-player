#-*- cording: utf-8 -*-
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('setting.ini')
sec = 'develop'

def start():
    pathToMP3 = config.get(sec, 'inputDir') + "/*.MP3"
    p = subprocess.call("mpg321 --loop 0 --shuffle -K " + pathToMP3, shell=True).getpid()

start()
