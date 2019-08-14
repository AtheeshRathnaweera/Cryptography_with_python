#Store a message string inside an image using python lib "cryptosteganography "
#cryptosteganography --- A python steganography module to store messages or files protected with AES-256 encryption inside an image.

from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('thIsisThEseCRetKEy')#set a key 

# Save the encrypted file inside the image
crypto_steganography.hide('puppy.jpg', 'puppywithsecret.png', 'Hello! This is a gsd puppy.') #secret message

secret = crypto_steganography.retrieve('puppywithsecret.png') # read the .png and retrieve the message

print(secret) #print the secret message after reading

#cons -- output file size is considerably high compared to the original file