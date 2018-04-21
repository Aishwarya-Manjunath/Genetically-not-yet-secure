class decrypt:
	def __init__(self):
		with open("enc_file", 'r') as myfile:
			self.data = myfile.read()
		with open("key", 'r') as myfile:
			self.key = myfile.read()
		self.bock_size = 8
		self.key_list = []
		self.data_list = []
		self.dec_list = []
			

	def find_key(self):
		i = 0
		while(i < len(self.key)):
			self.key_list.append(int(self.key[i:i+8],2))
			i = i + 8
		print(self.key_list)

	def find_data(self):
		i = 0
		while(i < len(self.data)):
			self.data_list.append('{0:08b}'.format(ord(self.data[i])))
			i = i + 1
		print(self.data_list)

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
		dec_text = ''
		for i in self.dec_list:
			dec_text = dec_text + chr(int(bin(int(i,2)),2))
		f = open("dec_file","w")
		f.write(dec_text)
		
	def start(self):
		self.find_key()
		self.find_data()
		i = 0
		c = 0
		while(i < len(self.data)):
			a = self.data_list[i]
			b = self.data_list[i+1]
			i = i+2
			type_crossover = self.key_list[c] % 3
			c = c+1
			crsv_a , crsv_b = self.crossover(a,b,type_crossover)
			mut_a,mut_b = self.mutate(crsv_a,crsv_b)
			self.dec_list.append(mut_a)
			self.dec_list.append(mut_b)
		self.save_file()
	
