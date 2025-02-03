# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byu_pytest_utils import with_import
from byuimage import Image


def iron_puzzle(filename):
    photo = Image(filename)
    for pixel in photo:
        pixel.color = (0, 0, pixel.blue * 10)
    return photo


def west_puzzle(filename):
    photo = Image(filename)
    for pixel in photo:
        if pixel.blue < 16:
            pixel.color = (0, 0, pixel.blue * 16)
        elif 16 <= pixel.blue:
            pixel.color = (0, 0, 0)
    return photo


def darken(filename, percent):
    photo = Image(filename)
    multiplier = 1 - percent
    for pixel in photo:
        pixel.red = round(pixel.red * multiplier, 0)
        pixel.green = round(pixel.green * multiplier, 0)
        pixel.blue = round(pixel.blue * multiplier, 0)
    return photo


def grayscale(filename):
    photo = Image(filename)
    for pixel in photo:
        average = round((pixel.red + pixel.green + pixel.blue) / 3)
        print(average)
        pixel.color = (average, average, average)
    return photo


def sepia(filename):
    photo = Image(filename)
    for pixel in photo:
        true_red = round(0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue)
        if true_red > 255:
            true_red = 255
        true_green = round(0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue)
        if true_green > 255:
            true_green = 255
        true_blue = round(0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue)
        if true_blue > 255:
            true_blue = 255
        pixel.color = (true_red, true_green, true_blue)
    return photo


def create_left_border(filename, weight):
    photo = Image(filename)
    new_photo = Image.blank(photo.width + weight, photo.height)
    for x in range(weight):
        for y in range(new_photo.height):
            pixel = new_photo.get_pixel(x, y)
            pixel.color = (0, 0, 255)

    for x in range(weight, new_photo.width):
        for y in range(new_photo.height):
            pixel = new_photo.get_pixel(x, y)
            original = photo.get_pixel(x - weight, y)
            pixel.color = (original.red, original.green, original.blue)
    return new_photo


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    photo = Image(filename)
    new_img = Image.blank(photo.width + 50, photo.height + 25)

    # BLUE
    for x in range(new_img.width):
        if (x + 1) % 2 == 0:
            for y in range(new_img.height):
                pixel = new_img.get_pixel(x, y)
                pixel.color = (0, 0, 255)

    # RED
    for x in range(new_img.width):
        for y in range(new_img.height):
            pixel = new_img.get_pixel(x, y)
            if pixel.red == 255 and pixel.green == 255 and pixel.blue == 255:
                pixel.color = (255, 0, 0)

    # GREEN
    for x in range(new_img.width):
        for y in range(new_img.height):
            if y % 2 == 0:
                pixel = new_img.get_pixel(x, y)
                pixel.color = (0, 255, 0)

    return new_img


def copper_puzzle(filename):
    photo = Image(filename)
    for pixel in photo:
        pixel.color = (0, pixel.green * 20, pixel.blue * 20)
    return photo
