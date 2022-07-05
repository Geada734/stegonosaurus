'''Generic functions module'''
from PIL import Image

def image_reader(img: Image):
    '''Generator that reads the whole image to be used in the inspect_image function'''
    img_data = list(img.getdata())

    for i in img_data:
        yield str(i)
