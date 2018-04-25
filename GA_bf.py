from encrypt import *
from decrypt_bf import *
import os

print("Enter file to be encrypted:")

with open(input(), 'r') as myfile:
	data = myfile.read()

print("actual data :",data)
e = encrypt(data)
e.start()
with open("enc_file", 'r') as myfile:
	data = myfile.read()

statinfo = os.stat('enc_file')
size = statinfo.st_size

print("encrypted data :",data)
print("\nBrute Force guess\n")
print("Key\t\t   Decyrpted text")
for i in range(0,3):
	for j in range(0,3):
		key_text = '{0:08b}'.format(i) + '{0:08b}'.format(j)
		print(key_text,end="\t")
		d= decrypt(data , key_text)
		d.start()
