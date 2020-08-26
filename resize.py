import PIL.Image
import numpy as np
from io import BytesIO
import requests


#ydb
src = 'https://i.scdn.co/image/ab67616d00004851988ede5e1276e758b5f9e577'

#graduation
src = 'resize/test.png'

#xxx album
src = 'https://i.scdn.co/image/ab67616d00004851806c160566580d6335d1f16c'

#mbdtf
src = 'https://i.scdn.co/image/ab67616d00004851d9194aa18fa4c9362b47464f'
content = src
if src.startswith('http'):
    imgresp = requests.get(src)
    content = BytesIO(imgresp.content)
img = PIL.Image.open(content)
img.convert('RGB')
pix = np.array(img)
width, height = img.size
stepsize = int(width / 16)


def generalize(pixels, avg):
    totals = [0, 0, 0, 0]
    if avg:
        for j in range(len(pixels)):
            pixel = pixels[j]
            try:
                totals[0] += pixel[0]  # r
                totals[1] += pixel[1]  # g
                totals[2] += pixel[2]  # b
            except:
                totals[0] += pixel  # r
                totals[1] += pixel  # g
                totals[2] += pixel  # b
            # totals[3] += pixel[3] #alpha

        for k in range(len(totals)):
            totals[k] = totals[k] / len(pixels)
        totals[3] = 255
    else:
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

        red = np.median(np.array(reds))
        green = np.median(np.array(greens))
        blue = np.median(np.array(blues))

        totals = [red, green, blue, 255]

    for k in range(len(totals)):
        if (totals[k] > 255):
            totals[k] = 255
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
        for a in range(4):
            for b in range(4):
                toGeneralize.append(pix[x+a][y+b])

        genavg = generalize(toGeneralize, True)
        genmed = generalize(toGeneralize, False)
        gend = []
        for l in range(len(genavg)):
            gend.append(np.uint8((genavg[l]+genmed[l]) / 2))
        # gend[3] = np.uint8(255)
        print(genavg)
        print(genmed)
        print(gend)
        print('  ')
        newrow.append(genavg)
        y += stepsize

    # print('x', x, '   y', y, '   len', newrow)
    resized.append(newrow)
    x += stepsize

im = PIL.Image.fromarray(np.array(resized))
im.show()

print(len(pix))
print(len(pix[0]))
print(len(pix[0][0]))


