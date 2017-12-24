#-*- cording: utf-8 -*-
import os
import sys
import subprocess

def stop():
    subprocess.call("ps aux | grep mpg321 | grep -v grep | awk '{ print \"kill -9\", $2 }' | sh", shell=True)

stop()
