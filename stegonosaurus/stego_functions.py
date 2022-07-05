'''This library runs on PIL'''
from PIL import Image
from . import stego_utils as su

def inspect(img: Image) -> str:
    '''Returns each individual pixel and additional information
    on the image input.'''
    info_string = ""
    valid = "No"
    generator = su.image_reader(img)

    for i in generator:
        info_string += i

    info_string += "\n" + "Filename: "

    if hasattr(img, "filename"):
        info_string += img.filename

    if su.validate_image_format(img):
        valid = "Yes"

    info_string += ("\nFormat: " + img.format + "\nMode:" + img.mode + "\nSize: " +
    str(img.width) + "x" + str(img.height) + "\nValid: " + valid)

    return info_string
