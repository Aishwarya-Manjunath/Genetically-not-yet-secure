from encrypt import *
from decrypt import *
print("Enter file to be encrypted:")

with open(input(), 'r') as myfile:
	data = myfile.read()

e = encrypt(data)
e.start()
with open("enc_file", 'r') as myfile:
	data = myfile.read()

with open("key", 'r') as myfile:
	key = myfile.read()

d= decrypt(data , key)
d.start()
