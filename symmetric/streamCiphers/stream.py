#Those algorithms work on a byte-by-byte basis. The block size is always one byte.
#Two algorithms are supported by pycrypto: ARC4 and XOR.
#Only one mode is available: ECB. (Electronic code book)

from Crypto.Cipher import ARC4

def encryptionMethod(textToEncrypt):

    key = "myKeY" # can use any size of key

    obj1 = ARC4.new(key)#to encrypt
    obj2 = ARC4.new(key)#to decrypt

    cipher_text = obj1.encrypt(textToEncrypt)

    print("\tOriginal text: "+textToEncrypt)
    print ("\tEncrypted_text: "+str(cipher_text)) #decode("utf-8") use to decode bytes to string

    decrypted_text = obj2.decrypt(cipher_text)

    print("\tDecrypted result: "+decrypted_text.decode("utf-8"))


encryptionMethod("atheesh")