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
    d.delete(0, END)

def sub():
    studentid = id.get()
    studentname = name.get()
    bookname = bname.get()
    bookid = bid.get()
    author = a.get()
    return_date_str = d.get()

    if not studentid or not studentname or not bookid or not bookname or not author or not return_date_str:
        messagebox.showerror("Message", 'All fields are required')
        return

    try:
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()

        mysqlcon = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()

        # Retrieve the due date and borrowed date from the `takebook` table
        query = 'SELECT due_date, date_borrowed FROM takebook WHERE studentid=%s AND studentname=%s AND bookid=%s AND bookname=%s AND author=%s'
        mycursor.execute(query, (studentid, studentname, bookid, bookname, author))
        res = mycursor.fetchall()

        if res:
            due_date, date_borrowed = res[0]

            # Check if the return date is before or equal to the due date
            if return_date > due_date:
                messagebox.showerror('Error', f'Return date {return_date} is after the due date {due_date}. Book cannot be returned.')
                return

            # Insert into `returnbook` table
            query1 = 'INSERT INTO returnbook (studentid, studentname, bookid, bookname, author, return_date) VALUES (%s, %s, %s, %s, %s, %s)'
            values = (studentid, studentname, bookid, bookname, author, return_date)
            mycursor.execute(query1, values)
            mysqlcon.commit()
            messagebox.showinfo('Message', 'Book returned successfully')

        else:
            messagebox.showerror('Error', 'No matching book found or already returned')

    except ValueError:
        messagebox.showerror('Error', 'Invalid date format. Please use YYYY-MM-DD.')
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')

    finally:
        mycursor.close()
        mysqlcon.close()

w = Tk()
w.geometry("600x500")
w.title("Return Book")
w.iconbitmap('homework_fJt_1.ico')
f = Frame(w, highlightbackground='black', bg='white', highlightthickness=2, padx=5, pady=10)
f.grid(row=0, column=1, padx=50, pady=50)

returnbook = Label(f, text='Return Book', font=('times', 20, 'bold'), fg='black', bg='white', padx=20, pady=10)
returnbook.grid(row=0, column=0, columnspan=2)

Studentid = Label(f, text='Student ID', font=('times', 20, 'bold'), fg='black', bg='white', padx=20, pady=1)
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

date = Label(f, text='Return Date', font=('times', 20, 'bold'), fg='black', bg='white')
date.grid(row=6, column=0, padx=20, pady=10)
d = Entry(f, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
d.config(highlightcolor='black', highlightbackground='black')
d.grid(row=6, column=1)

sub = Button(f, text='Submit', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#55efc4',
             command=sub)
sub.grid(row=7, column=1, sticky=W, padx=(10, 10))

clear = Button(f, text='Clear', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#ff7675',
               command=clear)
clear.grid(row=7, column=1, sticky=E, padx=(10, 10))

w.mainloop()
