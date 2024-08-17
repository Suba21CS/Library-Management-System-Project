from tkinter import *
import mysql.connector
from tkinter import messagebox

def clear():
    name.delete(0, END)
    id.delete(0, END)
    bid.delete(0, END)
    bname.delete(0, END)
    bid.delete(0, END)


def sub():
    studentid = id.get()
    studentname = name.get()
    bookid = bid.get()  # Use bid here for book ID
    bookname = bname.get()  # Use bname here for book name
    author = a.get()

    if studentid == "" or studentname == "" or bookid == "" or bookname == "" or author == "":
        messagebox.showerror("message", 'All fields are required')
        return

    try:
        mysqlcon = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()
        query = 'SELECT * FROM register WHERE studentid=%s AND studentname=%s'
        mycursor.execute(query, (studentid, studentname))

        res = mycursor.fetchall()

        if res:
            query1 = 'INSERT INTO addbook(studentname,studentid,bookid, bookname, author) VALUES (%s,%s, %s, %s, %s)'
            values = (studentname,studentid,bookid, bookname, author)
            mycursor.execute(query1, values)
            mysqlcon.commit()
            messagebox.showinfo('message', 'Book added successfully')
        else:
            messagebox.showerror('Error', 'Student not found')

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        mycursor.close()
        mysqlcon.close()


w=Tk()
w.iconbitmap('homework_fJt_1.ico')
w.geometry("600x600")
w.title("Addbook")


f= Frame(w, highlightbackground='black',bg='white', highlightthickness=2, padx=5, pady=10)
f.grid(row=0, column=1, padx=50, pady=50)
addbook=Label(f,text='Add Book',font=('times',20,'bold'),fg='black',bg='white',padx=20,pady=10)
addbook.grid(row=0,column=0,columnspan=2)

Studentid=Label(f,text='Studentid',font=('times',20,'bold'),fg='black',bg='white')
Studentid.grid(row=1,column=0,pady=10,padx=20)
id=Entry(f,font=('times',15,'bold'),fg='black',bg='white',highlightthickness=1)
id.config(highlightbackground='black',highlightcolor='black')
id.grid(row=1,column=1)
Studentname=Label(f,text='Studentname',font=('times',20,'bold'),fg='black',bg='white')
Studentname.grid(row=2,column=0,padx=20,pady=10)
name=Entry(f,font=('times',15,'bold'),fg='black',bg='white',highlightthickness=1)
name.config(highlightcolor='black',highlightbackground='black')
name.grid(row=2,column=1)
Bookname=Label(f,text='Bookname',font=('times',20,'bold'),fg='black',bg='white')
Bookname.grid(row=3,column=0,padx=20,pady=10)
bname=Entry(f,font=('times',15,'bold'),fg='black',bg='white',highlightthickness=1)
bname.config(highlightcolor='black',highlightbackground='black')
bname.grid(row=3,column=1)
Bookid=Label(f,text='Bookid',font=('times',20,'bold'),fg='black',bg='white')
Bookid.grid(row=4,column=0,padx=20,pady=10)
bid=Entry(f,font=('times',15,'bold'),fg='black',bg='white',highlightthickness=1)
bid.config(highlightcolor='black',highlightbackground='black')
bid.grid(row=4,column=1)
Author=Label(f,text='Author',font=('times',20,'bold'),fg='black',bg='white')
Author.grid(row=5,column=0,padx=20,pady=10)

a=Entry(f,font=('times',15,'bold'),fg='black',bg='white',highlightthickness=1)
a.config(highlightcolor='black',highlightbackground='black')
a.grid(row=5,column=1)
sub = Button(f, text='Submit',border=0, padx=20, pady=5,font=("times", 10, 'bold') , fg='black', bg='#55efc4', command=sub)
sub.grid(row=6, column=1, sticky=E, padx=10)
clear= Button(f, text='Clear',border=0, padx=20, pady=5,font=("times", 10, 'bold') , fg='black', bg='#ff7675',command=clear)
clear.grid(row=6, column=2, sticky=W)

w.mainloop()

