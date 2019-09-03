#Usage of blowfish algorithm
from Crypto.Cipher import Blowfish


def paddingTheMessage(plainText):
    #algorithm works only if the plain text is a multiple of 8
    length = len(plainText)
    missingDigits = length%8

    if missingDigits != 0 :
        for x in range(8-missingDigits):
            plainText = plainText + " " #padding spaces for make the length of the message is a multiple of 8

    return plainText

def creatingTheCipher(key) :   

    cipher = Blowfish.new(key, Blowfish.MODE_ECB) #Creating the new blowfish cipher
    print("Cipher : "+str(cipher))
    return cipher

def encryption(cipher,plainText):
    
    result = cipher.encrypt(plainText)  #Encrypting the message
    print("Encrypted message : "+str(result))
    return result

def decryption(cipher,encryptedRes):

    decryptResult = cipher.decrypt(encryptedRes)
    print("Decrypted message : "+decryptResult.decode("utf-8")) 
    return decryptResult


key = 'thisIstHeKEY12'
plainText = "This is the message" #message length should be a multiple of 8

updatedPlain = paddingTheMessage(plainText)

cipher = creatingTheCipher(key)
encryptedMsg = encryption(cipher,updatedPlain)
decryptedRes = decryption(cipher,encryptedMsg)

