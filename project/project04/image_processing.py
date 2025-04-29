from byuimage import Image
import sys


def check_args(args, i):
    if len(args) > i:
        print("Unexpected Arguments")
        return False
    elif len(args) < i:
        print("Missing Arguments")
        return False
    else:
        return True


def display(args):
    photo = Image(args[1])
    photo.show()


def darken(args):
    photo = Image(args[1])
    multiplier = 1 - float(args[3])
    for pixel in photo:
        pixel.red = round(pixel.red * multiplier, 0)
        pixel.green = round(pixel.green * multiplier, 0)
        pixel.blue = round(pixel.blue * multiplier, 0)
    photo.save(args[2])


def sepia(args):
    photo = Image(args[1])
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
    photo.save(args[2])


def grayscale(args):
    photo = Image(args[1])
    for pixel in photo:
        average = round((pixel.red + pixel.green + pixel.blue) / 3)
        print(average)
        pixel.color = (average, average, average)
    photo.save(args[2])


def make_borders(args):
    photo = Image(args[1])
    new_photo = Image.blank(photo.width + 2 * int(args[3]), photo.height + 2 * int(args[3]))
    for pixel in new_photo:
        pixel.color = (int(args[4]), int(args[5]), int(args[6]))
    for x in range(photo.width):
        for y in range(photo.height):
            pixel = photo.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x + int(args[3]), y + int(args[3]))
            new_pixel.color = (pixel.red, pixel.green, pixel.blue)
    new_photo.save(args[2])


def flipped(args):
    photo = Image(args[1])
    new_photo = Image.blank(photo.width, photo.height)
    for x in range(new_photo.width):
        for y in range(new_photo.height):
            original_pixel = photo.get_pixel(x, -(y + 1))
            new_pixel = new_photo.get_pixel(x, y)
            new_pixel.color = (original_pixel.red, original_pixel.green, original_pixel.blue)
    new_photo.save(args[2])


def mirror(args):
    photo = Image(args[1])
    new_photo = Image.blank(photo.width, photo.height)
    for x in range(new_photo.width):
        for y in range(new_photo.height):
            original_pixel = photo.get_pixel(-(x + 1), y)
            new_pixel = new_photo.get_pixel(x, y)
            new_pixel.color = (original_pixel.red, original_pixel.green, original_pixel.blue)
    new_photo.save(args[2])


def collage(args):
    photo1 = Image(args[1])
    photo2 = Image(args[2])
    photo3 = Image(args[3])
    photo4 = Image(args[4])

    new_photo = Image.blank(photo1.width * 2 + int(args[6]) * 3, photo1.height * 2 + int(args[6]) * 3)
    for pixel in new_photo:
        pixel.color = (0, 0, 0)

    # PHOTO 1
    for x in range(photo1.width):
        for y in range(photo1.height):
            pixel = photo1.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x + int(args[6]), y + int(args[6]))
            new_pixel.color = (pixel.red, pixel.green, pixel.blue)

    # PHOTO 2
    for x in range(photo2.width):
        for y in range(photo2.height):
            pixel = photo2.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x + photo1.width + int(args[6]) * 2, y + int(args[6]))
            new_pixel.color = (pixel.red, pixel.green, pixel.blue)

    # PHOTO 3
    for x in range(photo3.width):
        for y in range(photo3.height):
            pixel = photo3.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x + int(args[6]), y + photo1.height + int(args[6]) * 2)
            new_pixel.color = (pixel.red, pixel.green, pixel.blue)

    # PHOTO 4
    for x in range(photo4.width):
        for y in range(photo4.height):
            pixel = photo4.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x + photo1.width + int(args[6]) * 2, y + photo1.height + int(args[6]) * 2)
            new_pixel.color = (pixel.red, pixel.green, pixel.blue)

    new_photo.save(args[5])


def detect_green(pixel, threshold, factor):
    average_rgb = (pixel.red + pixel.green + pixel.blue) / 3
    return pixel.green > threshold and pixel.green >= average_rgb * factor


def green_screen(args):
    foreground = Image(args[1])
    background = Image(args[2])
    new_photo = Image.blank(background.width, background.height)
    for x in range(new_photo.width):
        for y in range(new_photo.height):
            bg_pixel = background.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x, y)
            new_pixel.color = (bg_pixel.red, bg_pixel.green, bg_pixel.blue)
    for x in range(foreground.width):
        for y in range(foreground.height):
            fg_pixel = foreground.get_pixel(x, y)
            if not detect_green(fg_pixel, int(args[4]), float(args[5])):
                new_pixel = new_photo.get_pixel(x, y)
                new_pixel.color = (fg_pixel.red, fg_pixel.green, fg_pixel.blue)
    new_photo.save(args[3])


def validate_commands(args):
    if args[0] == "-d":
        if check_args(args, 2):
            display(args)
    elif args[0] == "-k":
        if check_args(args, 4):
            darken(args)
    elif args[0] == "-s":
        if check_args(args, 3):
            sepia(args)
    elif args[0] == "-g":
        if check_args(args, 3):
            grayscale(args)
    elif args[0] == "-b":
        if check_args(args, 7):
            make_borders(args)
    elif args[0] == "-f":
        if check_args(args, 3):
            flipped(args)
    elif args[0] == "-m":
        if check_args(args, 3):
            mirror(args)
    elif args[0] == "-c":
        if check_args(args, 7):
            collage(args)
    elif args[0] == "-y":
        if check_args(args, 6):
            green_screen(args)
    else:
        print("Invalid Command")


def main(arguments):
    args = arguments[1:]
    validate_commands(args)


if __name__ == '__main__':
    main(sys.argv)
