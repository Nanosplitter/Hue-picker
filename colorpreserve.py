from PIL import Image
import numpy as np
import colorsys as cs
im = Image.open("C:\\Users\\colin\\OneDrive\\Documents\\GitHub\\Hue-picker\\test.png")
color = 39
color_range = 70
pixels = np.array(im)
for w in range(im.width):
    for h in range(im.height):
        pixel = pixels[h, w]
        hsv = cs.rgb_to_hsv(pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
        hue = hsv[0] * 360
        # if not ((color + color_range) >= hue >= (color - color_range)):
        # print(abs((hue-color)/360))
        #hsv[1]*(abs((hue-color)/360))
        dist = abs(color - hue)
        dropoff = color + color_range + (color_range/4)
        modifier = hsv[1] - (dist/color)
        saturation = hsv[1] * modifier if hsv[1] * modifier > 0 and dist < dropoff else 0
        hsv = (hsv[0], saturation, hsv[2])
        # else:
        #     hsv = (hsv[0], 0, hsv[2])
        rgb = cs.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        pixels[h, w] = rgb[0]*255, rgb[1]*255, rgb[2]*255, pixels[h, w][3]

im.show()
Image.fromarray(pixels).show()
