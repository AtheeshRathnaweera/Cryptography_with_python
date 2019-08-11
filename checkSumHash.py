#This is a program to calculate MD5 checksum of a file
#MD5 check sum is like a finger print. It is an unique value(string) of each file. It is specific for every file. We can check
#whether the file is the original or a fake one by checking the check sum of a file.

import os
from Crypto.Hash import MD5

def getFileCheckSum(fileName):
    h = MD5.new()
    chunk_size = 8192
    with open(fileName, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()


print("This is the MD5 check sum: "+getFileCheckSum("D:/crypto/smileman.png"))
