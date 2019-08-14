from PIL import Image, ImageFont, ImageDraw
import textwrap


def writingText(text, imageSize):

    image_text = Image.new("RGB", imageSize)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    #Text wrapping. Change parameters for different text formatting
    margin = offset = 10
    for line in textwrap.wrap(text, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encoding(text_to_encode, template_image="puppy.jpg"):

    imgTemplate = Image.open(template_image)
    redTemplate = imgTemplate.split()[0]
    greenTemplate = imgTemplate.split()[1]
    blueTemplate = imgTemplate.split()[2]

    xSize = imgTemplate.size[0]
    ySize = imgTemplate.size[1]

    #drawing text
    imageText = writingText(text_to_encode, imgTemplate.size)
    bw_encode = imageText.convert('1') #convert the image text to mode 1

    # MODE --- The mode of an image defines the type and depth of a pixel in the image
    # MODE "1" ------ 1-bit pixels, black and white, stored with one pixel per byte
    # MODE "RGB" ----3x8-bit pixels, true color

    #encode text into image
    encoded_image = Image.new("RGB", (xSize, ySize))
    pixels = encoded_image.load() #Allocates storage for the image and loads the pixel data

    for i in range(xSize):
        for j in range(ySize):
            red_template_pix = bin(redTemplate.getpixel((i,j)))
            old_pix = redTemplate.getpixel((i,j))
            tencode_pix = bin(bw_encode.getpixel((i,j)))

            if tencode_pix[-1] == '1':
                red_template_pix = red_template_pix[:-1] + '1'
            else:
                red_template_pix = red_template_pix[:-1] + '0'
            pixels[i, j] = (int(red_template_pix, 2), greenTemplate.getpixel((i,j)), blueTemplate.getpixel((i,j)))

    encoded_image.save("pillRes_encodedPuppy.png")

    print("\n\tMessage encoded and hide in the image successfully. Output file: encodedPuppy.png")


def decoding(file_location="pillRes_encodedPuppy.png"):

    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255) #display white if the first bit == 0
            else:
                pixels[i, j] = (0,0,0) #else black

    decoded_image.save("pillRes_decodedImage.png")

    print("\n\tdecoded the encoded image successfully.")
    #hidden message will be appeared in a white background


encoding("This is the hidden message.")
decoding()