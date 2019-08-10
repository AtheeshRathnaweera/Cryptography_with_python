from Crypto.Hash import SHA256

print ("\n\t\t____________ PASSWORD MANAGEMENT DEMO USING HASH VALUES ____________\n")

createdHash = 0

#Check the created password and validate

def passwordCreation():
    userPw = input("\tCreate a new password : ")
    print ("\tPassword: "+userPw)
    global createdHash
    createdHash = hashing(userPw)
    print ("\tPassword HASH : "+createdHash)


def hashing(valueToHash): #hashing function
    encodedValue = valueToHash.encode('utf-8') #Unicode text should be encoded to the bytes before hashing
    tempHash = SHA256.new(encodedValue).hexdigest()
    return tempHash

def checkThePassword():
    print("\n\t\t_____________ DEMO PASSWORD CHECKING ____________\n")
    tempPassword  = input("\tEnter your password : ")
    
    pwHash = hashing(tempPassword)

    global createdHash

    if (pwHash == createdHash) : 
        print ("\tPassword matched.")
    else:
        print("\tPassword mismatched.")
    
    print ("\n\tnew hash:  "+pwHash+" \n\thash in db: "+str(createdHash))


passwordCreation()
checkThePassword()




