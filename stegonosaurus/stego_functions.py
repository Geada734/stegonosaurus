'''This library runs on PIL'''
from PIL import Image
from . import stego_utils as su

def inspect(img: Image):
    '''Inspects an image.'''
    generator = su.image_reader(img)

    for i in generator:
        print(i)

    img.show()
