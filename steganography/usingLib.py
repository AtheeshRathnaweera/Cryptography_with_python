from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('thIsisThEseCRetKEy')#set a key 

# Save the encrypted file inside the image
crypto_steganography.hide('puppy.jpg', 'puppywithsecret.png', 'Hello! This is a gsd puppy.') #secret message

secret = crypto_steganography.retrieve('puppywithsecret.png') # read the .png and retrieve the message

print(secret)