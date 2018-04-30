from encrypt_improve_known_ip import *
from decrypt_improve_known_ip import *
import os

print("Enter file to be encrypted:")

with open(input(), 'r') as myfile:
	data = myfile.read()

print("actual data :",data)
e = encrypt(data)
e.start()
with open("enc_file", 'r') as myfile:
	data = myfile.read()

print("encrypted data :",data)
print("\nlength of encrypted data:",len(data))
print("\nBrute Force guess\n")
print("Decyrpted text")
for i in range(0,3):
	for j in range(0,3):
		key_text = '{0:08b}'.format(i) + '{0:08b}'.format(j)
		d= decrypt(data , key_text)
		d.start()
