from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps
from pytesseract import * 
import numpy as np
import pywinauto
import time
from Arti_Ficelle import *

basic_cells = [(155,155,50),(165,124,72),(154,143,62),(175,125,78),(182,149,113)]
signs = [(89, 146, 34),(212, 85, 0),(52, 21, 0),(191, 142, 0),(253, 66, 66),(255, 248, 1),(139, 227, 53),(225, 90, 0),(78, 128, 30),(159, 117, 0)]
background = [(51,51,51)]

mouse_coordinates = {}
for i in range (7):
    for j in range (7):
        mouse_coordinates[str(i)+"."+str(j)] = (375+i*50+j*50,475+i*25-j*25)

for i in range (7):
    mouse_coordinates["spells."+str(i)] = (500+(i*63),820)

path_to_tesseract = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

def notsamepixel(test_pixel,reference_pixels):
    for i in range (len(reference_pixels)):
        if((abs(reference_pixels[i][0]-test_pixel[0]) <= 10) and (abs(reference_pixels[i][1]-test_pixel[1]) <= 10) and (abs(reference_pixels[i][2]-test_pixel[2]) <= 10)):
            return False
    return True

def clean(image,x): 
    for i in range(-3,12):
        for j in range(image.height):
            if( i in [5,6] and j in [image.height-4,image.height-5]):
                image.putpixel((x+i,j),(255,255,255))
            else:
                image.putpixel((x+i,j),(42,42,42))

#for i in range (inverted_image.width):
    #print(str(i) + "  "+ str(inverted_image.getpixel((i,9))))

def add_character(char_list,ally):
    fond = Image.open(r"fond.png")
    x = 0
    if(ally):
        pass
    else:
        image = ImageGrab.grab(bbox=(950,68,1230,86)) 

        while(notsamepixel(image.getpixel((x,0))[0:3],background) and (x < image.width)):
            for j in range (image.height):
                image.putpixel((x,j),(42,42,42))
            x+=1

        for i in range(x,image.width):
                print(image.getpixel((i,9)))
                if(not notsamepixel(image.getpixel((i,9))[0:3],signs)):
                    clean(image,i)

        x=1
        while(notsamepixel(image.getpixel((-x,0))[0:3],background) and (x < image.width)):
            for j in range (image.height):
                image.putpixel((-x,j),(42,42,42))
            x+=1

        for i in range(image.width):
            for j in range(image.height):
                fond.putpixel((50+i,90+j),image.getpixel((i,j)))
        
        #image = fond.resize((fond.width*4,fond.height*4),resample=Image.BOX)
        image.show()
        time.sleep(1)
        text = pytesseract.image_to_string(image)
        print(text[:-1])

def reco_board(chars,hand):
    image = ImageGrab.grab(bbox=(0,0,1343,882))
    for i in range (7):
          for j in range (7):
            if(notsamepixel(image.getpixel(mouse_coordinates[str(i)+"."+str(j)]),basic_cells)):
                pywinauto.mouse.click(button="left",coords=mouse_coordinates[str(i)+"."+str(j)])
                pywinauto.mouse.press(button="left",coords=mouse_coordinates[str(i)+"."+str(j)])
                time.sleep(0.7)
                snapshot = ImageGrab.grab(bbox=(0,0,1343,80))
                goodpixel=snapshot.getpixel((120,66))
                badpixel=snapshot.getpixel((1210,66))
                if(badpixel[0]==255 and badpixel[1]==255 and badpixel[2] == 255):
                    print("mezzant")
                    add_character(chars,False)
                elif(goodpixel[0]==255 and goodpixel[1]==255 and goodpixel[2] == 255):
                    print("zentil")
                pywinauto.mouse.release(button="left",coords=mouse_coordinates[str(i)+"."+str(j)])

    for i in range (0):
        for cle,valeur in spells.items() :
            for j in range (len(valeur[1])):
                if (not notsamepixel(image.getpixel(mouse_coordinates["spells."+str(i)]),valeur[1])):
                    print(cle)
                    hand.append(spells[cle])
                    break

        print(i)
        print(image.getpixel(mouse_coordinates["spells."+str(i)]))

    image.putpixel((941,820),(255,0,0))
    image.putpixel((1210,66),(0,255,0))
    image.putpixel((120,66),(0,255,0))

    image.show()

reco_board(char_list,spellist)

#image = Image.open(r"fond.png")
#image = image.resize((image.width*4,image.height*4),resample=Image.BOX)
#image.show()
#text = pytesseract.image_to_string(image)
#print(text[:-1])
