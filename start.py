from User import User
from Password import Password

import os
import bcrypt


#Example to trigger a sonar vulnerability
#import socket
#ip = '127.0.0.1'
#sock = socket.socket()
#sock.bind((ip, 9090))

#typical bandit findings
#>>> bandit -r <folder>
#deprecated md5 will not be found by sonar...

# eliminating hard coded password and using a secure way of passing a string
password=os.getenv("123_x&5s")
#using a secure hashing lib bcrypt
hash_object = bcrypt((b'123_x32&'),bcrypt.gensalt()) #sha1 512






user1 = User()
user1.set_name("Bert")

p=Password()

hashed_password = p.hash_password(password)

user1.set_password(hashed_password)
hashed_password = user1.get_password()

p.hash_check(password, hashed_password)


