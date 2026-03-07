from PIL import Image
import sys

try:
    img = Image.open('images/airbound-deeptech-growth-banner.png')
    width, height = img.size
    print(f"Image size: {width}x{height}")
    pixels = [img.getpixel((0,0)), img.getpixel((width-1,0)), img.getpixel((0,height-1)), img.getpixel((width-1,height-1))]
    print(f"Corner pixels: {pixels}")
except Exception as e:
    print(e)
