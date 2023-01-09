from PIL import Image

def floyd_steinberg(image):
    pixels = image.load()
    image_copy = image.copy()
    pixels_copy = image_copy.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            o_r, o_g, o_b = pixels[x, y]
            n_r = 51 * round(o_r // 51)
            n_g = 51 * round(o_g // 51)
            n_b = 51 * round(o_b // 51)
            pixels_copy[x, y] = (n_r, n_g, n_b)
            chyba_r = o_r - n_r
            chyba_g = o_g - n_g
            chyba_b = o_b - n_b
            if x < width-1:
                pixels[x+1, y] = (pixels[x+1, y][0] + chyba_r * 7//16, pixels[x+1, y][1] + chyba_g * 7//16, pixels[x+1, y][2] + chyba_b * 7//16)
            if y < height-1:
                if x > 0:
                    pixels[x-1, y+1] = (pixels[x-1, y+1][0] + chyba_r * 3//16, pixels[x-1, y+1][1] + chyba_g * 3//16, pixels[x-1, y+1][2] + chyba_b * 3//16)
                pixels[x, y+1] = (pixels[x, y+1][0] + chyba_r * 5//16, pixels[x, y+1][1] + chyba_g * 5//16,  pixels[x, y+1][2] + chyba_b * 5//16)
                if x < width-1:
                    pixels[x+1, y+1] = (pixels[x+1, y+1][0] + chyba_r * 1//16, pixels[x+1, y+1][1] + chyba_g * 1//16, pixels[x+1, y+1][2] + chyba_b * 1//16)
    return image_copy

image = Image.open('image.png')
dithered_image = floyd_steinberg(image)
im1 = dithered_image.save("final.png")