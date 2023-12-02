from PIL import Image
from PIL import ImageGrab
from pytesseract import * 
import numpy as np

snapshot = ImageGrab.grab(bbox=(0,0,1343,881))
path_to_tesseract = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

im_rgb = snapshot.convert('RGB')

def reco_board():
    for i in range (-6,7):
        if(i%2==0):
            for j in range (7-abs(i)):
                snapshot.putpixel((370+(i+6)*50,480-int(50*(6-abs(i))/2)+50*j),(0,255,0))
        else:   
            for j in range (7-abs(i)):
                snapshot.putpixel((370+(i+6)*50,480-int(50*(6-abs(i))/2)+50*j),(255,255,0))

    for i in range (7):
        snapshot.putpixel((500+(i*63),820),(255,0,0))

    snapshot.putpixel((941,820),(255,0,0))

reco_board()
print(im_rgb)

snapshot.show()

#text = pytesseract.image_to_string(inverted_image)

#print(text[:-1])

