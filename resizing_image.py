import os
from PIL import Image

size = (254, 254)


def sizing_image(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        im = Image.open(input_folder + filename)
        print("Resizing "+filename)
        im.thumbnail(size)
        im.save(output_folder+filename, 'JPEG')
    print("All images resizing complete..!!")

if __name__ == "__main__":
    input_folder = input("Please Enter input folder like this format 'F:/Images/': ")
    output_folder = input("Please Enter output folder like this format 'F:/Output/': ")

    sizing_image(input_folder, output_folder)


