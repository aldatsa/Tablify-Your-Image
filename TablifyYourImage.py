from PIL import Image
import os

# Path to the image
path = 'iametza.jpg'

# Get the name of the image from the path -> we are going to use it as the name of the new html file
name = os.path.splitext(path)[0]

# Open the image
im = Image.open(path)

# Convert to RGB
rgb_im = im.convert('RGB')

# Get the width and height of the image (in pixels)
width, height = im.size

# Create the html file
f = open(name + '.html', 'w')

# Create the table
f.write('<table cellspacing="0" cellpadding="0" border="0" style="margin-left: auto; margin-right: auto; font-size:0px;">\n')

# Create the body of the table
f.write('<tbody>\n')

# Create a <td> for each pixel of the image with the corresponding color
for y in range(0, height):
    for x in range(0, width):
        # If it is the first column (0st), create an tr tag
        if x == 0:
            f.write('<tr>')
        
        # Get the color of the corresponding pixel
        r, g, b = rgb_im.getpixel((x, y))
        f.write('<td width="1" height="1" bgcolor="' + '#%02x%02x%02x' % (r, g, b)  + '" colspan="1">&nbsp;</td>')

        # If it is the last column, close the tr tag
        if x == width - 1:
            f.write('</tr>')

        # Add a new line
        f.write('\n')

# Close the body of the table and the table itself
f.write('</tbody></table>')

# Close the html file
f.close()
