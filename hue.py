import time
import PIL
from PIL import Image
import numpy

image = Image.open('test.jpg').convert('HSV')

data = image.load()

for row in data:
    for pixel in row:
        print(pixel)