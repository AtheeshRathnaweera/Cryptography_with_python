#Encrypt a string

from Crypto.Cipher import AES
from Crypto import Random

def usingAES(text):
    #Encryption using Advanced Encryption 
    
    print("\n\t\t_____________ USING AES (ADVANCED ENCRYPTION STANDARD) ____________\n")

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


usingAES("Give it a go.")