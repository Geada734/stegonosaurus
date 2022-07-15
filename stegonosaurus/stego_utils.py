'''Generic functions module'''
from PIL import Image


def image_reader(img: Image) -> str:
    '''Generator that reads the whole image to be used in the
    inspect_image function'''
    img_data = list(img.getdata())

    for i in img_data:
        yield str(i)


def validate_image_format(img: Image) -> bool:
    '''Validates the file is a multiband PNG image'''
    if img.format != "PNG":
        return False
    elif img.mode != "RGB" and img.mode != "RGBA":
        return False

    return True


def validate_images_size(coded: Image, img: Image) -> bool:
    '''Validates the image with the coded message isn't larger than the
    image used to hide the message.'''
    coded_width = coded.size[0]
    coded_height = coded.size[1]
    img_width = img.size[0]
    img_height = img.size[1]

    if coded_width>img_width or coded_height>img_height:
        return False

    return True


def flatten_image(img: Image) -> Image:
    '''Makes sure the message can be encoded in the image.'''
    pix_x = 0
    pix_y = 0
    width = img.size[0]
    height = img.size[1]

    # Copy of the original image.
    new_img = img.copy()

    # Iterates over each pixel in the image to make their RGB value
    # even.
    for pix_x in range(0, width):
        for pix_y in range(0, height):
            pix = list(img.getpixel((pix_x, pix_y)))
            red = pix[0]
            green = pix[1]
            blue = pix[2]

            # Since blue is the "B" in "RGB", that's the value we are
            # making even.
            if blue%2==1:
                blue = blue - 1
                new_img.putpixel((pix_x, pix_y), (red, green, blue, 255))

    return new_img


def flatten_coded(img: Image) -> Image:
    '''Makes the image's blacks extra black.'''
    pix_x = 0
    pix_y = 0
    width = img.size[0]
    height = img.size[1]

    # Copy of the orginal image.
    new_img = img.copy()

    # Iterates over each pixel to make the image usable by turning
    # them black.
    for pix_x in range(0, width):
        for pix_y in range(0, height):
            if img.getpixel((pix_x,pix_y))[0]==0:
                new_img.putpixel((pix_x, pix_y), (0, 0, 0, 255))

    return new_img
    