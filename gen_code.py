from PIL import Image

def encode(rgb):
    (r,g,b) = rgb
    return ((r & 128) >> 2) + ((g & 128) >> 4) + ((b & 128) >> 6)

myimage = Image.open('test_pic.jpg')
myimage.load()

size_x = 60
size_y = 28

string = ''

for y in range(size_y):
    for x in range(size_x):
        string += 'image['+str(x + (y*size_x)) + '] = ' + str(encode(myimage.getpixel((x,y)))) +';'
print(string)

