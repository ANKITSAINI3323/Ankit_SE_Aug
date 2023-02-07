"""
    Tkinter is a Module.

        - a predefined class inside Python.
        
"""

from tkinter import *
import tkinter.messagebox as msg
import mysql.connector

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="dec12python"
        )

print(create_conn())


def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory*")
    else:
        conn = create_conn()
        cursor = conn.cursor()  # Execute the connection
        query = "insert into employee (fname,lname,email,mobile) values (%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args) # Execute the query
        conn.commit()
        conn.close()
        msg.showinfo("Insert Status","Data Inserted Successfully.")

    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

def search_data():
    print("Update Clicked")

def update_data():
    print("Update Clicked")

def delete_data():
    print("Delete Clicked")


root = Tk()
root.geometry("400x400")
root.title("Employee Registration")
root.resizable(width="false",height="false")


#Labels

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname = Label(root,text="First Name : ")
l_fname.place(x=50,y=100)

l_lname = Label(root,text="Last Name : ")
l_lname.place(x=50,y=150)

l_email = Label(root,text="Email : ")
l_email.place(x=50,y=200)

l_mobile = Label(root,text="Mobile : ")
l_mobile.place(x=50,y=250)


# TextBoxes

e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname = Entry(root)
e_fname.place(x=150,y=100)

e_lname = Entry(root)
e_lname.place(x=150,y=150)

e_email = Entry(root)
e_email.place(x=150,y=200)

e_mobile = Entry(root)
e_mobile.place(x=150,y=250)

#Buttons

insert = Button(root,text="Insert",bg="black",fg="white",font=("Arial",10),command=insert_data)
insert.place(x=50,y=300)

search = Button(root,text="Search",bg="black",fg="white",font=("Arial",10),command=search_data)
search.place(x=120,y=300)

update = Button(root,text="Update",bg="black",fg="white",font=("Arial",10),command=update_data)
update.place(x=190,y=300)

delete = Button(root,text="Delete",bg="black",fg="white",font=("Arial",10),command=delete_data)
delete.place(x=260,y=300)



    




































