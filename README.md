# resize
This resizes an image using a custom algorithm. Built for the Frame, the smart album cover display.

## Algorithm
Splits up the image in to a grid of 16 pixels (adjustable of course), and averages the red, green, and blue values of that region. 

**Then, it boosts the contrast as averaging pixels dulls the image. [Here's the math](https://www.desmos.com/calculator/rkdaypwhdy) behind that part.** Basically, this makes the image overall brighter and more fun. 

In essence, this is a weighted average.

## Why didn't we use existing software?
The existing software often didn't deal with sharp edges too well, and would produce dull images.

## Note
1. This assumes that 
    a) the initial image is a square
    b) the desired image is a square
2. **This is not very robust.** It might not work perfectly for odd image types. However, it works for its purpose. In the future I'll update it to be a useful general tool.
