from PIL import Image


print("Image Converter")
print("1. jpg to png    2. png to jpg")
print("3. jpg to bmp")

num = input("Input here ")


if (input == 1 ) :
    # Open the JPEG image file
    jpg_image = Image.open("./src/Kevin.jpg")

    # Convert the image to RGBA format (if it is not already in RGBA)
    if jpg_image.mode != "RGBA":
        jpg_image = jpg_image.convert("RGBA")

    # Save the image in PNG format
    jpg_image.save("output_image.png", "PNG")

elif (input == 2) :
        
    # Open the PNG image file
    png_image = Image.open("input_image.png")

    # Convert the image to RGB format (if it is not already in RGB)
    if png_image.mode != "RGB":
        png_image = png_image.convert("RGB")

    # Save the image in JPEG format
    png_image.save("output_image.jpg", "JPEG")

elif (input == 3) :

    # Open the JPG image
    jpg_image = Image.open("input.jpg")

    # Convert to BMP format
    bmp_image = jpg_image.convert("RGB")

    # Save the BMP image
    bmp_image.save("output.bmp")

