# resize
This resizes an image using a custom algorithm. Built for the [smart album cover display](https://github.com/phultquist/smart-album-cover)

## Algorithm
Splits up the image in to a grid of 16 pixels (easy to change of course), and averages the red, green, and blue values of that region. 

### Then, it boosts the contrast as averaging pixels genearally dullens the image. [here's the math](https://www.desmos.com/calculator/xsoj6patxg) behind that part

Basically, the goal is to make the high values higher and the low values lower.
