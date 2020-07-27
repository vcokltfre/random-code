from PIL import Image, ImageDraw
from math import sqrt, ceil

def mkimg(filename):
    with open(filename) as f:
        data = f.read()

    cols = [(ord(x), 0, 0) for x in data]
    cols.append((0, 255, 0))
    size = ceil(sqrt(len(cols)))
    img = Image.new("RGB", (size,size))
    img.putdata(cols)
    img.save(f"{filename}.png")

def dcimg(imgfile, outfile):
    data = Image.open(imgfile)
    pixels = list(data.getdata())
    output = ""
    complete = False
    for pixel in pixels:
        if not complete:
            if pixel[1] != 255:
                output += chr(pixel[0])
            else:
                complete = True
    with open(outfile, 'w') as f:
        f.write(output)