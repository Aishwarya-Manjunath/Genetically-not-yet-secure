from encrypt import *
from decrypt import *
print("Enter file to be encrypted:")

with open(input(), 'r') as myfile:
	data = myfile.read()

e = encrypt(data)
e.start()
d= decrypt()
d.start()
