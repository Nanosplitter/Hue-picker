from PIL import Image
import numpy as np
import colorsys as cs
im = Image.open("C:\\Users\\colin\\OneDrive\\Documents\\GitHub\\Hue-picker\\test.png")
color = 210
color_range = 50
pixels = np.array(im)
for w in range(im.width):
    for h in range(im.height):
        pixel = pixels[h, w]
        hsv = cs.rgb_to_hsv(pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
        hue = hsv[0] * 360
        if not ((color + color_range) >= hue >= (color - color_range)):
            hsv = (hsv[0], 0, hsv[2])
        rgb = cs.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        pixels[h, w] = rgb[0]*255, rgb[1]*255, rgb[2]*255, pixels[h, w][3]

im.show()
Image.fromarray(pixels).show()
