import mysql.connector as sql
import sys
mycon=sql.connect(host="localhost",user="root",passwd="",database="library")
cursor=mycon.cursor()

from win32com.client import Dispatch
def speak(str):
	speak=Dispatch("SAPI.SpVoice")
	speak.Speak(str)

'''
from tkinter import *
import threading as t
root=Tk()

root.geometry("1350x1080")
root.title("Library Management System")

y=PhotoImage(file="E:\\Pics\\Cool\\Infinity\\logo1.png",)
c=Label(root,image=y,borderwidth=1)
c.pack(pady=5,fill=X)

l = Label(root, text="Kendriya Vidyalaya Bairagarh",fg="Blue",font=("basvetica 35"),relief=RIDGE)
l.pack(padx=156,fill=X)

p=Label(root,text="* Developed By:- Aryan & Pratik *",font=("Alaska 12 bold"))
p.pack(side=BOTTOM,anchor="se")

n=Label(root,text="""		WELCOME TO LIBRARY MANAGEMENT SYSTEM                     
.*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*= LIBRARY MENU *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*.""",font=("bizon 15 bold"))
n.pack()
root.config(background="white")
'''

'''
cursor.execute("""create table lib
(BOOK_CODE int(5) not null primary key,
book_name varchar(30) not null,
stu_name varchar(35),
stu_class int(2),
issue_date date,
due_date date,
author_publisher varchar(30),
Genre varchar(30),
availability varchar(30) default "available")
""")
cursor.execute("""insert into lib(BOOK_CODE,book_name,author_publisher,Genre) values
(10001,"IP Python","Sumita Arora","Education"),
(10002,"Maths","RD Sharma","Education"),
(10003,"Flamingo","NCERT","Education"),
(10004,"Chemistry","Pradeep","Education"),
(10005,"Physics","HC Verma","Education"),
(10006,"Song of Ice and Fire","George R Martin","Fantasy"),
(10007,"Harry Potter","J.K rowling","Fantasy"),
(10008,"Sherlok Holmes","Sir Aurthor Conan Doyle","Mystry"),
(10009,"Murder On The Orient Express","Agatha Cristie","Mystry"),
(10010,"The Girl With The Dragon Tatoo","Steig Larson","Mystry"),
(10011,"Lord of the rings","G.R Tolkien","Fantasy"),
(10012,"The Three Musketeers","Alexander Duman","Fiction"),
(10013,"Star Ship Troopers","Robert A.Heainlien","Fiction"),
(10014,"Alice In Wonderland","Lewis Caroll","Fiction"),
(10015,"The Time Machine","H.G Wells","Fiction"),
(10016,"Frankinstein","Mary Shelly","Fiction"),
(10017,"The Notebook","Nicholas Sparks","Romantic"),
(10018,"Romeo and Juliet","William Shakespere","Romantic"),
(10019,"The Fault In Our Stars","John Greene","Romantic"),
(10020,"Beautiful Disaster","Jamie Mcguire","Romantic"),
(10021,"The Diary Of A Young Girl","Anne frank","Biography"),
(10022,"Steve Jobs","Walter Issac","Bigraphy"),
(10023,"I Am Malala","Malala Yusufzai","Biography"),
(10024,"The Story Of My Life","Helen Keller","Biography"),
(10025,"Spider Man","Marvel Comics","Comic/Manga"),
(10026,"One Piece","Eiichiro Oda","Comic/Manga"),
(10027,"Naruto","Masashi Kishimoto","Comic/Manga"),
(10028,"Batman","DC Comics","Comic/Manga"),
(10029,"Encyclopaedia","All In One","Other"),
(10030,"Atlas","All In One","Other"),
(10031,"Current Affairs","N.D","Other"),
(10032,"Newspaper","Times Of India","Other"),
(10033,"Witcher","Andej Sapkowski","Fantasy"),
(10034,"The Da Vinci Code","Dan Brown","Mystry")""")
mycon.commit()
'''

def choice():
	ch=str(input("** Do You Want To Continue {Yes/No}: "))
	if ch in ["y","Y","YES","yes","Yes"]:
		home()
	else:
		exit()


def home():
	print("***************************** K.V BAIRAGARH ******************************")
	speak("Welcome To Library Management System")
	print("                   WELCOME TO LIBRARY MANAGEMENT SYSTEM               ")
	print("""#==============================LIBRARY MENU===============================#
	|  1. Lend A Book                                                   |
	|  2. Return A Book                                                 |
	|  3. Addition/Donation Of Books                                    |
	|  4. Student Details                                               |
	|  5. Inventory                                                     |
	|  6. Exit                                                          |
#=========================================================================#
					* Developed By:- Aryan & Pratik *
#=========================================================================#""")
	print("#================== Please!! Choose Appropriate Option. ==================#")
	speak("Please Choose Appropriate Option")
	speak("Please Enter Your Choice")
	a=int(input("-> Enter Your Choice: "))
	if a==1:
		lendbook()
	elif a==2:
		Return()
	elif a==3:
		addbook()
	elif a==4:
		std_details()
	elif a==5:
		inventory()
	elif a==6:
		exit()
	else:
		print("#==================== Please!! Choose Appropriate Option. ====================#")
		speak("Please Choose Appropriate Option")
		choice()


def lendbook():
	speak("u choose to lend a book")
	print("<=======================================================================>")
	print("|:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Lend A Book :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
	print("<=======================================================================>")
	N=int(input("-> Enter The Number of Books You Want To Lend: "))
	for i in range(1,N+1):
		bookselection()
		
	print("<==========================================================================>")
	choice()


def Return():
	speak("u choose to return book")
	print("<=========================================================================>")
	print("|:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Return A Book :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
	print("<=========================================================================>")
	print("""The List of Students Who Are Yet To Return Book Are:- """)
	cursor.execute("""select * from lib where availability=%s""",("not available",))
	dt=cursor.fetchall()
	for i in dt:
		print("-> ",i[2],"Of Class",i[3],"Who Has Withdrawn: \n     # Book:",i[1]," \n     # Code:",i[0]," \n     # Lending Date: %s."%i[4]," \n     # Return Till: %s."%i[5])                
	print("$**************************************************************************$") 
	a=int(input("-> Enter The Code Of The Book You Want To Return: "))
	cursor.execute("""update lib set issue_date=null,stu_name=null,stu_class=null,due_date=null,\
	availability=%s where BOOK_CODE=%s""",("available",a))
	print("<========================== ! Thanks For Returning ! ===========================>")
	mycon.commit()
	choice()


def addbook():

	print("<======================================================================================>")
	print("|:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Addition/Donation Of Books :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
	print("<======================================================================================>")
	speak("Add new books")
	cursor.execute("select * from lib")
	data=cursor.fetchall()
	row=cursor.rowcount
	d=int(input("-> How Many Books You Want To Add: "))
	for i in range(1,d+1):
		print("_______________________________________________________________________________")
		print("""---------------------------    Genre    ---------------------------------------
	|  1. Education                                         2. Fantasy   |
	|  3. Fiction                                           3. Romantic  |
	|  5. Mystry                                            4. Biography |
	|  7. Comic/Manga                                       5. Others    |
-------------------------------------------------------------------------------""")
		c=int(input("-> Select Genre: "))
		if c==1:
			Genre="Education"
		elif c==2:
			Genre="Fantasy"
		elif c==3:
			Genre="Fiction"
		elif c==4:
			Genre="Romantic"
		elif c==5:
			Genre="Mystry"
		elif c==6:
			Genre="Biography"
		elif c==7:
			Genre="Comics/Manga"
		elif c==8:
			Genre="Others"
		else:
			print("#================== Please!! Choose Appropriate Option. ==================#")
		a=str(input("-> Enter Name Of The Book: "))
		b=str(input("-> Enter The Name of The Author Or Publisher: "))
		e=i+row+10000
		cursor.execute("""insert into lib(BOOK_CODE,book_name,author_publisher,Genre) values(%s,%s,%s,%s)""",(e,a,b,Genre))
	mycon.commit()
	print("<---------------- ! The Books Have Been Successfully Added ! ----------------------->")
	print("<===============================================================================>")
	choice()    


def std_details():
	print("<============================================================================>")
	print("|:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Students Details :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
	print("<============================================================================>")
	print("""****************************  ! Select Option !  *****************************
|  1. Details Of Single Student.                                       	    |
|  2. Classwise Details Of Students.                                        |
|  3. Details Of Students Who Are Passed Their Deadline.                    |
|  4. Details Of All The Students Who Have Withdrawn Books From The Library.|
******************************************************************************""")
	s=int(input("-> Enter choice {1-4}: "))
	select(s)
	print("<==========================================================================>")
	choice()


def inventory():
	print("<============================================================================>")
	print("   |:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Inventory :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
	print("<============================================================================>")
	print("""	--------------------------- Select Option ----------------------------
	|   1.Whole Inventory.                                               |
	|   2.Genre Wise List Of Books.                                      |
	----------------------------------------------------------------------""")
	A=int(input("-> Enter Choice {1-2}: "))
	if A==1:
		print(" #   	-:The Books We Have In Our Library Are As Follows:-	    # ")
		print("<==========================================================================>")
		cursor.execute("select book_name,author_publisher from lib where availability='available'")
		data=cursor.fetchall()
		for i in data:
			print("#",i[0],"By",i[1])
	elif A==2:
		print("<==========================================================================>")
		print("""    -----------------------    GENRE    ----------------------------------
	|  1. Education                                         2. Fantasy   |
	|  3. Fiction                                           4. Romantic  |
	|  5. Mystry                                            6. Biography |
	|  7. Comic/Manga                                       8. Others    |
	----------------------------------------------------------------------""")
		print("")
		gen=int(input("-> Select Genre{1-8}:  "))
		if gen==1:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre='Education'""")
			print("The Available Educational Book Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==2:
			cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Fantasy'""")
			print("The Available Fantasy Novels Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==3:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre='Fiction'""")
			print("The Available Fiction Novels Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==4:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre='Romantic'""")
			print("The Available Romantic Novels Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==5:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre='Mystry'""")
			print("The Available Mystry Novels Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==6:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre='Biography'""")
			print("The Available Biographies Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==7:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre in ("Comic","Manga")""")
			print("The Available Comics Or Manga Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("*********************************************************")
		elif gen==8:
			cursor.execute("""select book_name,author_publisher from lib where availability="available" and Genre='Other'""")
			print("Other Available Educational Materials Are Following: ")
			data=cursor.fetchall()
			for i in data:
				print("# Book: %s"%i[0],"::By %s."%i[1])
			print("****************************************************")
		else:
			print("#================== Please!! Choose Appropriate Option. ==================")
			inventory()
	print("<==============================================================>") 
	choice()    

def date(sid,D):
	cursor.execute("""select issue_date from lib where BOOK_CODE=%s""",(sid,))
	data=cursor.fetchone()
	for i in data:
		print(":You Have Lended This Book On: %s:"%i)
	cursor.execute("""select due_date from lib where BOOK_CODE=%s""",(sid,))
	data=cursor.fetchone()
	for i in data:
		print("Please!! Return This Book Within",D,"Days Till%s."%i)

def days(stu,cl,sid):
	D=int(input("-> For How Many Days You Want To Lend The Book {Maximum 30 Days}: "))
	if D>0 and D<=30:
		cursor.execute("""update lib set issue_date=curdate(),due_date=date_add(curdate(),interval %s day),\
	stu_name=%s,stu_class=%s,availability="not available" where BOOK_CODE=%s""",(D,stu,cl,sid))
	else:
		print("   *********** YOU CAN NOT LEND THE BOOK FOR MORE THAN 30 DAYS *************"   )
		lendbook()
	date(sid,D)

def bookselection():
	print("-------------------------------  Lend Book  ----------------------------------")
	print("<==========================================================================>")
	print("""-------------------------------    Genre    ----------------------------------
	|  1. Education                                         2. Fantasy   |
	|  3. Fiction                                           4. Romantic  |
	|  5. Mystry                                            6. Biography |
	|  7. Comic/Manga                                       8. Others    |
------------------------------------------------------------------------------""")
	gen=int(input("Select Genre {1-8}: "))
	if gen==1:
		Genre="Education"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Education'""")
		print("The Available Educational Book Are Following:")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==2:
		Genre="Fantasy"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Fantasy'""")
		print("The Available Fantasy Novels Are Following:")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==3:
		Genre="Fiction"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Fiction'""")
		print("The Available Fiction Novels Are Following: ")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==4:
		Genre="Romantic"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Romantic'""")
		print("The Available Romantic Novels Are Following: ")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==5:
		Genre="Mystry"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Mystry'""")
		print("The Available Mystery Novels Are Following: ")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==6:
		Genre="Biography"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Biography'""")
		print("The Available Biographies Are Following: ")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==7:
		Genre="Comics/Manga"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre in ("Comic","Manga")""")
		print("The Available Comics And Mangas Are Following: ")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	elif gen==8:
		Genre="Others"
		cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Others'""")
		print("Other Available Educational Materials Are Following: ")
		data=cursor.fetchall()
		for i in data:
			print("# ",i[0]," By",i[1],":Code:",i[2])
		print("*********************************************************")
	else:
		print("#==================== Please!! Choose Appropriate Option. ====================#")
		lendbook()
	print("___________________________________________________________")
	sid=int(input("-> Enter Book Code: "))
	stu=str(input("-> Enter Your Name: "))
	cl=int(input("-> Enter Your Class: "))
	days(stu,cl,sid)
	mycon.commit()
	print("___________________________________________________________")

def select(s):
	if s==1:
		print("<*****************************************************************************>")
		name=str(input("-> Enter Name Of The Student: "))
		CLS=int(input("-> Enter The Class Of The Student: "))
		cursor.execute("""select * from lib where stu_name=%s and stu_class=%s""",(name,CLS))
		data=cursor.fetchall()
		p=()
		for i in data:
			p=p+i
		if len(p)==0:
			print("There Are No Records Of This Student!!")
		else:
			print("Details Of Student:- ")
			for i in data:
				print(i[2],"Of Class",i[3],"Has Withdrawn Book",i[1],"code:",i[0],
					  "On",i[4],"Till %s."%i[5])
		print("<*****************************************************************************>")
	if s==2:
		clss=int(input("-> Enter Class: "))
		cursor.execute("""select * from lib where stu_class=%s""",(clss,))
		data=cursor.fetchall()
		p=()
		for i in data:
			p=p+i
		if len(p)==0:
			print("There Are No Students Of This Class !!")
		else:
			print("<*****************    Details Of Class",clss," Students Are Foloowing:-     *****************>")
			for i in data:
				print("#  ",i[2],"Has Withdrawn",i[1],"Code:",i[0],"On",i[4],"Till %s."%i[5])
		print("<*****************************************************************************>")
	elif s==3:
		print("<******************************************************************************>")
		cursor.execute("select * from lib where due_date<curdate()")
		data=cursor.fetchall()
		p=()
		for i in data:
			p=p+i
		if len(p)==0:
			print(" ****** No Student Passed Their Deadline !! ****** ")
		else:
			cursor.execute("select * from lib where due_date<curdate()")
			data=cursor.fetchall()
			print("---- Students Who Passed Their Deadline Are Following:- ----")
			for i in data:
				print("# Student",i[2],"Of Class",i[3],"Who Has Withdrawn Book",i[1],"Code:",i[O],"\n    Is Passed Their Due Date Which Is %s."%i[5])
			print("*******************************************************************************")
	elif s==4:
		print("<******************************************************************************")
		print("""#  The List Of Students Who Are Yet To Return  # **************************>
***************************    Their Books To The Library Are As Follows:-""")
		cursor.execute("""select * from lib where availability=%s""",("not available",))
		dt=cursor.fetchall()
		for i in dt:
			print("# ",i[2],"of Class",i[3],"Who Has Withdrawn \n     Book:",i[1],"Code:",i[0],"on",i[4],"Is Due on",i[5])
						
		print("<******************************************************************************>") 


def exit():
	print("<=====================================================================================>")
	print("<=====:+:===:+:==:+:=====:+:=== Thanks!! For Coming By =====:+:======:+:===:+:==:+:===>")
	print("<=====================================================================================>")
	# root.destroy()
	sys.exit()
home()

'''
x=PhotoImage(file="E:\\Pics\\Cool\\Infinity\\Capture.png",)
c=Label(root,image=x)
c.pack(pady=56,fill=X)

b= Button(c,fg="cyan",text="Lend A Book",command=t.Thread(target=lendbook).start,bg="brown",relief=RIDGE,font=("calibri 15 bold"))
b.pack(side=LEFT,padx=48)

b= Button(c,fg="cyan",text="Return A Book",command=t.Thread(target=Return).start,bg="yellow",relief=RIDGE,font=("calibri 15 bold"))
b.pack(side=LEFT,padx=49)

b= Button(c,fg="cyan",text="Addition of Books",command=t.Thread(target=addbook).start,bg="green",relief=RIDGE,font=("calibri 15 bold"))
b.pack(side=LEFT,padx=49)

b= Button(c,fg="cyan",text="Student Details",command=t.Thread(target=std_details).start,bg="indigo",relief=RIDGE,font=("calibri 15 bold"))
b.pack(side=LEFT,padx=49)

b= Button(c,fg="cyan",text="Inventory",command=t.Thread(target=inventory).start,bg="orange",relief=RIDGE,font=("calibri 15 bold"))
b.pack(side=LEFT,padx=49)

b= Button(c,fg="cyan",text="Exit",command=t.Thread(target=exit).start,bg="red",relief=RIDGE,font=("calibri 15 bold"))
b.pack(side=LEFT,padx=49)

root.mainloop()  
'''
