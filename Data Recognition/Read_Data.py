from PIL import Image
from PIL import ImageGrab
from pytesseract import *
import cv2  
import numpy as np

snapshot = ImageGrab.grab(bbox=(0,0,1343,881))
path_to_tesseract = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

im_rgb = snapshot.convert('RGB')

print(im_rgb)

snapshot.show()

#text = pytesseract.image_to_string(inverted_image)

#print(text[:-1])

