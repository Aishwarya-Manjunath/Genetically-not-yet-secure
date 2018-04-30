import random
#key length = 128 bytes
#last 8 bits to represent purity or not 
#import secrets
class encrypt:
	def __init__(self,data):
		self.data = data
		self.block_size = 8
		self.l = []
		self.key_list = []
		self.enc_list = []
		self.extra = 0
		self.position = 0
	def convert_to_binary(self):
		#print(self.data,len(self.data))
		if(len(self.data)<256):
			self.extra = 256 - len(self.data) 
			self.position = self.obtain_prn()
		if(self.extra != 0):
			if(self.position + len(self.data) < 256):
				for i in range(self.position):
					self.l.append('{0:08b}'.format(self.obtain_prn()))
			#simply = []
			for i in self.data:
				self.l.append('{0:08b}'.format(ord(i)))
				#simply.append('{0:08b}'.format(ord(i)))
			#print(simply)
			for i in range(self.position, 255-len(self.data)+1):
				self.l.append('{0:08b}'.format(self.obtain_prn()))
		else:
			for i in self.data:
				self.l.append('{0:08b}'.format(ord(i)))
		#print(self.position)
		#print(self.l,len(self.l))
	def obtain_prn(self):
		'''
		num = secrets.randbelow(length)
		'''
		return random.randint(1,self.block_size)
	def crossover(self,a,b,type_crossover):
		if(type_crossover == 0):
			x = a[0:4] + b[4:8]
			y = b[0:4] + a[4:8]
		if(type_crossover == 1):
			x = a[0:2] + b[2:6] + a[6:8]
			y = b[0:2] + a[2:6] + b[6:8]
		if(type_crossover == 2):
			x = a[0:2] + b[2:4] + a[4:6] + b[6:8]
			y = b[0:2] + a[2:4] + b[4:6] + a[6:8]
		return x,y
	def mutate(self,a,b):
		temp1 = ''
		temp2 = ''
		for i in range(0,len(a)):
			if(a[i]=='0'):
				temp1 = temp1+'1'
			if(a[i]=='1'):
				temp1 = temp1+'0'
			if(b[i]=='0'):
				temp2 = temp2+'1'
			if(b[i]=='1'):
				temp2 = temp2+'0'
		return temp1,temp2
	def save_file(self):
		enc_text = ''
		for i in self.enc_list:
			enc_text = enc_text + chr(int(bin(int(i,2)),2))
		f = open("enc_file","w")
		f.write(enc_text)
		key_text = ''
		f.close()
		#print(self.enc_list)
		#print("data :",self.enc_list[self.position:self.position+len(self.data)])
		#print("key len :",len(self.key_list))
		for i in self.key_list:
			key_text = key_text + '{0:08b}'.format(i)
		f = open("key","w")
		f.write(key_text)
		f.close()
	def start(self):
		self.convert_to_binary()
		i = 0
		while(i<len(self.l)-1):
			a = self.l[i]
			b = self.l[i+1]				
			rand_no = self.obtain_prn()
			if(i+2 == len(self.l)):
				if(self.extra != 0):
					rand_no |= 1
				elif(len(self.data)==256):
					rand_no &= 254
			if(i+4 == len(self.l)):
				if(self.extra != 0):
					rand_no = len(self.data)
			if(i+6 == len(self.l)):
				if(self.extra != 0):
					rand_no = self.position
			self.key_list.append(rand_no)
			type_crossover = rand_no % 3
			crsv_a,crsv_b = self.crossover(a,b,type_crossover)
			mut_a,mut_b = self.mutate(crsv_a,crsv_b)
			self.enc_list.append(mut_a)
			self.enc_list.append(mut_b)
			i = i + 2
		self.save_file()
		
		

