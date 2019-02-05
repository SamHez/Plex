"""
PYTHON SCRIPT THAT RANDOMLY OPENS WEBSITES TO PRANK PEOPLE THAT THERE MACHINE HAS A VIRUS OR AN ISSUE
WRITTEN BY - SAMUEL EPODOI

!!ATTENTION!!
This is just a prank program and the links open arent actually virus links

To stop the program press control + C.

"""
#Imports
import webbrowser
import time
import random

#Randomly open websites within a random time range
while True:
	sites = random.choice(['geekprank.com/static-tv-noise/', 'geekprank.com/blue-death/', 'geekprank.com/fbi-warning/', 'geekprank.com/fake-virus/'])
	visit = "https://{}".format(sites)
	webbrowser.open(visit)
	seconds = random.randrange(3, 4)
	time.sleep(seconds)



	