import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        write_to_shirt(sys.argv[1], sys.argv[2])

def write_to_shirt(shirt_1, shirt_2):
    try:
        extension1 = os.path.splitext(shirt_1)
        extension2 = os.path.splitext(shirt_2)

        if extension1[1].casefold() != extension2[1].casefold():
            sys.exit("Input and output have different extensions") 
            
        else:

            image1 = Image.open(shirt_1)
            shirt = Image.open("shirt.png")
            resize = ImageOps.fit(image1, shirt.size)
            resize.paste(shirt, shirt)
            resize.save(shirt_2)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ in "__main__":
    main()