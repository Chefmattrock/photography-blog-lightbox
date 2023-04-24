#!/usr/bin/env python3
import glob
import os


photos = glob.glob('*.jpg')
name = 'folks'
selection = 2
directory = 'alvarez-and-marsal'

print ('\n----------------------\n')
print ('<h1>Thanks ' + name + '!</h1>')
print ('<p>&nbsp;</p>')
print ('<h3>Here are your proofs:</h3>')
print ('<p>Let me know which ' + str(selection) + " photos you want to pick. Choose the expression you like the best. I'll adjust things like brightness, color and shadows in the next step.</p>")
print ('<p>&nbsp;</p>')

photos.sort()	
for i in photos:
#!for i in reversed(photos):

	print ('<p><img src=\"//www.matthewsteinphotography.com/hubfs/' + directory + '/' + i + '\" width=\"600\">')
	print ('</p>')
	print ('<p>' + i + '</p>')
	print ('<hr>')

print ('\n----------------------\n')

