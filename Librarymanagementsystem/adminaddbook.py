from tkinter import *
from tkinter import messagebox
import mysql.connector


def clear():
    sno1.delete(0,END)
    bid.delete(0, END)
    bname.delete(0, END)
    a.delete(0, END)


def sub():
    Sno=sno1.get()
    bookid = bid.get()
    bookname = bname.get()
    author = a.get()

    if bookid == '' or bookname == '' or author == '':
        messagebox.showerror('Error', 'All fields are required')
        return

    try:
        db = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
        cur = db.cursor()
        query = 'INSERT INTO bookdetail (sno,bookid, bookname, author) VALUES (%s, %s, %s,%s)'
        values = (Sno,bookid, bookname, author)

        cur.execute(query, values)
        db.commit()
        messagebox.showinfo('Message', 'Book added successfully')
        clear()
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        cur.close()
        db.close()


w = Tk()
w.title('Library')
w.config(bg='white')
w.geometry("700x700")
w.iconbitmap('homework_fJt_1.ico')

frame = Frame(w, highlightbackground='black', bg='white',highlightthickness=2, padx=10, pady=10)
frame.grid(row=0, column=0, padx=80, pady=80)
lab = Label(frame, text="Add Book", font=('times', 20, 'bold'), fg='black',bg='white')
lab.grid(row=0, column=0, columnspan=2, pady=10, sticky=S)
Sno=Label(frame,text='S.No', font=('times', 20, 'bold'), fg='black',bg='white')
Sno.grid(row=1,column=0,padx=20,pady=20)
sno1= Entry(frame, width=20, font=('times', 15, 'bold'),highlightthickness=1)
sno1.config(highlightcolor='black',highlightbackground='black')
sno1.grid(row=1, column=1, padx=20, pady=20)
bookid_label = Label(frame, text='Bookid', font=('times', 20, 'bold'), fg='black',bg='white')

bookid_label.grid(row=2, column=0, padx=10, pady=10)
bid = Entry(frame, width=20, font=('times', 15, 'bold'),highlightthickness=1)
bid.config(highlightcolor='black',highlightbackground='black')
bid.grid(row=2, column=1, padx=20, pady=20)

bookname_label = Label(frame, text='Bookname', font=('times', 20, 'bold'), fg='black',bg='white')
bookname_label.grid(row=3, column=0, padx=10, pady=10)
bname = Entry(frame, width=20, font=('times', 15, 'bold'),highlightthickness=1)
bname.config(highlightcolor='black',highlightbackground='black')
bname.grid(row=3, column=1, padx=20, pady=20)

author_label = Label(frame, text='Author', font=('times', 20, 'bold'), fg='black',bg='white')
author_label.grid(row=4, column=0, padx=10, pady=10)
a = Entry(frame, width=20, font=('times', 15, 'bold'),highlightthickness=1)
a.config(highlightcolor='black',highlightbackground='black')
a.grid(row=4, column=1, padx=20, pady=20)

sub1 = Button(frame, text='Submit', border=0, padx=20, pady=5, fg='black', bg='#55efc4', command=sub)
sub1.grid(row=5, column=1, sticky=W, padx=100)

clear_button = Button(frame, text='Clear', border=0, padx=20, pady=5, fg='black', bg='#ff7675', command=clear)
clear_button.grid(row=5, column=1, sticky=E, padx=10)

w.mainloop()

