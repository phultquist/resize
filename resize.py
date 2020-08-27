import PIL.Image
import numpy as np
from io import BytesIO
import requests
import math

width, height, stepsize = (0,0,0)

# content = src
# if src.startswith('http'):
#     imgresp = requests.get(src)
#     content = BytesIO(imgresp.content)

size = 16

def resize(img):
    global width, height, stepsize
    img.convert('RGB')
    pix = np.array(img)
    width, height = img.size
    # if width == size:
    #     return pix
    stepsize = int(width / size)
    return get_new_pixels(pix)


def generalize(pixels, type):
    # transpose data to get array of reds, blues, greens
    reds = []
    greens = []
    blues = []
    for j in range(len(pixels)):
        pixel = pixels[j]
        try:
            reds.append(pixel[0])
            greens.append(pixel[1])
            blues.append(pixel[2])
        except:
            reds.append(pixel)
            greens.append(pixel)
            blues.append(pixel)

    red = 0
    green = 0
    blue = 0

    if type=='mean':
        red = np.mean(np.array(reds))
        green = np.mean(np.array(greens))
        blue = np.mean(np.array(blues))
    elif type=='median':
        red = np.median(np.array(reds))
        green = np.median(np.array(greens))
        blue = np.median(np.array(blues))

    totals = [red, green, blue, 255]

    for k in range(len(totals)):
        if totals[k] > 255:
            totals[k] = 255
        elif totals[k] < 0:
            totals[k] = 0
        totals[k] = np.uint8(contrast(totals[k]))
    return totals

def contrast(o):
    m = 255
    g = 1.1

    if o == 0 or o == 255 or o == m/2:
        return o
    g2 = 1/g
    if o < m/2:
        return -1 * ((m/2) * ((2*(-1*o+m/2)/m) ** g2) - m/2)
    elif o > m/2:
        return ((m/2) * ((2*(o-m/2)/m) ** g2) + m/2)

def get_new_pixels(pix):
    x = 0
    resized = []
    while x < height:
        y = 0
        newrow = []
        while y < width:
            # print('x', x, '   y', y)
            toGeneralize = []
            a = 0
            b = 0
            for a in range(stepsize):
                for b in range(stepsize):
                    toGeneralize.append(pix[x+a][y+b])

            generated = generalize(toGeneralize, 'mean')
            # gend[3] = np.uint8(255)
            # print(generated)
            newrow.append(generated)
            y += stepsize

        # print('x', x, '   y', y, '   len', newrow)
        resized.append(newrow)
        x += stepsize

    # resizedimg = PIL.Image.fromarray(np.array(resized))
    # resizedimg.show()
    return np.array(resized)
