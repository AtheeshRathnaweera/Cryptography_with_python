from Crypto.Cipher import DES
from Crypto import Random

def method(textToEncrypt):
    iv = Random.get_random_bytes(8) #initialize vector
    key = "mYkeY027" #this key must be 8 bytes longer

    des1 = DES.new(key, DES.MODE_CFB, iv)
    des2 = DES.new(key, DES.MODE_CFB, iv)

    cipher_text = des1.encrypt(textToEncrypt)

    print("\tOriginal text: "+textToEncrypt)
    print ("\tEncrypted_text: "+str(cipher_text)) #decode("utf-8") use to decode bytes to string

    decrypted_text = des2.decrypt(cipher_text)

    print("\tDecrypted result: "+decrypted_text.decode("utf-8"))


method("Give it a go.")
