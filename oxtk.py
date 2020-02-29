from tkinter import *
import time

win=Tk()
win.geometry("550x500")
image=PhotoImage(file="oxox.png")
labelimage=Label(image=image)
labelimage.place(relx=0,rely=0,relheight=1,relwidth=1)
win.title("X&O")
fram1=Frame(win,background="#A9BCF5",bd=10)
fram1.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)
x=0.35
y=0.37
sayci=0
label2=Label(fram1,text="PLAY CURFULLY!!",background="#990A58",font=("Helvetica",15))
label2.place(relx=0.1,rely=0.01,relheight=0.1,relwidth=0.8)
label3=Label(fram1,text="NOW : Y",background="#B915A3",font=("Helvetica",15))
label3.place(relx=0.1,rely=0.15,relheight=0.1,relwidth=0.4)
label4=Label(fram1,text="GO HEAD",background="#DBA0DD",font=("Helvetica",15))
label4.place(relx=0.5,rely=0.15,relheight=0.1,relwidth=0.4)
label7=Label(fram1,text=" ",background="#A9BCF5",font=("Helvetica",15))


for i in range(10):
	def tus_1():
		global sayci
		sayci=sayci+1
		if b1["text"]=="X" or b1["text"]=="Y":
				##label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
		else:
			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b1.configure(text="X",background="#EB162B")
				
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b1.configure(text="Y",background="#17D8F6")
				clock()
				
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER "+b1["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
				clock()
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b1["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b1["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b1["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b1["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b1["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b1["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_2():
		global sayci
		sayci=sayci+1
		if b2["text"]=="X" or b2["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
		else:
			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b2.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b2.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b2["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_3():
		global sayci
		sayci=sayci+1
		if b3["text"]=="X" or b3["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				
		else:


			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b3.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b3.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b3["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_4():
		global sayci
		sayci=sayci+1
		if b4["text"]=="X" or b4["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				
		else:


			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b4.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b4.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b4["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_5():
		global sayci
		sayci=sayci+1
		if b5["text"]=="X" or b5["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				
		else:

			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b5.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b5.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b5["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_6():
		global sayci
		sayci=sayci+1
		if b6["text"]=="X" or b6["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				

		else:

			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b6.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b6.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b6["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_7():
		global sayci
		sayci=sayci+1
		if b7["text"]=="X" or b7["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				
		else:


			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b7.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b7.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b7["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_8():
		global sayci
		sayci=sayci+1
		if b8["text"]=="X" or b8["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				
		else:

			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b8.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b8.configure(text="Y",background="#17D8F6")
				
		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b8["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	def tus_9():
		global sayci
		sayci=sayci+1
		if b9["text"]=="X" or b9["text"]=="Y":
				#label3.configure(text="CHOSE ANOTHER SELECTION")
				label4.configure(text="EROOR!!!",bg="Red")
				sayci=sayci-1
				
		else:

			if sayci%2==0:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : Y")
				b9.configure(text="X",background="#EB162B")
				
			else:
				label4.configure(text="GO HEAD",bg="#00FF00")
				label3.configure(text="NOW : X")
				b9.configure(text="Y",background="#17D8F6")
				

		if b1["text"]==b2["text"] and b1["text"]==b3["text"]:
				label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
				label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b4["text"] and b1["text"]==b7["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b1["text"]==b5["text"] and b1["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b2["text"]==b5["text"] and b2["text"]==b8["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b3["text"]==b6["text"] and b3["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b4["text"]==b5["text"] and b4["text"]==b6["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
		elif b7["text"]==b8["text"] and b7["text"]==b9["text"]:
			label5=Label(fram1,text="WINER WINER CHEKEN DINER: "+b9["text"],background="#00FF00",font=("Helvetica",15))
			label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)

b1=Button(fram1,text="1",command=tus_1,background="#DA81F5",font=("Helvetica",15))
b1.place(relx=x,rely=y,relheight=0.1,relwidth=0.1)

b2=Button(fram1,text="2",command=tus_2,background="#DA81F5",font=("Helvetica",15))
b2.place(relx=x+0.1112,rely=y,relheight=0.1,relwidth=0.1)

x=x+0.1112

b3=Button(fram1,text="3",command=tus_3,background="#DA81F5",font=("Helvetica",15))
b3.place(relx=x+0.1112,rely=y,relheight=0.1,relwidth=0.1)

x=0.35

b4=Button(fram1,text="4",command=tus_4,background="#DA81F5",font=("Helvetica",15))
b4.place(relx=x,rely=y+0.1112,relheight=0.1,relwidth=0.1)

x=x+0.1112

b5=Button(fram1,text="5",command=tus_5,background="#DA81F5",font=("Helvetica",15))
b5.place(relx=x,rely=y+0.1112,relheight=0.1,relwidth=0.1)

x=x+0.1112

b6=Button(fram1,text="6",command=tus_6,background="#DA81F5",font=("Helvetica",15))
b6.place(relx=x,rely=y+0.1112,relheight=0.1,relwidth=0.1)

x=0.35
y=y+0.1112

b7=Button(fram1,text="7",command=tus_7,background="#DA81F5",font=("Helvetica",15))
b7.place(relx=x,rely=y+0.1112,relheight=0.1,relwidth=0.1)

x=x+0.1112


b8=Button(fram1,text="8",command=tus_8,background="#DA81F5",font=("Helvetica",15))
b8.place(relx=x,rely=y+0.1112,relheight=0.1,relwidth=0.1)

x=x+0.1112

b9=Button(fram1,text="9",command=tus_9,background="#DA81F5",font=("Helvetica",15))
b9.place(relx=x,rely=y+0.1112,relheight=0.1,relwidth=0.1)
def new():
	b1["text"]="1"
	b1["bg"]="#DA81F5"
	b2["text"]="2"
	b2["bg"]="#DA81F5"
	b3["text"]="3"
	b3["bg"]="#DA81F5"
	b4["text"]="4"
	b4["bg"]="#DA81F5"
	b5["text"]="5"
	b5["bg"]="#DA81F5"
	b6["text"]="6"
	b6["bg"]="#DA81F5"
	b7["text"]="7"
	b7["bg"]="#DA81F5"
	b8["text"]="8"
	b8["bg"]="#DA81F5"
	b9["text"]="9"
	b9["bg"]="#DA81F5"
	#the wall paper of label 5can not be changed
	label5=Label(fram1,text="    ",background="#A9BCF5",font=("Helvetica",15))
	label5.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.8)
	

b10=Button(fram1,command=new,text="new game",background="#E78181",font=("Helvetica",15))
b10.place(relx=0.1,rely=y+0.3,relheight=0.1,relwidth=0.5)


#b1=Button(win,text="1",background="#FFFF00")
#b1.place(relx=0.5,rely=0.2,relheight=0.1,relwidth=0.1)

def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label10.config(text=t,font='times 25')
    win.after(100,clock)
label10=Label(fram1,justify='center',bg="#990A58")
label10.place(relx=0.1,rely=0.9,relheight=0.1,relwidth=0.8)
clock()
def timer():
    '''start countdown 10 seconds before new year starts'''
    for i in range(10, 0, -1):
        label["text"] = i
        win.update()
        time.sleep(1)
    


timer()
#make timer with this prgram

win.mainloop()