import mysql.connector
from tkinter import *
from tkinter import messagebox

def clear():
    sid.delete(0,END)
    n.delete(0, END)
    p.delete(0, END)

def submit():
    db = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
    cur = db.cursor()
    studentid=sid.get()
    user = n.get()
    password = p.get()

    query = 'SELECT * FROM register WHERE studentid=%s AND studentname=%s AND password=%s'
    cur.execute(query, (studentid,user, password))

    res = cur.fetchall()

    if res:
        import studentmodule # Assuming main is another Python module
        w.destroy()
        return True
    else:
        if user != '' or password != '':
            messagebox.showerror('Error', 'Username or password is incorrect')
        return False

    cur.close()
    db.close()

w = Tk()
w.title("studentlogin")
w.config(bg='white')
w.iconbitmap('homework_fJt_1.ico')
frame1 = Frame(w, highlightbackground='black', highlightthickness=2, padx=5, pady=10,bg='white')
frame1.grid(row=0, column=1, padx=50, pady=50)

log = Label(frame1, text='Login', font=('times', 20, 'bold'), fg='black',bg='white')
log.grid(row=0, column=0, columnspan=2, sticky=S)

id= Label(frame1, text='Studentid', font=('times', 20, 'bold'), fg='black',bg='white')
id.grid(row=1, column=0, padx=10, pady=10)

sid= Entry(frame1, width=20, font=('times', 15, 'bold'),highlightthickness=1)
sid.config(highlightbackground='black',highlightcolor='black')
sid.grid(row=1, column=1, padx=20, pady=10)

name = Label(frame1, text='Studentname', font=('times', 20, 'bold'), fg='black',bg='white')
name.grid(row=2, column=0, padx=10, pady=10)

n = Entry(frame1, width=20, font=('times', 15, 'bold'),highlightthickness=1)
n.config(highlightbackground='black',highlightcolor='black')
n.grid(row=2, column=1, padx=20, pady=10)

Password = Label(frame1, text='Password', font=('times', 20, 'bold'), fg='black',bg='white')
Password.grid(row=3, column=0, padx=10, pady=10)

p = Entry(frame1, width=20, font=('times', 15, 'bold'), show='*',highlightthickness=1)
p.config(highlightbackground='black',highlightcolor='black')
p.grid(row=3, column=1, padx=20, pady=10)

submit_btn = Button(frame1, text='Submit', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#55efc4', command=submit)
submit_btn.grid(row=4, column=1, padx=10)

clear_btn = Button(frame1, text='Clear', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#ff7675', command=clear)
clear_btn.grid(row=4, column=1,sticky=E)

w.mainloop()
