#######################################################
## Cold Imager                                       ##
## Program that combines images from Lab C cold box. ##
## Includes serial numbers based on input.           ##
#######################################################
from PIL import Image, ImageDraw, ImageFont
import sys

# User passes Outer Tracker plank serial numbers #
id1 = sys.argv[1]
id2 = sys.argv[2]

# Program seeks out the images #
ext = ".png"
print("Loading Files...")
img1 = Image.open(id1+ext)
img2 = Image.open(id2+ext)

###################################################################################################

# Define function for stamping images #
def StampImage(image,text):
    stamp = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 24)

    # Positioning #
    pos = (10,10)
    color = "white"
    outline = "black"

    # Add an outline (for readability) #
    stamp.text((pos[0]-1, pos[1]-1), text, font=font, fill=outline)
    stamp.text((pos[0]+1, pos[1]-1), text, font=font, fill=outline)
    stamp.text((pos[0]-1, pos[1]+1), text, font=font, fill=outline)
    stamp.text((pos[0]+1, pos[1]+1), text, font=font, fill=outline)

    # Now render the text
    print("Stamping Image...")
    stamp.text(pos, text, font=font, fill=color)

    return image

# Define Function to combine images #
def CombineImages(img1,img2):
    width = max(img1.width, img2.width)
    result = Image.new('RGB',(width, img1.height+img2.height))
    print("Combining Images...")
    result.paste(img1,(0,0))
    result.paste(img2,(0,img1.height))
    return result

###################################################################################################

# Start by stamping the images with the serial #
Img1_Stamp = StampImage(img1.copy(),id1)
Img2_Stamp = StampImage(img2.copy(),id2)
combined_picture = CombineImages(Img1_Stamp,Img2_Stamp).save("Panel_" + id1 + "_" + id2 + ext)
print("Images combined!")



