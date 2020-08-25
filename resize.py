import PIL.Image
import numpy as np
from io import BytesIO
import requests

# src = 'https://i.scdn.co/image/ab67616d00004851988ede5e1276e758b5f9e577'
src = 'resize/test.png'
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
    totals = [0,0,0,0]
    if avg:    
        for j in range(len(pixels)):
            pixel = pixels[j]
            totals[0] += pixel[0] #r
            totals[1] += pixel[1] #g
            totals[2] += pixel[2] #b
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
            reds.append(pixel[0])
            greens.append(pixel[1])
            blues.append(pixel[2])
        
        red = np.median(np.array(reds))
        green = np.median(np.array(greens))
        blue = np.median(np.array(blues))

        totals = [red, green, blue, 255]
    
    for k in range(len(totals)):
            if (totals[k] > 255):
                totals[k] = 255
            totals[k] = np.uint8(totals[k])
    return totals

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
        newrow.append(genmed)
        y += stepsize

    # print('x', x, '   y', y, '   len', newrow)
    resized.append(newrow)
    x += stepsize

im = PIL.Image.fromarray(np.array(resized))
im.show()

print(len(pix))
print(len(pix[0]))
print(len(pix[0][0]))