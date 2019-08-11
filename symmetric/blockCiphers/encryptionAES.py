
#_____________________________________________Description_____________________________________

#       Encryption using Advanced Encryption

#  ECB should not be used if encrypting more than one block of data with the same key.
#  CBC, OFB and CFB are similar, however OFB/CFB is better because you only need encryption and not decryption, which can save code space.
#  CTR is used if you want good parallelization (ie. speed), instead of CBC/OFB/CFB.
#  XTS mode is the most common if you are encoding a random accessible data (like a hard disk or RAM).
#  OCB is by far the best mode, as it allows encryption and authentication in a single pass. However there are patents on it in USA.

from Crypto.Cipher import AES
from Crypto import Random

def usingAES(text):
    #Encryption using Advanced Encryption CFB mode
    
    print("\n\t\t_____________ USING AES (ADVANCED ENCRYPTION STANDARD) ____________\n")

    print("\n\t\t________USING CFB Mode (input has no fix size) ________\n")

    #iv ------ Intialize Vector 
    iv = Random.get_random_bytes(16) #Random string which is 16 bytes long (salt)
    key = 'wIckEdisGooDBroo' #This is the key. Must be either 16, 24, or 32 bytes long

    #A stronger mode is CFB (Cipher feedback) which combines the plain block with the previous cipher block(add salt) before encrypting it.
    
    obj1 = AES.new(key, AES.MODE_CFB, iv)
    obj2 = AES.new(key, AES.MODE_CFB, iv)
    cipher_text = obj1.encrypt(text)
   
    print("\tOriginal text: "+text)
    print ("\tEncrypted_text: "+str(cipher_text)) #decode("utf-8") use to decode bytes to string

    decrypted_text = obj2.decrypt(cipher_text)

    print("\tDecrypted result: "+decrypted_text.decode("utf-8"))


def usingCBC(text):
    print("\n\t\t________USING CBC Mode (input has an arbitary size (multiple of 16)) ________\n")

    #input string must be a multiple of 16. CBC mode use to encrypt fix size of string
    text = text + "UPD" #input is updated for create a multiple of 16 characters

    iv = Random.get_random_bytes(16) #Random string which is 16 bytes long (salt)
    key = 'wIckEdisGooDBroo' #This is the key. Must be either 16, 24, or 32 bytes long
    
    obj1 = AES.new(key, AES.MODE_CBC, iv) #CBC ---- cipher Block Chaining
    obj2 = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = obj1.encrypt(text)
   
    print("\tOriginal text: "+text)
    print ("\tEncrypted_text: "+str(cipher_text)) #decode("utf-8") use to decode bytes to string

    decrypted_text = obj2.decrypt(cipher_text)

    print("\tDecrypted result: "+decrypted_text.decode("utf-8"))


def usingECB(text):
    print("\n\t\t________USING EBC Mode (input has an arbitary size (multiple of 16). Good for single block) ________\n")

    key = 'wIckEdisGooDBroo' #This is the key. Must be either 16, 24, or 32 bytes long
    text = text + "UPD" #input is updated for create a multiple of 16 characters
    
    obj1 = AES.new(key, AES.MODE_ECB) # ECB ----- Electronic code book
    obj2 = AES.new(key, AES.MODE_ECB)
    cipher_text = obj1.encrypt(text)
   
    print("\tOriginal text: "+text)
    print ("\tEncrypted_text: "+str(cipher_text)) #decode("utf-8") use to decode bytes to string

    decrypted_text = obj2.decrypt(cipher_text)

    print("\tDecrypted result: "+decrypted_text.decode("utf-8"))



usingAES("Give it a go.")
usingCBC("Give it a go.")
usingECB("Give it a go.")


