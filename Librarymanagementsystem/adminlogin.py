import  mysql.connector
from tkinter import *
from tkinter import messagebox

def clear():
    n1.delete(0,END)
    e1.delete(0,END)
    p1.delete(0,END)
    p3.delete(0,END)
    c1.delete(0,END)



def sub():

        db = mysql.connector.connect(host='localhost',port=3306, user='suba',password='suba123', database='lib')
        cur = db.cursor()

        user = n.get()
        password= p.get()

        query = 'SELECT * FROM admin WHERE name=%s AND password=%s'
        cur.execute(query, (user, password))

        res = cur.fetchall()

        if res:
            w.destroy()
            import main1
            return True
        else:
            if e.get()!= '' or p.get != '':
               messagebox.showerror('Error', 'Username or password error')
               return False

        db.close()



w = Tk()
w.title('adminlogin')
w.config(bg='white')
w.iconbitmap('homework_fJt_1.ico')

frame1 = Frame(w, highlightbackground='black', highlightthickness=2, padx=5, pady=10,bg='white')
frame1.grid(row=0, column=1, padx=50, pady=50)

log = Label(frame1, text='Login', font=('times', 20, 'bold'), fg='black',bg='white')
log.grid(row=0, column=0, columnspan=2, sticky=S)

name = Label(frame1, text='Adminname', font=('times', 20, 'bold'), fg='black',bg='white')
name.grid(row=1, column=0, padx=10, pady=10)
n = Entry(frame1, width=20, font=('times', 15, 'bold'),highlightthickness=1)
n.config(highlightcolor='black',highlightbackground='black')
n.grid(row=1, column=1, padx=20, pady=10)

password= Label(frame1, text='Password', font=('times', 20, 'bold'), fg='black',bg='white')
password.grid(row=2, column=0, padx=10, pady=10)
p = Entry(frame1, width=20, font=('times', 15, 'bold'), show='*',highlightthickness=1)
p.config(highlightcolor='black',highlightbackground='black')
p.grid(row=2, column=1, padx=20, pady=10)


sub = Button(frame1, text='Submit',border=0, padx=20, pady=5,font=("times", 10, 'bold') , fg='black', bg='#55efc4', command=sub)
sub.grid(row=3, column=1, sticky=E, padx=10)
clear= Button(frame1, text='Clear',border=0, padx=20, pady=5,font=("times", 10, 'bold') , fg='black', bg='#ff7675',command=clear)
clear.grid(row=3, column=2, sticky=W)

w.mainloop()
