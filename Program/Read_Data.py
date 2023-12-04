from PIL import Image
from PIL import ImageGrab
from pytesseract import * 
import numpy as np
import pywinauto
import time
from Arti_Ficelle import *

basic_cells = [(155,155,50),(165,124,72),(154,143,62),(175,125,78),(182,149,113)]

path_to_tesseract = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

def notsamepixel(test_pixel,reference_pixels):
    for i in range (len(reference_pixels)):
        if((abs(reference_pixels[i][0]-test_pixel[0]) <= 10) and (abs(reference_pixels[i][1]-test_pixel[1]) <= 10) and (abs(reference_pixels[i][2]-test_pixel[2]) <= 10)):
            return False
    return True

def reco_board():
    image = ImageGrab.grab(bbox=(0,0,1343,882))
    for i in range (7):
          for j in range (7):
            if(notsamepixel(image.getpixel((375+i*50+j*50,475+i*25-j*25)),basic_cells)):
                pywinauto.mouse.click(button="left",coords=(375+i*50+j*50,475+i*25-j*25))
                pywinauto.mouse.press(button="left",coords=(375+i*50+j*50,475+i*25-j*25))
                time.sleep(0.7)
                snapshot = ImageGrab.grab(bbox=(0,0,1343,80))
                goodpixel=snapshot.getpixel((120,66))
                badpixel=snapshot.getpixel((1210,66))
                if(badpixel[0]==255 and badpixel[1]==255 and badpixel[2] == 255):
                    print("mezzant")
                    data = ImageGrab.grab(bbox=(1050,68,1230,86))
                    data.show()
                elif(goodpixel[0]==255 and goodpixel[1]==255 and goodpixel[2] == 255):
                    print("zentil")
                pywinauto.mouse.release(button="left",coords=(375+i*50+j*50,475+i*25-j*25))
                    
            image.putpixel((375+i*50+j*50,475+i*25-j*25),(0,255,0))

    for i in range (0):
        for cle,valeur in spells.items() :
            for j in range (len(valeur[1])):
                if (not notsamepixel(image.getpixel((500+(i*63),820)),valeur[1])):
                    print(cle)
                    spellist.append(spells[cle])
                    break

        print(i)
        print(image.getpixel((500+(i*63),820)))

    image.putpixel((941,820),(255,0,0))
    image.putpixel((1210,66),(0,255,0))
    image.putpixel((120,66),(0,255,0))

    image.show()

reco_board()

#text = pytesseract.image_to_string(inverted_image)

#print(text[:-1])

