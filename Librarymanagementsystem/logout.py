import mysql.connector
from tkinter import *
from tkinter import messagebox


def clear():
    n.delete(0, END)
    p.delete(0, END)
    sid.delete(0, END)


def submit():
    db = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
    cur = db.cursor()
    studentid = sid.get()
    user = n.get()
    password = p.get()

    query = 'SELECT * FROM register WHERE studentid=%s AND studentname=%s AND password=%s'
    cur.execute(query, (studentid, user, password))

    res = cur.fetchall()

    cur.close()
    db.close()

    if res:
        logout(studentid, user, password)
        w.destroy()
    else:
        if user != '' or password != '':
            messagebox.showerror('Error', 'Username or password is incorrect')


def logout(studentid, user, password):
    try:
        mycon = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycur = mycon.cursor()
        query = 'DELETE FROM register WHERE studentid=%s AND studentname=%s AND password=%s'
        mycur.execute(query, (studentid, user, password))
        mycon.commit()
        messagebox.showinfo('message', 'Logout successful')
    except mysql.connector.Error as er:
        messagebox.showerror('Error', f'Error: {er}')
    finally:
        mycur.close()
        mycon.close()


w = Tk()
w.title("Logout")
w.iconbitmap('homework_fJt_1.ico')
w.config(bg='white')
frame1 = Frame(w, highlightbackground='black', highlightthickness=2, padx=5, pady=10, bg='white')
frame1.grid(row=0, column=1, padx=50, pady=50)


log = Label(frame1, text='Logout', font=('times', 20, 'bold'), fg='black',bg='white')
log.grid(row=0, column=0, columnspan=2, sticky=S)

id_label = Label(frame1, text='Studentid', font=('times', 20, 'bold'), fg='black', bg='white')
id_label.grid(row=1, column=0, padx=10, pady=10)

sid = Entry(frame1, width=20, font=('times', 15, 'bold'), highlightthickness=1)
sid.config(highlightbackground='black', highlightcolor='black')
sid.grid(row=1, column=1, padx=20, pady=10)

name_label = Label(frame1, text='Studentname', font=('times', 20, 'bold'), fg='black', bg='white')
name_label.grid(row=2, column=0, padx=10, pady=10)

n = Entry(frame1, width=20, font=('times', 15, 'bold'), highlightthickness=1)
n.config(highlightbackground='black', highlightcolor='black')
n.grid(row=2, column=1, padx=20, pady=10)

password_label = Label(frame1, text='Password', font=('times', 20, 'bold'), fg='black', bg='white')
password_label.grid(row=3, column=0, padx=10, pady=10)

p = Entry(frame1, width=20, font=('times', 15, 'bold'), show='*', highlightthickness=1)
p.config(highlightbackground='black', highlightcolor='black')
p.grid(row=3, column=1, padx=20, pady=10)

submit_btn = Button(frame1, text='Submit', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black',
                    bg='#55efc4', command=submit)
submit_btn.grid(row=4, column=1, padx=10)

clear_btn = Button(frame1, text='Clear', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black',
                   bg='#ff7675', command=clear)
clear_btn.grid(row=4, column=1, sticky=E)

w.mainloop()
