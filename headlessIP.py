#!/usr/bin/env python
import subprocess
import socket
import os
import time

#Functions

def say(sentence):
    cmd = 'echo "{0}" | festival --tts'.format(sentence).rstrip("/n")
    os.system(cmd) # UPGRADE: os.system is depricated, need to fix to use subprocess

#Install Festival
print("Installing Festival")
festival_install_cmd = "sudo apt-get --assume-yes install festival"
os.system(festival_install_cmd)


# NEED TO ADD LOGGING print(install_Festival.stdout)
print("Festival has been successfully installed")

# Get networking information
while True:
    host = socket.gethostname()
    ipnum = subprocess.check_output(["hostname", "-I"]).decode()
    say("The I. P. is " + ipnum)
    say("The host is " + host)
    time.sleep(1)
