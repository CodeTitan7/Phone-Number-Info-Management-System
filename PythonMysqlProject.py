'''q="create table phn(Sno int Primary key ,Phno char(10),Firstname char(50),Lastname char(50),Address char(200),EmailID varchar(100))"
cur.execute(q)
con.commit()
cur.close()
con.close()
'''

def space():
    for i in range(4):
        print()

def add():
    a=int(input("Enter serial number"))
    b=input("Enter phone number")
    c=input("Enter Firstname")
    d=input("Enter Lastname")
    e=input("Enter Address")
    f=input("Enter EmailID")
    z="insert into phn values({},'{}','{}','{}','{}','{}')".format(a,b,c,d,e,f)
    cur.execute(z)
    con.commit()
    print("Record is added")
    space()    

def delete():
    a=input("Enter Firstname of the person whose data to be deleted")
    k="delete from phn where Firstname = "+"'"+a+"'"+";"
    cur.execute(k)
    con.commit()
    print("Record is deleted")
    space()

def mod():
    print("1.Modify phone number")
    print("2.Modify Firstname")
    print("3.Modify Lastname")
    print("4.Modify Address")
    print("5.Modify EmailID")
    choice1=int(input("Enter your choice...."))
    if choice1==1:
        a=input("Enter Firstname")        
        b=input("Enter modified phone number")
        x="UPDATE phn SET Phno ="+"'"+b+"'"+" WHERE Firstname = "+"'"+a+"'"+";"
        cur.execute(x)
        con.commit()       
    if choice1==2:
        a=input("Enter Firstname")        
        b=input("Enter modified Firstname")
        x="UPDATE phn SET Firstname ="+"'"+b+"'"+" WHERE Firstname = "+"'"+a+"'"+";"
        cur.execute(x)
        con.commit()        
    if choice1==3:
        a=input("Enter Firstname")        
        b=input("Enter modified Lastname")
        x="UPDATE phn SET Lastname ="+"'"+b+"'"+" WHERE Firstname = "+"'"+a+"'"+";"
        cur.execute(x)
        con.commit()
    if choice1==4:
        a=input("Enter Firstname")       
        b=input("Enter modified Address")
        x="UPDATE phn SET Address ="+"'"+b+"'"+"  WHERE Firstname = "+"'"+a+"'"+";"
        cur.execute(x)
        con.commit()        
    if choice1==5:
        a=input("Enter Firstname")      
        b=input("Enter modified EmailID")
        x="UPDATE phn SET EmailID ="+"'"+b+"'"+" WHERE Firstname = "+"'"+a+"'"+";"
        cur.execute(x)
        con.commit()        
    print("Record is modified")
    space()    

def disf():
    cur.execute("SELECT * FROM phn")
    a= cur.fetchall()
    for x in a:
        print(x)
    con.commit()
    space()    

def disp():
    y=input("Enter the  name of whose record you want")
    cur.execute("SELECT*FROM phn where Firstname ="+"'"+y+"'")
    a= cur.fetchall()
    for x in a:
        print(x)
    con.commit()
    space()


import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="devanarayan",database="dev")
if (con.is_connected()):
    print("OK")
cur=con.cursor()
print("Phone Number Management System")
while True:
    print("1.Add Records")
    print("2.Modify Records")
    print("3.Delete Records")
    print("4.Display Records")
    print("5.Display a particular Records")
    print("6.Exit")
    print("\nEnter your choice....")
    choice=int(input())
    if choice==1:
        add()
    elif choice==2:
        mod()
    elif choice==3:
        delete()
    elif choice==4:
        disf()
    elif choice==5:
        disp()
    elif choice==6:
        print("The programme is ended,Bye")
        break
    else:
        print("Enter a number between 1 and 6")
        space()
con.close()
cur.close()




















        

        


        
