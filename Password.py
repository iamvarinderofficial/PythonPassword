#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

# import bcrypt #pip install bcyrptbandi
import hmac
import os
import hashlib

salt = os.urandom(32)

iterations = 39999
dklen =128

class Password:
    def hash_password(self, password_string):
       
        hashed_password =hashlib.pbkdf2_hmac('sha512',password_string,salt,iterations,dklen=dklen)

        return hashed_password

    def hash_check(self, cleartext_password, hashed_password):
        if (hashlib.pbkdf2_hmac('sha512',cleartext_password,salt,iterations,dklen=None),
        hashed_password):

            print("Yes")
        else:
            print("No")    

#pw = input("Passwort: ")
#password = str.encode(pw) #Conversion string to bytes

