from tkinter import *
import mysql.connector
from tkinter import messagebox
from datetime import datetime

def clear():
    name.delete(0, END)
    id.delete(0, END)
    bid.delete(0, END)
    bname.delete(0, END)
    a.delete(0, END)
    i.delete(0, END)
    idate.delete(0, END)

def sub():
    studentid = id.get()
    studentname = name.get()
    bookid = bid.get()
    bookname = bname.get()
    author = a.get()
    issue = i.get()
    issuedate = idate.get()

    if studentid == "" or studentname == "" or bookid == "" or bookname == "" or author == "" or issue == '' or issuedate == '':
        messagebox.showerror("Message", 'All fields are required')
        return

    # Define current date
    currentdate = datetime.now().strftime('%Y-%m-%d')

    try:
        mysqlcon = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()

        # Check if the book details match any record in the takebook table
        query = '''SELECT * FROM takebook 
                   WHERE studentid=%s AND studentname=%s AND bookid=%s AND bookname=%s AND author=%s'''
        mycursor.execute(query, (studentid, studentname, bookid, bookname, author))
        res = mycursor.fetchall()

        if res:
            query1 = '''INSERT INTO issuebook (studentid, studentname, bookid, bookname, author, issuebook, currentdate) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            values = (studentid, studentname, bookid, bookname, author, issue, currentdate)
            mycursor.execute(query1, values)
            mysqlcon.commit()
            messagebox.showinfo('Message', 'Book issued successfully')
        else:
            messagebox.showerror('Error', 'No matching book found')

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        mycursor.close()
        mysqlcon.close()

w = Tk()
w.geometry("600x600")
w.title("Issue Book")
w.iconbitmap('homework_fJt_1.ico')

f = Frame(w, highlightbackground='black', bg='white', highlightthickness=2, padx=10, pady=10)
f.grid(row=0, column=1, padx=50, pady=50)

returnbook = Label(f, text='Issue Book', font=('times', 20, 'bold'), fg='black', bg='white', padx=20, pady=10)
returnbook.grid(row=0, column=0, columnspan=2)

Studentid = Label(f, text='Student ID', font=('times', 20, 'bold'), fg='black', bg='white', padx=20, pady=10)
Studentid.grid(row=1, column=0, pady=10, padx=20)
id = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
id.config(highlightcolor='black', highlightbackground='black')
id.grid(row=1, column=1)

Studentname = Label(f, text='Student Name', font=('times', 20, 'bold'), fg='black', bg='white')
Studentname.grid(row=2, column=0, padx=20, pady=10)
name = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
name.config(highlightcolor='black', highlightbackground='black')
name.grid(row=2, column=1)

Bookname = Label(f, text='Book Name', font=('times', 20, 'bold'), fg='black', bg='white')
Bookname.grid(row=3, column=0, padx=20, pady=10)
bname = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
bname.config(highlightcolor='black', highlightbackground='black')
bname.grid(row=3, column=1)

Bookid = Label(f, text='Book ID', font=('times', 20, 'bold'), fg='black', bg='white')
Bookid.grid(row=4, column=0, padx=20, pady=10)
bid = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
bid.config(highlightcolor='black', highlightbackground='black')
bid.grid(row=4, column=1)

Author = Label(f, text='Author', font=('times', 20, 'bold'), fg='black', bg='white')
Author.grid(row=5, column=0, padx=20, pady=10)
a = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
a.config(highlightcolor='black', highlightbackground='black')
a.grid(row=5, column=1)

Issues = Label(f, text='Issues', font=('times', 20, 'bold'), fg='black', bg='white')
Issues.grid(row=6, column=0, padx=20, pady=10)
i = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
i.config(highlightcolor='black', highlightbackground='black')
i.grid(row=6, column=1)

Issuedate = Label(f, text='Issue Date', font=('times', 20, 'bold'), fg='black', bg='white')
Issuedate.grid(row=7, column=0, padx=20, pady=10)
idate = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
idate.config(highlightcolor='black', highlightbackground='black')
idate.grid(row=7, column=1)

# Submit and Clear buttons
sub_btn = Button(f, text='Submit', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#55efc4', command=sub)
sub_btn.grid(row=8, column=1, sticky=W, padx=10)

clear_btn = Button(f, text='Clear', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#ff7675', command=clear)
clear_btn.grid(row=8, column=1, sticky=E, padx=10)

w.mainloop()

