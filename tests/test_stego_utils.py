'''Test the utils for the Stegonosaurus library'''
import pytest
from PIL import Image
from stegonosaurus import stego_utils as su

# Sample abstract images used for testing:
@pytest.fixture
def raw_image_rgb_png():
    '''Creates a raw RGB image used to hide a message in'''
    new_image = Image.new(mode ="RGB", size=(2,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (0, 255, 255))
    new_image.putpixel((0,1), (0, 255, 255))
    new_image.putpixel((1,0), (0, 255, 255))
    new_image.putpixel((1,1), (0, 255, 255))

    return new_image

@pytest.fixture
def raw_image_rgba_png():
    '''Creates a raw RGBA .png image used to hide a message in'''
    new_image = Image.new(mode ="RGBA", size=(2,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (0, 255, 255, 255))
    new_image.putpixel((0,1), (0, 255, 255, 255))
    new_image.putpixel((1,0), (0, 255, 255, 255))
    new_image.putpixel((1,1), (0, 255, 255, 255))

    return new_image

@pytest.fixture
def raw_image_l_png():
    '''Creates a raw RGBA .png image used to hide a message in'''
    new_image = Image.new(mode ="L", size=(2,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), 0)
    new_image.putpixel((0,1), 0)
    new_image.putpixel((1,0), 0)
    new_image.putpixel((1,1), 0)

    return new_image

@pytest.fixture
def raw_image_rgb_jpeg():
    '''Creates a raw RGB .jpeg image used to hide a message in'''
    new_image = Image.new(mode ="RGB", size=(2,2))
    new_image.format = "JPG"

    new_image.putpixel((0,0), (0, 255, 255))
    new_image.putpixel((0,1), (0, 255, 255))
    new_image.putpixel((1,0), (0, 255, 255))
    new_image.putpixel((1,1), (0, 255, 255))

    return new_image

@pytest.fixture
def raw_image_rgba_jpeg():
    '''Creates a raw RGBA .jpeg image used to hide a message in'''
    new_image = Image.new(mode ="RGBA", size=(2,2))
    new_image.format = "JPG"

    new_image.putpixel((0,0), (0, 255, 255, 255))
    new_image.putpixel((0,1), (0, 255, 255, 255))
    new_image.putpixel((1,0), (0, 255, 255, 255))
    new_image.putpixel((1,1), (0, 255, 255, 255))

    return new_image

@pytest.fixture
def raw_coded_rgb_png():
    '''Creates a raw RGB image used to encode a message'''
    new_image = Image.new(mode ="RGB", size=(2,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (255, 0, 0))
    new_image.putpixel((0,1), (0, 1, 1))
    new_image.putpixel((1,0), (0, 1, 1))
    new_image.putpixel((1,1), (0, 1, 1))

    return new_image

@pytest.fixture
def raw_coded_rgba_png():
    '''Creates a raw RGBA image used to encode a message'''
    new_image = Image.new(mode ="RGBA", size=(2,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (255, 0, 0, 255))
    new_image.putpixel((0,1), (0, 1, 1, 255))
    new_image.putpixel((1,0), (0, 1, 1, 255))
    new_image.putpixel((1,1), (0, 1, 1, 255))

    return new_image

@pytest.fixture
def raw_coded_smaller_rgb_png():
    '''Creates a small raw RGB image used to encode a message'''
    new_image = Image.new(mode ="RGB", size=(2,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (255, 0, 0))

    return new_image

@pytest.fixture
def raw_coded_larger_x_rgb_png():
    '''Creates a raw RGBA image used to encode a message'''
    new_image = Image.new(mode ="RGBA", size=(3,2))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (255, 0, 0))
    new_image.putpixel((0,1), (0, 1, 1))
    new_image.putpixel((1,0), (0, 1, 1))
    new_image.putpixel((1,1), (0, 1, 1))
    new_image.putpixel((2,0), (0, 1, 1))
    new_image.putpixel((2,1), (0, 1, 1))

    return new_image

@pytest.fixture
def raw_coded_larger_y_rgb_png():
    '''Creates a raw RGBA image used to encode a message'''
    new_image = Image.new(mode ="RGBA", size=(2,3))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (255, 0, 0))
    new_image.putpixel((0,1), (0, 1, 1))
    new_image.putpixel((0,2), (0, 1, 1))
    new_image.putpixel((1,0), (0, 1, 1))
    new_image.putpixel((1,1), (0, 1, 1))
    new_image.putpixel((1,2), (0, 1, 1))

    return new_image

@pytest.fixture
def raw_coded_larger_rgb_png():
    '''Creates a raw RGBA image used to encode a message'''
    new_image = Image.new(mode ="RGBA", size=(3,3))
    new_image.format = "PNG"

    new_image.putpixel((0,0), (255, 0, 0))
    new_image.putpixel((0,1), (0, 1, 1))
    new_image.putpixel((0,2), (0, 1, 1))
    new_image.putpixel((1,0), (0, 1, 1))
    new_image.putpixel((1,1), (0, 1, 1))
    new_image.putpixel((1,2), (0, 1, 1))
    new_image.putpixel((2,0), (0, 1, 1))
    new_image.putpixel((2,1), (0, 1, 1))
    new_image.putpixel((2,2), (0, 1, 1))

    return new_image

# Image reader tests:
def test_image_reader(raw_image_rgb_png):
    '''Tests the image reader, generator used in the inspect function.'''
    data = []

    for i in su.image_reader(raw_image_rgb_png):
        data.append(i)

    assert data == ["(0, 255, 255)", "(0, 255, 255)", "(0, 255, 255)", "(0, 255, 255)"]

# Format validation tests:
def test_validate_format_png_rgb(raw_image_rgb_png):
    '''Test the validation of a .png RGB image'''
    assert su.validate_image_format(raw_image_rgb_png)

def test_validate_format_png_rgba(raw_image_rgba_png):
    '''Test the validation of a .png RGB image'''
    assert su.validate_image_format(raw_image_rgba_png)

def test_validate_format_l_rgb(raw_image_l_png):
    '''Test the validation of a .png single-band image'''
    assert not su.validate_image_format(raw_image_l_png)

def test_validate_format_jpeg_rgb(raw_image_rgb_jpeg):
    '''Test the validation of a .png RGB image'''
    assert not su.validate_image_format(raw_image_rgb_jpeg)

def test_validate_format_jpeg_rgba(raw_image_rgba_jpeg):
    '''Test the validation of a .png RGB image'''
    assert not su.validate_image_format(raw_image_rgba_jpeg)

# Size validation tests:
def test_same_size_images(raw_coded_rgb_png, raw_image_rgb_png):
    '''Test the validation of same size .png RGB images'''
    assert su.validate_images_size(raw_coded_rgb_png, raw_image_rgb_png)

def test_smaller_coded_image(raw_coded_smaller_rgb_png, raw_image_rgb_png):
    '''Test the validation of same size .png RGB images'''
    assert su.validate_images_size(raw_coded_smaller_rgb_png, raw_image_rgb_png)

def test_larger_x_coded_image(raw_coded_larger_x_rgb_png, raw_image_rgb_png):
    '''Test the validation of a horizontally smaller .png RGB images'''
    assert not su.validate_images_size(raw_coded_larger_x_rgb_png, raw_image_rgb_png)

def test_larger_y_coded_image(raw_coded_larger_y_rgb_png, raw_image_rgb_png):
    '''Test the validation of a vertically smaller .png RGB images'''
    assert not su.validate_images_size(raw_coded_larger_y_rgb_png, raw_image_rgb_png)

def test_larger_coded_image(raw_coded_larger_rgb_png, raw_image_rgb_png):
    '''Test the validation of a smaller .png RGB images'''
    assert not su.validate_images_size(raw_coded_larger_rgb_png, raw_image_rgb_png)

# Image flattening tests:
def test_flatten_rgb_image(raw_image_rgb_png):
    '''Test the flatenning of an RGBA .png image'''
    flat_image = su.flatten_image(raw_image_rgb_png)
    data = []

    for i in su.image_reader(flat_image):
        data.append(i)

    assert data == ["(0, 255, 254)", "(0, 255, 254)",
                    "(0, 255, 254)", "(0, 255, 254)"]

# Image flattening tests:
def test_flatten_rgba_image(raw_image_rgba_png):
    '''Test the flatenning of an RGBA .png image'''
    flat_image = su.flatten_image(raw_image_rgba_png)
    data = []

    for i in su.image_reader(flat_image):
        data.append(i)

    assert data == ["(0, 255, 254, 255)", "(0, 255, 254, 255)",
                    "(0, 255, 254, 255)", "(0, 255, 254, 255)"]

def test_flatten_code_rgb_image(raw_coded_rgb_png):
    '''Tests the falettening of an RGB .png coded image.'''
    flat_coded = su.flatten_coded(raw_coded_rgb_png)
    data = []

    for i in su.image_reader(flat_coded):
        data.append(i)

    assert data == ["(255, 0, 0)", "(0, 0, 0)", "(0, 0, 0)", "(0, 0, 0)"]

def test_flatten_code_rgba_image(raw_coded_rgba_png):
    '''Tests the falettening of an RGB .png coded image.'''
    flat_coded = su.flatten_coded(raw_coded_rgba_png)
    data = []

    for i in su.image_reader(flat_coded):
        data.append(i)

    assert data == ["(255, 0, 0, 255)", "(0, 0, 0, 255)", "(0, 0, 0, 255)", "(0, 0, 0, 255)"]
