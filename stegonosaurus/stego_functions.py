'''This library runs on PIL'''
from PIL import Image
from . import stego_utils as su

def inspect(img: Image) -> str:
    '''Returns each individual pixel and additional information
    on the image input.'''
    info_string = ""
    generator = su.image_reader(img)

    for i in generator:
        info_string + i + " "

    info_string += "\n" + "Filename: "

    if hasattr(img, "filename"):
        info_string += img.filename

    info_string = info_string + "\nFormat: " + img.format + "\nMode:" + img.format + "\nSize: " +
    img.width + "x" + img.height + "\n"

    return info_string
