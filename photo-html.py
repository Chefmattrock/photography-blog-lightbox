#!/usr/bin/env python3
import glob
import os, sys

#Next step http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html

photos = glob.glob('*res.jpg')
photos.sort()
name = 'folks'
selection = 3
directory = 'alvarez-and-marsal'

def header(name):

	print ('\n----------------------\n')
	print ('<h1>Thanks, ' + name + '!</h1>')
	print ('<p>&nbsp;</p>')
	print ('<h3>Here are your photos:</h3>')
	print ('<p>Click to download the image file.</p>')
	print ('<p>&nbsp;</p>')


header(name)


for i in reversed(photos):
#! 4for i in photos:

	print ('<p><a href=\"http://www.matthewsteinphotography.com/hubfs/' + directory + '/' + i + '\" download=\"\">')
	print ('<img src=\"http://www.matthewsteinphotography.com/hubfs/' + directory + '/' + i + '\" width=\"600\">')
	print ('</a></p>')
	print ('<p>' + i + '</p>')
	print ('<hr>')

print ('\n----------------------\n')
