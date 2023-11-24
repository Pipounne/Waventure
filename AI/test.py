from pytesseract import pytesseract
from PIL import Image

image_path = r"C:\Users\antho\Pictures\test.png"
tesseract_path = r"C:\Users\antho\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img  = Image.open(image_path)

pytesseract.tesseract_cmd = tesseract_path

print(pytesseract.image_to_string(img))