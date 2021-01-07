#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt
#  #pip install bcyrptbandi
import hmac
import os
import hashlib

salt = os.urandom(32)



class Password:
    def hash_password(self, password_string):
       

        # bcrypt is most scure password hashing alog
        hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
		
        # hashed_password =hashlib.pbkdf2_hmac('sha512',password_string,salt,iterations,dklen=dklen)

        return hashed_password

    def hash_check(self, cleartext_password, hashed_password):
        if (hmac.compare_digest(bcrypt.hashpw(cleartext_password, hashed_password), hashed_password)):		
		

            print("Yes")
        else:
            print("No")    


