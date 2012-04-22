#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib2 import urlopen, HTTPError
from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve
from PIL import Image
from sys import argv

def mainpage(sorting):
	url = urlopen('http://9gag.com/%s' %sorting).read()
	soup = BeautifulSoup(url)
	content = soup('div', {'class':'img-wrap'})
	contentinfo = soup('div', {'class':'imsticky-items'})
	for i in range(0, len(content)):
		filename = "%s.jpg"%content[i].img['alt']
		print filename
		try:	
			urlretrieve(content[i].img['src'], filename)
			wmarkcrop(filename)
		except HTTPError, e:
			print "Error while downloading image", e

def wmarkcrop(filename):
	# size is width/height
	img = Image.open(filename)
	o_width, o_height = img.size

	#crop position/size

	left = 0
	top = 0
	width = o_width
	height = o_height - 30
	box = (left, top, left+width, top+height)
	area = img.crop(box)

	area.save(filename, 'jpeg')	
	print 'Cropped'		

if __name__ == "__main__":
	try:
		mainpage(argv[1])
	except IndexError:
		print "Example of usage:\npython 9gag.py hot\nor\npython 9gag.py trending"


