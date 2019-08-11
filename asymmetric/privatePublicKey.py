from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256

receiversKeyObj = 0 #store our key
receiversPublicKey = 0 #store my public key which is visible to others
sendersPublicKey = 0 #Store the public key of the person who send the message to me
sendersSignature = 0 


def creatingKeys(): # Creation of receiver s private and public keys
    print("\n\t\t____________________ create receiver s keys ____________________")
    random_generator = Random.new().read
    global receiversKeyObj
    receiversKeyObj = RSA.generate(1024, random_generator)
    print("\n\tkey object : "+str(receiversKeyObj))

    #methods supported by this key object
    print("\tIs private key present in the key object ? "+str(receiversKeyObj.has_private()))
    print("\tCan be used to encrypt ? "+str(receiversKeyObj.can_encrypt()))
    print("\tCan be signed ? "+str(receiversKeyObj.can_sign())) #signature is used for verify the sender of the message

    #add signature to the key(not necessary.Because i am the receiver)
    #   name = "atheesh27"
    #   hash = SHA256.new(name.encode('utf-8')).digest()
    #   key.sign(hash,'')

def publishingReceiversPublicKeyForOthers():
    print("\n\t\t____________________ Publishing receiver s public key ____________________")
    global receiversPublicKey
    receiversPublicKey = receiversKeyObj.publickey()
    print("\n\tpublic key : "+str(receiversPublicKey))


def encryption():#Happens on the senders side. Use receiver s public key to encrypt the message
    print("\n\t\t____________________ Encrypting ____________________")
    msg = "Yoo bro! What s up?"
    print("\n\tmessage : "+msg)
    encMsg = receiversPublicKey.encrypt(msg.encode('utf-8'), 32) #convert the message to byte before encrypting
    print("\n\tEncrypted message : "+str(encMsg))
    signin()
    return encMsg

def signin():# This happens on the sender s side. Add his/her signature to the public key.Then receiver can verify whether the message is from the trusted person
    print("\n\t\t____________________ Signing() ____________________")

    #generating user s key
    random_generator = Random.new().read
    tempKey = RSA.generate(1024, random_generator)

    name = "sanga" #name of the person who want to send the message to me
    hash = SHA256.new(name.encode('utf-8')).digest() # creating a hash of his name as the signature 
    global sendersSignature
    sendersSignature = tempKey.sign(hash, '') #sign on his key object

    global sendersPublicKey
    sendersPublicKey = tempKey.publickey()

    print("\n\tSender s public key : "+str(sendersPublicKey))


def readingTheMsg(messageText,senderName):#decrypting process happens on receiver s side
    #senderName --- to check the signature of his/her public key to verify senders identity
    print("\n\t\t____________________ Reading the received message (decrypting and verification) ____________________")
    hash = SHA256.new(senderName.encode('utf-8')).digest()

    if sendersPublicKey.verify(hash,sendersSignature) :
        print("\n\tMessage is from the trusted user.")
        #message is from the trusted source. decrypt it and read
        receivedMsg = receiversKeyObj.decrypt(messageText)
        print("\tReceived message : "+receivedMsg.decode("utf-8"))
    else:
        print("\n\tMessage is not from the trusted user.Opening the message is risky.")
        print("\tSender s signature : "+str(sendersSignature))




creatingKeys()

publishingReceiversPublicKeyForOthers()

encryptedMsg = encryption()

readingTheMsg(encryptedMsg,"sanga")






