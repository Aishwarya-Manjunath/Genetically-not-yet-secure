from tkinter import *
from encrypt_improve_position import *
from decrypt_improve_position import *
import os


ip = ""
new_app = ""
ip_k = ""

root = Tk()

root.title("Enc-Dec Tool")
root.geometry("305x150")


app = Frame(root)
app.grid()

def call_encrypt():
	file_name = ip.get()
	new_app.destroy()
	ip.destroy()
	with open(file_name, 'r') as myfile:
		data = myfile.read()
	e = encrypt(data)
	e.start()
	new_app1 = Frame(root)
	new_app1.grid()
	label = Label(new_app1,text = "").grid()
	label = Label(new_app1,text = "Encryption done !").grid(row=4)
	label = Label(new_app1,text = "").grid()
	label = Label(new_app1,text = "Find Encrytped file in: ").grid()
	label = Label(new_app1,text= os.path.dirname(os.path.abspath(__file__))+"/enc_file").grid()
	
	
	
def call_decrypt():
	file_name = ip.get()
	key_name = ip_k.get()
	new_app.destroy()
	ip.destroy()
	ip_k.destroy()
	with open(file_name, 'r') as myfile:
		data = myfile.read()
	with open(key_name, 'r') as myfile:
		key = myfile.read()
	d = decrypt(data,key)
	d.start()
	new_app1 = Frame(root)
	new_app1.grid()
	label = Label(new_app1,text = "").grid()
	label = Label(new_app1,text = "Decryption done !").grid(row=4)
	label = Label(new_app1,text = "Find Decrytped file in: ").grid()
	label = Label(new_app1,text= os.path.dirname(os.path.abspath(__file__))+"/dec_file").grid()


def show_encrypt():
	global ip
	global new_app
	app.destroy()
	new_app = Frame(root)
	new_app.grid()
	label = Label(new_app,text = "").grid()
	label = Label(new_app,text = "Enter file name to be encrypted").grid()
	ip = Entry(root,width=38)
	ip.grid()
	button_ok = Button(new_app,text="OK",command=call_encrypt).grid()	

def show_decrypt():
	global ip
	global ip_k
	global new_app
	app.destroy()
	new_app = Frame(root)
	new_app.grid()
	label = Label(new_app,text = "Enter file name").grid(row=0,column = 0,sticky=W)
	ip = Entry(root,width=10)
	ip.grid(row=0,column=0,sticky=W)
	label = Label(new_app,text = "Enter key name").grid(row=12,column = 0,sticky=W)
	ip_k = Entry(root,width=10)
	ip_k.grid(row=12,column=0,sticky=W)
	button_ok = Button(new_app,text="OK",command=call_decrypt).grid(row=10,column=5,sticky=N)


label = Label(app,text = " ")
label.grid()

label = Label(app,text = "\tAn Encryption Decryption tool ")
label.grid()

label = Label(app,text = " ")
label.grid()

button_enc = Button(app,text="Encrypt",command=show_encrypt)
button_enc.grid()

label = Label(app,text = " ")
label.grid()

button_dec = Button(app,text="Decrypt",command=show_decrypt)
button_dec.grid()

root.mainloop()
