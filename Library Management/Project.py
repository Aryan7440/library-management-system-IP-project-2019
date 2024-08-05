import mysql.connector as sql
import sys
mycon=sql.connect(host="localhost",user="root",passwd="7489895821",database="library")
cursor=mycon.cursor(buffered=True)



def choice():
        print("")
        ch=str(input("** Do You Want To Continue {Yes/No}: "))
        if ch in ["y","Y","YES","yes","Yes"]:
                print("")
                home()
        else:
            exit()


def home():
    print("***************************** K.V BAIRAGARH ******************************")
    print("                   WELCOME TO LIBRARY MANAGEMENT SYSTEM               ")
    print("""#==============================LIBRARY MENU===============================#
    |  1. Lend A Book                                                   |
    |  2. Return A Book                                                 |
    |  3. Addition Of Books                                             |
    |  4. Student Details                                               |
    |  5. Inventory                                                     |
    |  6. Exit                                                          |
#=========================================================================#
                    * Developed By:- Aryan & Pratik *
#=========================================================================#""")
    print("#================== Please!! Choose Appropriate Option. ==================#")
    print("")
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
             print("")
             print("#================== Please!! Choose Appropriate Option. ==================#")
             choice()


def lendbook():
    print("<=======================================================================>")
    print("|:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Lend A Book :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
    print("<=======================================================================>")
    N=int(input("-> Enter The Number of Books You Want To Lend: "))
    for i in range(1,N+1):
        bookselection()
        
    print("<==========================================================================>")
    choice()


def Return():
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
|  1. Details Of Single Student.                                            |
|  2. Classwise Details Of Students.                                        |
|  3. Details Of Students Who Are Passed Their Deadline.                    |
|  4. Details Of All The Students Who Have Withdrawn Books From The Library.|
******************************************************************************""")
    s=int(input("-> Enter choice {1-4}: "))
    select(s)
    choice()


def inventory():
    print("<============================================================================>")
    print("   |:-|-:-|-:-|-:-|-:-|-:-|-:-|-: Inventory :-|-:-|-:-|-:-|-:-|-:-|-:-|-:|")
    print("<============================================================================>")
    print("""   --------------------------- Select Option ----------------------------
    |   1.Whole Inventory.                                               |
    |   2.Genre Wise List Of Books.                                      |
    ----------------------------------------------------------------------""")
    A=int(input("-> Enter Choice {1-2}: "))
    if A==1:
        print(" #       -:The Books We Have In Our Library Are As Follows:-     # ")
        print("<==========================================================================>")
        cursor.execute("select book_name,author_publisher from lib where availability='available'")
        data=cursor.fetchall()
        for i in data:
            print("#",i[0],"--By",i[1])
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
        print(":You Have Lended This Book On %s:"%i)
    cursor.execute("""select due_date from lib where BOOK_CODE=%s""",(sid,))
    data=cursor.fetchone()
    for i in data:
        print("Please!! Return This Book Within",D,"Days Till %s."%i)

def days(stu,cl,sid):
    D=int(input("-> For How Many Days You Want To Lend The Book {Maximum 30 Days}: "))
    if D>0 and D<=30:
        cursor.execute("""update lib set issue_date=curdate(),due_date=date_add(curdate(),interval %s day),\
    stu_name=%s,stu_class=%s,availability="not available" where BOOK_CODE=%s""",(D,stu,cl,sid))
    else:
        print("   *********** !!You Cannot Lend Book For More Than 30 Days!! *************"   )
        lendbook()
    date(sid,D)

def bookselection():
    print("<==========================================================================>")
    print("""-------------------------------    Genre    ----------------------------------
    |  1. Education                                         2. Fantasy   |
    |  3. Fiction                                           4. Romantic  |
    |  5. Mystry                                            6. Biography |
    |  7. Comic/Manga                                       8. Others    |
------------------------------------------------------------------------------""")
    gen=int(input("Select Genre {1-8}: "))
    if gen==1:
        print("*********************************************************")    
        Genre="Education"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Education'""")
        print("The Available Educational Book Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==2:
        print("*********************************************************")    
        Genre="Fantasy"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Fantasy'""")
        print("The Available Fantasy Novels Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==3:
        print("*********************************************************")    
        Genre="Fiction"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Fiction'""")
        print("The Available Fiction Novels Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==4:
        print("*********************************************************")    
        Genre="Romantic"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Romantic'""")
        print("The Available Romantic Novels Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==5:
        print("*********************************************************")    
        Genre="Mystry"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Mystry'""")
        print("The Available Mystery Novels Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==6:
        print("*********************************************************")    
        Genre="Biography"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Biography'""")
        print("The Available Biographies Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==7:
        print("*********************************************************")    
        Genre="Comics/Manga"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre in ("Comic","Manga")""")
        print("The Available Comics And Mangas Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    elif gen==8:
        print("*********************************************************")    
        Genre="Others"
        cursor.execute("""select book_name,author_publisher,BOOK_CODE from lib where availability="available" and Genre='Others'""")
        print("Other Available Educational Materials Are Following:--")
        data=cursor.fetchall()
        for i in data:
            print("# ",i[0]," -By",i[1],":Code:",i[2])
        print("*********************************************************")
    else:
        print("#==================== Please!! Choose Appropriate Option. ====================#")
        lendbook()
    sid=int(input("-> Enter Book Code: "))
    stu=str(input("-> Enter Your Name: "))
    cl=int(input("-> Enter Your Class: "))
    days(stu,cl,sid)
    mycon.commit()
    print("*********************************************************")

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
            print("<******* Details Of %s:- ********>"%name)
            for i in data:
                print(i[2],"Of Class",i[3],"Has Withdrawn Book",i[1],"On",i[4],"Till %s."%i[5])
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
            print("<***************** Details Of Class",clss," Students Are Foloowing:- *****************>")
            for i in data:
                print("#  ",i[2],"Has Withdrawn %s book"%i[1],"On",i[4],"Till %s."%i[5])
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
                print("# Student",i[2],"Of Class",i[3],"Who Has Withdrawn Book",i[1],"Code:",i[0],"\n    Is Passed Their Due Date Which Is %s."%i[5])
            print("*******************************************************************************")
    elif s==4:
        print("<******************************************************************************")
        print("<------------> The List Of Students Who Are Yet To Return Book are <-------------->")
        cursor.execute("""select * from lib where availability=%s""",("not available",))
        dt=cursor.fetchall()
        for i in dt:
            print("# ",i[2],"of Class",i[3],"Who Has Withdrawn:- \n     ||Book:",i[1],"on",i[4],"Is Due on %s."%i[5])
                        
        print("<******************************************************************************>") 


def exit():
        print("")
        print("<=====================================================================================>")
        print("<=====:+:===:+:==:+:=====:+:=== Thanks!! For Coming By =====:+:======:+:===:+:==:+:===>")
        print("<=====================================================================================>")
        sys.exit()


def exit1():
    print("<=====================================================================================>")
    print("<=====:+:===:+:==:+:=====:+:=== Thanks!! For Coming By =====:+:======:+:===:+:==:+:===>")
    print("<=====================================================================================>")
    #root.destroy()
    sys.exit()
    
home()




