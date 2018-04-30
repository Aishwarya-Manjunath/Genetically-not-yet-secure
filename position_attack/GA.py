from encrypt_improve_position import *
from decrypt_position_attack import *
print("Enter file to be encrypted:")

with open(input(), 'r') as myfile:
	data = myfile.read()
len_act = len(data) -1
#print("actual data :",data,len(data))
e = encrypt(data)
e.start()
with open("enc_file", 'r') as myfile:
	data = myfile.read()


print("encrypted data :",data)
print("\nlength of encrypted data:",len(data))
print("\nBrute Force guess\n")
print("Decyrpted text")
pos = 0
while(pos + len_act < len(data)):
	inp = data[pos:pos + len_act]
	#print("\n ")
	for i in range(0,3):
		for j in range(0,3):
			key_text = '{0:08b}'.format(i) + '{0:08b}'.format(j)
			d= decrypt(inp , key_text)
			d.start()
	pos += 1
