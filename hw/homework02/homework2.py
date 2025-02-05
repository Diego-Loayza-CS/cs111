from byuimage import Image

def flipped(filename):
    photo = Image(filename)
    new_photo = Image.blank(photo.width, photo.height)
    for x in range(new_photo.width):
        for y in range(new_photo.height):
            original_pixel = photo.get_pixel(x, -(y+1))
            new_pixel = new_photo.get_pixel(x, y)
            new_pixel.color = (original_pixel.red, original_pixel.green, original_pixel.blue)
    return new_photo

def make_borders(filename, thickness, red, green, blue):
    photo = Image(filename)
    new_photo = Image.blank(photo.width + 2*thickness, photo.height + 2*thickness)
    for pixel in new_photo:
        pixel.color = (red, green, blue)
    for x in range(photo.width):
        for y in range(photo.height):
            pixel = photo.get_pixel(x, y)
            new_pixel = new_photo.get_pixel(x + thickness, y + thickness)
            new_pixel.color = (pixel.red, pixel.green, pixel.blue)
    return new_photo