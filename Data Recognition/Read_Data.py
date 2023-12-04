from PIL import Image
from PIL import ImageGrab
from pytesseract import * 
import numpy as np
import pywinauto
import time

basic_cells = [(155,155,50),(165,124,72),(154,143,62),(175,125,78),(182,149,113)]

path_to_tesseract = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

def samepixel(r,g,b):
    for i in range (len(basic_cells)):
        if((abs(basic_cells[i][0]-r) <= 10) and (abs(basic_cells[i][1]-g) <= 10) and (abs(basic_cells[i][2]-b) <= 10)):
            return False
    return True

def reco_board():
    image = ImageGrab.grab(bbox=(0,0,1343,882))
    for i in range (7):
          for j in range (7):
            pixel = image.getpixel((375+i*50+j*50,475+i*25-j*25))
            if(samepixel(pixel[0],pixel[1],pixel[2])):
                pywinauto.mouse.click(button="left",coords=(375+i*50+j*50,475+i*25-j*25))
                pywinauto.mouse.press(button="left",coords=(375+i*50+j*50,475+i*25-j*25))
                time.sleep(0.7)
                snapshot = ImageGrab.grab(bbox=(0,0,1343,80))
                goodpixel=snapshot.getpixel((120,66))
                badpixel=snapshot.getpixel((1210,66))
                if(badpixel[0]==255 and badpixel[1]==255 and badpixel[2] == 255):
                    print("mezzant")
                elif(goodpixel[0]==255 and goodpixel[1]==255 and goodpixel[2] == 255):
                    print("zentil")
                pywinauto.mouse.release(button="left",coords=(375+i*50+j*50,475+i*25-j*25))
                    
            image.putpixel((375+i*50+j*50,475+i*25-j*25),(0,255,0))

    for i in range (7):
        print(image.getpixel((500+(i*63),820)))
        image.putpixel((500+(i*63),820),(255,0,0))

    image.putpixel((941,820),(255,0,0))
    image.putpixel((1210,66),(0,255,0))
    image.putpixel((120,66),(0,255,0))

    image.show()

reco_board()

#text = pytesseract.image_to_string(inverted_image)

#print(text[:-1])

