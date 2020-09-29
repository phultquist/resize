# resize
This resizes an image using a custom algorithm. Built for the [smart album cover display](https://github.com/phultquist/smart-album-cover)

## Algorithm
Splits up the image in to a grid of 16 pixels (easy to change of course), and averages the red, green, and blue values of that region. 

### Then, it boosts the contrast as averaging pixels dulls the image. [here's the math](https://www.desmos.com/calculator/rkdaypwhdy) behind that part.

Basically, the goal is to make the high values higher and the low values lower.

## Note
1. This assumes that 
    a) the initial image is a square
    b) the desired image is a square

    Honestly, this is really easy to change. But to keep it strict for album covers, I'd like to keep it this way. Perhaps I'll update it in the future.
2. **This is not very robust.** It might not work perfectly for odd image types. However, it works for its purpose. In the future I'll update it to be a useful general tool.
