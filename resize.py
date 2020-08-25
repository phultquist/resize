import PIL.Image
import numpy as np

img = PIL.Image.open('resize/test.png')
img.convert('RGB')
pix = np.array(img)
width, height = img.size

stepsize = int(width / 16)

# print(stepsize)

def generalize(pixels):
    totals = [0,0,0,0]
    for j in range(len(pixels)):
        pixel = pixels[j]
        totals[0] += pixel[0] #r
        totals[1] += pixel[1] #g
        totals[2] += pixel[2] #b
        totals[3] += pixel[3] #alpha
    
    for k in range(len(totals)):
        totals[k] = totals[k] / len(pixels)
        if (totals[k] > 255):
            totals[k] = 255
        totals[k] = np.uint8(totals[k])
    
    return totals

# print(pix)

# i can see how x/y can be confusing here
x = 0
resized = []
# print(width)
while x < width: 
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
        
        gend = generalize(toGeneralize)
        newrow.append(gend)
        y += stepsize

    print('x', x, '   y', y, '   len', newrow)
    resized.append(newrow)
    x += stepsize

# quit()
# print(resized)
# print(len(resized))
# print(len(resized[0]))
# print(len(resized[0][0]))
im = PIL.Image.fromarray(np.array(resized))
im.show()

print(len(pix))
print(len(pix[0]))
print(len(pix[0][0]))