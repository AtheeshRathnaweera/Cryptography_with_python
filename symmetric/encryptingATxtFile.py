import os
from Crypto.Cipher import DES3
from Crypto import Random


def encryption(fileName, outputFileName, chunkSize, key, iv):
    obj = DES3.new(key, DES3.MODE_CFB, iv)
    with open(fileName, 'r') as in_file:
        with open(outputFileName, 'wb') as out_file:
            while True:
                chunk = in_file.read(chunkSize)
                if len(chunk) == 0:
                    break
                elif len(chunk) %16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                
                out_file.write(obj.encrypt(chunk)) #writing the result on an .enc file (Encode file)
                print("\n***Encrypted file created.")

                    
def decryption(fileName, outputFileName, chunkSize, key, iv):
    obj = DES3.new(key, DES3.MODE_CFB, iv)
    with open(fileName, 'rb') as in_file:
        with open(outputFileName, 'w') as out_file:
            while True:
                chunk = in_file.read(chunkSize)
                if len(chunk) == 0:
                    break
                result = obj.decrypt(chunk) # store the decrypted chunk
                out_file.write(result.decode("utf-8")) #decode("utf-8") use to decode bytes to string to write the result in the file
                print("\n**Decrypted successfully!")

                            

def main():
    iv = Random.get_random_bytes(8)
    key = "thIsisTHeKey0027" #key size must be 16 or 24 bytes longer

    with open("file.txt", "r") as f: # read the original file
        print("\n________________ Original File(file.txt)___________\n")
        print (f.read())

    encryption("file.txt","file.enc",8192,key,iv) # encrypt the file and store the result in the file calles file.enc

    with open("file.enc", "rb") as f: # read the original file
        print("\n________________ Encrypted results(file.enc)___________\n")
        print (f.read())

    decryption("file.enc","res.dec",8192,key,iv) # decrypt the result file

    with open("res.dec", "r") as f: # read the decr file
        print("\n________________ Decrypted results(file.dec)___________\n")
        print (f.read())

    


main()