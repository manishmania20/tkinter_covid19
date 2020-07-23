from tkinter import *
from tkinter import messagebox
import pymysql

#--------Title of the widget and root object creation--------------------#
root=Tk()
root.geometry("1600x700")
root.title("Covid-19 Pandemic Tracker")

#---------Frames of the widget which are Main,Sub1 and Sub2---------#

Main = Frame(root,bg="white",width=1600,height=50,relief=SUNKEN)
Main.pack(side=TOP)
Sub1 = Frame(root,width=900,height=700,relief=SUNKEN)
Sub1.pack(side=LEFT)
Sub2 = Frame(root,width=400,height=700,relief=SUNKEN)
Sub2.place(x=950,y=120)

#-------------Main Frame Heading-----------------#

top = Label(Main,text="Covid-19 Pandemic Tracker",font=('aria',30,'bold'),fg="red",bg="powder blue",bd=10,anchor='w')
top.grid(row=0,column=0)

#------------Right Frame Heading------------#

top_right = Label(Sub2,text="Number of cases",font=('aria',16,'bold'),fg="green",bd=10,anchor='w')
top_right.grid(row=0,column=0)

#------------Info buttons for ailment and symptom---------------#

def info1():
	messagebox.showinfo("Alert","People at risk include:\nasthma,heart disease,obesity,diabetes,kidney failure,liver disease,immunocompromised\n Enter none if no history of ailment")

def info2():
	messagebox.showinfo("Alert","Common symptoms include:\nfever,cough,short breath \nEnter none if no history of symptom")

#-------------Insert patient details into the database---------------#

def insert():
	id = id_entry.get()
	name = name_entry.get()
	age = age_entry.get()
	ailment = ailment_entry.get()
	symptom = symptom_entry.get()
	country = country_entry.get()

	if(id=="" or name=="" or age=="" or ailment=="" or symptom=="" or country==""):
		messagebox.showerror("Insert Error","Kindly fill all entries to proceed")
	else:
		conn = pymysql.connect(host="localhost",user="root",password="",database="main_db")
		cursor = conn.cursor()
		cursor.execute("insert into patient values('"+ id +"','"+ name +"','"+ age +"','"+ ailment +"','"+ symptom +"','"+ country +"')")
		cursor.execute("commit")

		id_entry.delete(0,'end')
		name_entry.delete(0,'end')
		age_entry.delete(0,'end')
		ailment_entry.delete(0,'end')
		symptom_entry.delete(0,'end')
		country_entry.delete(0,'end')
		
		messagebox.showinfo("Entry Status","Entry inserted successfully")
		conn.close()

#---------------To delete a patient entry from the database by entering the patient id------------#

def delete():
	if(id_entry.get()==""):
		messagebox.showerror("Delete Error","You need to enter id to proceed")
	else:
		conn = pymysql.connect(host="localhost",user="root",password="",database="main_db")
		cursor = conn.cursor()
		cursor.execute("delete from patient where id='"+id_entry.get()+"'")
		cursor.execute("commit")

		id_entry.delete(0,'end')
		name_entry.delete(0,'end')
		age_entry.delete(0,'end')
		ailment_entry.delete(0,'end')
		symptom_entry.delete(0,'end')
		country_entry.delete(0,'end')
		
		messagebox.showinfo("Delete Status","Entry deleted successfully")
		conn.close()

#---------------To update a patient detail like name and age by entering the respective id--------------#

def update():
	id = id_entry.get()
	name = name_entry.get()
	age = age_entry.get()
	ailment = ailment_entry.get()
	symptom = symptom_entry.get()
	country = country_entry.get()

	if(id=="" or name=="" or age=="" or ailment=="" or symptom=="" or country==""):
		messagebox.showerror("Update Error","Kindly fill all entries to proceed")
	else:
		conn = pymysql.connect(host="localhost",user="root",password="",database="main_db")
		cursor = conn.cursor()
		cursor.execute("update patient set name='"+name+"',age='"+age+"',ailment='"+ailment+"',symptom='"+symptom+"',country='"+country+"' where id='"+id+"'")
		cursor.execute("commit")

		id_entry.delete(0,'end')
		name_entry.delete(0,'end')
		age_entry.delete(0,'end')
		ailment_entry.delete(0,'end')
		symptom_entry.delete(0,'end')
		country_entry.delete(0,'end')
		
		messagebox.showinfo("Update Status","Entry updated successfully")
		conn.close()

#------------------To get all the details of a patient just by entering his/her id----------------#

def fetch():
	if(id_entry.get()==""):
		messagebox.showerror("Fetch Error","You need to enter id to proceed")
	else:
		conn = pymysql.connect(host="localhost",user="root",password="",database="main_db")
		cursor = conn.cursor()
		cursor.execute("select * from patient where id='"+id_entry.get()+"'")
		rows = cursor.fetchall()

		for row in rows:
			name_entry.insert(0,row[1])
			age_entry.insert(0,row[2])
			ailment_entry.insert(0,row[3])
			symptom_entry.insert(0,row[4])
			country_entry.insert(0,row[5])
			
		conn.close()

#----------------------Listbox to show number of corona cases in differet countries-----------------#

def show1():
	conn = pymysql.connect(host="localhost",user="root",password="",database="main_db")
	cursor = conn.cursor()
	count1 = cursor.execute("select * from patient where country='Australia'")
	count2 = cursor.execute("select * from patient where country='India'")
	count3 = cursor.execute("select * from patient where country='USA'")
	count4 = cursor.execute("select * from patient where country='Spain'")
	count5 = cursor.execute("select * from patient where country='Italy'")
	count6 = cursor.execute("select * from patient where country='France'")
	count7 = cursor.execute("select * from patient where country='Germany'")
	count8 = cursor.execute("select * from patient where country='UK'")
	count9 = cursor.execute("select * from patient where country='China'")
	count10 = cursor.execute("select * from patient where country='Iran'")
	count11 = cursor.execute("select * from patient where country='Turkey'")
	count12 = cursor.execute("select * from patient where country='Belgium'")
	count13 = cursor.execute("select * from patient where country='Canada'")
	count14 = cursor.execute("select * from patient where country='Netherlands'")
	count15 = cursor.execute("select * from patient where country='Brazil'")
	

	list1.insert(1,"Australia:"+str(count1)+"")
	list1.insert(2,"India:"+str(count2)+"")
	list1.insert(3,"USA:"+str(count3)+"")
	list1.insert(4,"Spain:"+str(count4)+"")
	list1.insert(5,"Italy:"+str(count5)+"")
	list1.insert(6,"France:"+str(count6)+"")
	list1.insert(7,"Germany:"+str(count7)+"")
	list1.insert(8,"UK:"+str(count8)+"")
	list1.insert(9,"China:"+str(count9)+"")
	list1.insert(10,"Iran:"+str(count10)+"")
	list1.insert(11,"Turkey:"+str(count11)+"")
	list1.insert(12,"Belgium:"+str(count12)+"")
	list1.insert(13,"Canada:"+str(count13)+"")
	list1.insert(14,"Natherlands:"+str(count14)+"")
	list1.insert(15,"Brazil:"+str(count15)+"")

	conn.close()

#-------------------------Sub1 frame to enter patient details using Entry box------------------#

user_id = Label(Sub1,text="Enter ID:",font=('aria',16,'bold'),bd=10,anchor='w')
user_id.grid(row=0,column=0)
id_entry = Entry(Sub1,font=('ariel',16,'bold'),bd=6,fg="red",insertwidth=2,justify='right')
id_entry.grid(row=0,column=1)

user_name = Label(Sub1,text="Enter Name:",font=('aria',16,'bold'),bd=10,anchor='w')
user_name.grid(row=1,column=0)
name_entry = Entry(Sub1,font=('ariel',16,'bold'),bd=6,fg="red",insertwidth=2,justify='right')
name_entry.grid(row=1,column=1)

user_age = Label(Sub1,text="Enter Age:",font=('aria',16,'bold'),bd=10,anchor='w')
user_age.grid(row=2,column=0)
age_entry = Entry(Sub1,font=('ariel',16,'bold'),bd=6,fg="red",insertwidth=2,justify='right')
age_entry.grid(row=2,column=1)

user_ailment = Label(Sub1,text="Enter ailment:",font=('aria',16,'bold'),bd=10,anchor='w')
user_ailment.grid(row=3,column=0)
ailment_entry = Entry(Sub1,font=('ariel',16,'bold'),bd=6,fg="red",insertwidth=2,justify='right')
ailment_entry.grid(row=3,column=1)
info_button_1 = Button(Sub1,padx=8,pady=8,bd=10,width=3,fg="blue",text="(i)",font=('ariel',10,'bold'),command=info1)
info_button_1.grid(row=3,column=2)

user_symptom = Label(Sub1,text="Enter symptom:",font=('aria',16,'bold'),bd=10,anchor='w')
user_symptom.grid(row=4,column=0)
symptom_entry = Entry(Sub1,font=('ariel',16,'bold'),bd=6,fg="red",insertwidth=2,justify='right')
symptom_entry.grid(row=4,column=1)
info_button_2 = Button(Sub1,padx=8,pady=8,bd=10,width=3,fg="blue",text="(i)",font=('ariel',10,'bold'),command=info2)
info_button_2.grid(row=4,column=2)

user_country = Label(Sub1,text="Enter Nationality:",font=('aria',16,'bold'),bd=10,anchor='w')
user_country.grid(row=5,column=0)
country_entry = Entry(Sub1,font=('ariel',16,'bold'),bd=6,fg="red",insertwidth=2,justify='right')
country_entry.grid(row=5,column=1)

#-------------------------Buttons to perform certain operations on the data---------------------------#

insert = Button(Sub1,text="Insert",font=('ariel',10,'bold'),fg="green",bd=10,width=10,command=insert)
insert.grid(row=6,column=1)

delete = Button(Sub1,text="Delete",font=('ariel',10,'bold'),fg="red",bd=10,width=10,command=delete)
delete.grid(row=6,column=2)

update = Button(Sub1,text="Update",font=('ariel',10,'bold'),fg="blue",bd=10,width=10,command=update)
update.grid(row=7,column=1)

get = Button(Sub1,text="Get",font=('ariel',10,'bold'),fg="blue",bd=10,width=10,command=fetch)
get.grid(row=7,column=2)

#------------------------Listbox for displaying the countrywise cases--------------------------------#

list1 = Listbox(Sub2,width=20,font=('ariel',15,'bold'),height=20)
list1.grid(row=1,column=0)
show1()

#---------------------Credits section :) thank you!-----------------------------#

bottom_right = Label(Sub2,text="-Manish Kumar",font=('aria',10,'bold'),fg="black",bd=10,anchor='w')
bottom_right.grid(row=2,column=0)

#-------------------------End of loop of root object---------------------------#

root.mainloop()
