from PIL import Image
from PIL import ImageOps
from pytesseract import *
import cv2  
import numpy as np

inverted_image = Image.open(r"C:\Users\antho\Pictures\test.png")
path_to_tesseract = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

inverted_array = np.array(inverted_image)

inverted_image = cv2.resize(inverted_array,None,fx = 3 , fy = 3 , interpolation=cv2.INTER_CUBIC)

inverted_image = Image.fromarray(inverted_image)

inverted_image.show()

text = pytesseract.image_to_string(inverted_image)

print(text[:-1])

for i in range (len(inverted_array)):
    if(inverted_array[i] != [ 42, 42, 42, 255].all):
        print(inverted_array[i])

