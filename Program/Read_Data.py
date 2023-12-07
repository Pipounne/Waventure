from PIL import Image
from PIL import ImageGrab
import pywinauto
import time
from Arti_Ficelle import *

basic_cells = [(155,155,50),(165,124,72),(154,143,62),(175,125,78),(182,149,113)]
signs = [(89, 146, 34),(52, 21, 0),(191, 142, 0),(253, 66, 66),(255, 248, 1),(139, 227, 53),(225, 90, 0),(78, 128, 30),(4, 4, 4),(160, 254, 252)]
crit_sign = [(254, 105, 1),(188, 75, 0),(114, 45, 0),(255, 118, 0)]
background = [(51,51,51)]
numbers = [(i,i,i) for i in range (130,251,10)]
numbers_ally = numbers + [(157, 225, 91),(84, 108, 60),(88, 115, 62),(151, 215, 89),(67, 81, 52),(142, 201, 85),(140, 197, 84),(108, 147, 70),(124, 172, 77),(156, 224, 91)]
mouse_coordinates = {}
for i in range (7):
    for j in range (7):
        mouse_coordinates[str(i)+"."+str(j)] = (375+i*50+j*50,475+i*25-j*25)

for i in range (7):
    mouse_coordinates["spells."+str(i)] = (500+(i*63),820)

mouse_coordinates["end_turn"] = (975,850)

def notsamepixel(test_pixel,reference_pixels):
    for i in range (len(reference_pixels)):
        if((abs(reference_pixels[i][0]-test_pixel[0]) <= 10) and (abs(reference_pixels[i][1]-test_pixel[1]) <= 10) and (abs(reference_pixels[i][2]-test_pixel[2]) <= 10)):
            return False
    return True

def clean(image,x): 
    for i in range(-3,13):
        for j in range(image.height):
            image.putpixel((x+i,j),(42,42,42))

def cleanup(image,x):
    for i in range(x-3,image.width):
        for j in range(image.height):
            image.putpixel((i,j),(42,42,42))

def number_reco(image,x):

    #for  i in range (3,15) :
        #for j in range(x-4,x+6):
            #print(image.getpixel((j,i))[0],end=' ')
        #print("")

    #1
    if(not notsamepixel(image.getpixel((x,9)),numbers) and not notsamepixel(image.getpixel((x,13)),numbers) and not notsamepixel(image.getpixel((x,5)),numbers) and notsamepixel(image.getpixel((x+2,9)),numbers) and  notsamepixel(image.getpixel((x+2,13)),numbers) and  notsamepixel(image.getpixel((x+2,5)),numbers) and notsamepixel(image.getpixel((x-2,9)),numbers) and  notsamepixel(image.getpixel((x-2,13)),numbers)):
        #print("C'est un 1")
        return 1
    #8
    elif(not notsamepixel(image.getpixel((x,4)),numbers) and not notsamepixel(image.getpixel((x-1,6)),numbers)and not notsamepixel(image.getpixel((x+3,6)),numbers) and not notsamepixel(image.getpixel((x,9)),numbers) and not notsamepixel(image.getpixel((x-1,12)),numbers) and not notsamepixel(image.getpixel((x+3,12)),numbers) and not notsamepixel(image.getpixel((x,13)),numbers)):
        #print("C'est un 8")
        return 8
    
    #2
    elif(not notsamepixel(image.getpixel((x-2,4)),numbers) and notsamepixel(image.getpixel((x-4,6)),numbers)and not notsamepixel(image.getpixel((x,6)),numbers) and not notsamepixel(image.getpixel((x-2,9)),numbers) and not notsamepixel(image.getpixel((x-4,12)),numbers) and notsamepixel(image.getpixel((x,12)),numbers) and not notsamepixel(image.getpixel((x-2,13)),numbers)):
        #print("C'est un 2")
        return 5
    
    #3
    elif(not notsamepixel(image.getpixel((x-2,4)),numbers) and notsamepixel(image.getpixel((x-4,6)),numbers)and not notsamepixel(image.getpixel((x,6)),numbers) and not notsamepixel(image.getpixel((x-2,9)),numbers) and not notsamepixel(image.getpixel((x-4,12)),numbers) and notsamepixel(image.getpixel((x,12)),numbers) and not notsamepixel(image.getpixel((x-2,13)),numbers)):
        #print("C'est un 3")
        return 3

    #0
    elif(not notsamepixel(image.getpixel((x+3,4)),numbers) and not notsamepixel(image.getpixel((x,6)),numbers)and not notsamepixel(image.getpixel((x+5,6)),numbers) and notsamepixel(image.getpixel((x+3,9)),numbers) and not notsamepixel(image.getpixel((x,12)),numbers) and not notsamepixel(image.getpixel((x+5,12)),numbers) and not notsamepixel(image.getpixel((x+3,13)),numbers)):
        #print("C'est un 0")
        return 0

    #5
    elif(not notsamepixel(image.getpixel((x+3,4)),numbers) and not notsamepixel(image.getpixel((x,6)),numbers) and notsamepixel(image.getpixel((x+4,6)),numbers) and not notsamepixel(image.getpixel((x+3,9)),numbers) and notsamepixel(image.getpixel((x-1,12)),numbers) and not notsamepixel(image.getpixel((x+3,13)),numbers)):
        #print("C'est un 5")
        return 5

    #6
    elif(not notsamepixel(image.getpixel((x+3,4)),numbers) and not notsamepixel(image.getpixel((x,6)),numbers)and notsamepixel(image.getpixel((x+4,7)),numbers) and not notsamepixel(image.getpixel((x+3,9)),numbers) and not notsamepixel(image.getpixel((x,11)),numbers) and not notsamepixel(image.getpixel((x+4,12)),numbers) and not notsamepixel(image.getpixel((x+3,13)),numbers)):
        #print("C'est un 6")
        return 6

    #9
    elif(not notsamepixel(image.getpixel((x+3,4)),numbers) and notsamepixel(image.getpixel((x,6)),numbers)and not notsamepixel(image.getpixel((x+4,6)),numbers) and not notsamepixel(image.getpixel((x+3,9)),numbers) and not notsamepixel(image.getpixel((x,11)),numbers) and not notsamepixel(image.getpixel((x+4,12)),numbers) and not notsamepixel(image.getpixel((x+3,13)),numbers)):
        #print("C'est un 9")
        return 9

    #7
    elif(not notsamepixel(image.getpixel((x,4)),numbers) and notsamepixel(image.getpixel((x-2,6)),numbers)and not notsamepixel(image.getpixel((x+2,6)),numbers) and not notsamepixel(image.getpixel((x,9)),numbers) and notsamepixel(image.getpixel((x-2,12)),numbers) and not notsamepixel(image.getpixel((x+2,12)),numbers) and not notsamepixel(image.getpixel((x,13)),numbers)):
        #print("C'est un 7")
        return 7

    #4
    elif(notsamepixel(image.getpixel((x+5,6)),numbers) and not notsamepixel(image.getpixel((x+3,9)),numbers) and not notsamepixel(image.getpixel((x,12)),numbers) ,numbers):
        #print("C'est un 4")
        return 4
    
    else:
        return -1
    
def add_character(ally):
    fond = Image.open(r"fond.png")
    x = 0
    stats = []
    if(ally):
        image = ImageGrab.grab(bbox=(120,68,400,86)) 

        while(notsamepixel(image.getpixel((x,0))[0:3],background) and (x < image.width)):
            for j in range (image.height):
                image.putpixel((x,j),(42,42,42))
            x+=1
        i=x
        while i < image.width :
                if(not notsamepixel(image.getpixel((i,9))[0:3],crit_sign)):
                    cleanup(image,i)
                if(not notsamepixel(image.getpixel((i,9))[0:3],signs)):
                    clean(image,i)
                    #image.show()
                    stats.append("")
                    print("")
                if(not notsamepixel(image.getpixel((i,9))[0:3],numbers_ally)):
                    number = number_reco(image,i)
                    image.putpixel((i,17),(0,255,0))
                    print(number)
                    if(number == 1):
                        i += 1
                    elif(number == 2 ):
                        i+=2
                    elif(number == 4 or number == 0):
                        i+=5
                    elif(number > -1):
                        i += 4
                    stats[-1]+=str(number)
                    #for j in range(image.height):
                        #print(image.getpixel((i,j)))
                    #print(i)
                image.putpixel((i,9),(255,0,0))
                i+=1
                    
        x=1
        while(notsamepixel(image.getpixel((-x,0))[0:3],background) and (x < image.width)):
            for j in range (image.height):
                image.putpixel((-x,j),(42,42,42))
            x+=1

        for i in range(image.width):
            for j in range(image.height):
                fond.putpixel((50+i,90+j),image.getpixel((i,j)))
        
        return stats

    else:
        image = ImageGrab.grab(bbox=(950,68,1230,86)) 
        
        while(notsamepixel(image.getpixel((x,0))[0:3],background) and (x < image.width)):
            for j in range (image.height):
                image.putpixel((x,j),(42,42,42))
            x+=1
        i=x
        while i < image.width :
                if(not notsamepixel(image.getpixel((i,9))[0:3],crit_sign)):
                    cleanup(image,i)
                if(not notsamepixel(image.getpixel((i,9))[0:3],signs)):
                    clean(image,i)
                    stats.append("")
                if(not notsamepixel(image.getpixel((i,9))[0:3],numbers)):
                    number = number_reco(image,i)
                    image.putpixel((i,17),(0,255,0))
                    print(number)
                    print("")
                    if(number == 1):
                        i += 1
                    elif(number == 2 ):
                        i+=2
                    elif(number == 4 or number == 0):
                        i+=5
                    elif(number > -1):
                        i += 4
                    stats[-1]+=str(number)
                    #for j in range(image.height):
                        #print(image.getpixel((i,j)))
                    #print(i)
                image.putpixel((i,9),(255,0,0))
                i+=1
                    
        x=1
        while(notsamepixel(image.getpixel((-x,0))[0:3],background) and (x < image.width)):
            for j in range (image.height):
                image.putpixel((-x,j),(42,42,42))
            x+=1

        for i in range(image.width):
            for j in range(image.height):
                fond.putpixel((50+i,90+j),image.getpixel((i,j)))
        
        time.sleep(5)
        return stats

def reco_board(chars,hand):
    cpt_foes = 1
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
                    stats = add_character(False)
                    if(len(stats)==3):
                        chars.append(character("Foe"+str(cpt_foes),str(cpt_foes),False,int(stats[0]),int(stats[0]),int(stats[1]),int(stats[2]),int(stats[2]),3,0,(i,j)))
                    else:
                        chars.append(character("Foe"+str(cpt_foes),str(cpt_foes),False,int(stats[0]),int(stats[0]),0,int(stats[1]),int(stats[1]),3,0,(i,j)))  
                    cpt_foes += 1
                elif(goodpixel[0]==255 and goodpixel[1]==255 and goodpixel[2] == 255):
                    print("zentil")
                    stats = add_character(True)
                    if(len(stats)==3):
                        stats[2] =  int(stats[2])-  round(0.6 * float(stats[1]))
                        chars[0]=(character("Arti_Ficelle","0",True,int(stats[0]),int(stats[0]),int(stats[1]),int(stats[2]),int(stats[2]),3,6,(i,j),{"passif_Justelame":True}))
                    else:
                        chars[0]=(character("Arti_Ficelle","0",True,int(stats[0]),int(stats[0]),0,int(stats[1]),int(stats[1]),3,6,(i,j),{"passif_Justelame":True})) 
                pywinauto.mouse.release(button="left",coords=mouse_coordinates[str(i)+"."+str(j)])

    for i in range (7):
        for cle,valeur in spells.items() :
            for j in range (len(valeur[1])):
                if (not notsamepixel(image.getpixel(mouse_coordinates["spells."+str(i)]),valeur[1])):
                    print(cle)
                    hand.append(spells[cle][0])
                    break
        #print(image.getpixel(mouse_coordinates["spells."+str(i)]))

    #image.putpixel((941,820),(255,0,0))
    #image.putpixel((1210,66),(0,255,0))
    #image.putpixel((120,66),(0,255,0))

#image = Image.open(r"fond.png")
#image = image.resize((image.width*4,image.height*4),resample=Image.BOX)
#image.show()
#text = pytesseract.image_to_string(image)
#print(text[:-1])

#reco_board([],[])