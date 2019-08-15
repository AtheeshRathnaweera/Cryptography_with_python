from PIL import Image
import stepic

#Open Image or file
image = Image.open('image.jpg')

#Encode some text into your Image file and save it in another file
secret = "Hey this is the secret message!"
imageWithSecret = stepic.encode(image, secret.encode('utf-8')) #encode the string to bytes before encode with the image
imageWithSecret.save('imageNew.png', 'PNG')


#Decode the image and show results
imageTemp = Image.open('imageNew.png')
results = stepic.decode(imageTemp)

print("This is the result : "+results)




