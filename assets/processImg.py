


from PIL import Image

with Image.open('table.png') as im:
    px = im.load()


height,width = im.size



for loop1 in range(height):
    for loop2 in range(width):
        if px[loop1, loop2] == (0,0,0):
            px[loop1, loop2] = (255, 255, 255, 0)


im.save('table.png')
