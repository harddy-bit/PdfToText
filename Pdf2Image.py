# Import libraries
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HARDIK\AppData\Local\Tesseract-OCR\tesseract.exe'
import sys
from pdf2image import convert_from_path
import os


PDF_file = "Sample.pdf"

#PDF to images
pages = convert_from_path(PDF_file, 500)
image_counter = 1

for page in pages:
    filename = "page_" + str(image_counter) + ".jpg"

    page.save(filename, 'JPEG')
    image_counter = image_counter + 1

#Recognizing text from the images using OCR

fileEnd = image_counter - 1
finaloutput = "out_text2.txt"
f = open(finaloutput, "a")

# Iterate from 1 to total number of pages----> Recognize Text File from page_n.jpg
for i in range(1, fileEnd + 1):
    filename = "page_" + str(i) + ".jpg"

    # Recognize the text as string
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    f.write(text)

f.close()
