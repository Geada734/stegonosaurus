'''This library runs on PIL'''
from PIL import Image
from . import stego_utils as su
from . import stego_exceptions as se

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

def blacken(img: Image) -> Image:
    '''Creates an all-black image with the provided image's dimensions.'''
    new_img = img.copy()

    if su.validate_image_format(img):
        pix_x = img.size[0]
        pix_y = img.size[1]
        width = img.width
        height = img.height

        for pix_x in range(0, width):
            for pix_y in range(0, height):
                new_img.putpixel((pix_x, pix_y), (0, 0, 0, 255))
    else:
        raise se.StegonosaurusIncorrectFormatException("The file must be a multi-band .png image.")

    return new_img
    