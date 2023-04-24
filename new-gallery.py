#!/usr/bin/env python3	
import glob
import sys

# Get the input flags from the command line
name = ''
directory = ''
selection = 0

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-n':
            name = sys.argv[i+1]
        elif sys.argv[i] == '-d':
            directory = sys.argv[i+1]
        elif sys.argv[i] == '-s':
            selection = int(sys.argv[i+1])

# Get the list of photo file names in the current directory
photos = glob.glob('*.jpg')


# Print line for easy scaning
print ('\n----------------------\n')

# Print the HTML for the top of the page
print('<h1>Thanks ' + name + '!</h1>')
print('<p>&nbsp;</p>')
print('<h3>Here are your proofs:</h3>')
print('<p>Let me know which ' + str(selection) + " photos you want to pick. Choose the expression you like the best. I'll adjust things like brightness, color and shadows in the next step.</p>")
print('<p>&nbsp;</p>')

# Print the HTML for the gallery
print('<div class="gallery">')
if len(photos) > 0:
    photos.sort()
    print('<div class="gallery_row">')
    for i in range(len(photos)):
        print('<div class="gallery_column">')
        print('<img class="gallery_img" src="//www.matthewsteinphotography.com/hubfs/' + directory + '/' + photos[i] + '" onclick="openLightbox(\'' + photos[i] + '\')">')
        print('</div>')
        if (i+1) % 2 == 0:
            print('</div><div class="gallery_row">')
    print('</div>')
else:
    print('<p>No photos found.</p>')
print('</div>')

# Print the HTML for the lightbox
print('<div class="gallery_lightbox" onclick="closeLightbox()">')
print('<img id="lightbox-img">')
print('</div>')

# Print the JavaScript for the lightbox
print('<script>')
print('function openLightbox(photo) {')
print('  document.getElementById("lightbox-img").src = "//www.matthewsteinphotography.com/hubfs/' + directory + '/" + photo;')
print('  document.querySelector(".gallery_lightbox").style.display = "flex";')
print('}')
print('function closeLightbox() {')
print('  document.querySelector(".gallery_lightbox").style.display = "none";')
print('}')
print('document.addEventListener("keydown", function(event) {')
print('  if (event.key === "Escape") {')
print('    closeLightbox();')
print('  }')
print('});')
print('</script>')
print ('\n----------------------\n')
# This code defines the openLightbox and closeLightbox functions and adds an event listener to the document object to listen for the Escape key to close the lightbox. The openLightbox function sets the src attribute of the img element with id="lightbox-img" to the URL of the clicked photo and sets the display style of the div element with class gallery_lightbox to "flex" to show the lightbox. The closeLightbox function sets the display style of the div element with class gallery_lightbox to "none" to hide the lightbox.
