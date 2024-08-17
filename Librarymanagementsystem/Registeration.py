import mysql.connector
import re
from tkinter import *
from tkinter import messagebox
from datetime import datetime

w = Tk()
w.title('Library')
w.config(bg='white')
w.geometry("1000x2000")
w.iconbitmap('homework_fJt_1.ico')


def log():
    import login


def clear():
    sid.delete(0, END)
    n1.delete(0, END)
    e1.delete(0, END)
    phone1.delete(0, END)
    p1.delete(0, END)
    c1.delete(0, END)
    name_entry.delete(0, END)
    card_entry.delete(0, END)
    d_entry.delete(0, END)
    cvv_entry.delete(0, END)
    amount_entry.delete(0, END)


def Ok():
    cname = name_entry.get()
    card_number = card_entry.get()
    regdate = d_entry.get()
    cvv = cvv_entry.get()
    amount = amount_entry.get()
    id = sid.get()
    Name = n1.get()
    Email = e1.get()
    Phone = phone1.get()
    Password = p1.get()
    ConformPassword = c1.get()

    # Validate inputs
    if id == '' or Name == '' or Email == '' or Phone == '' or Password == '' or ConformPassword == '' or cname == '' or card_number == '' or cvv == '' or regdate == '' or amount == '':
        messagebox.showerror('Error', 'All fields are required')
    elif not Phone.isdigit() or len(Phone) != 10:
        messagebox.showerror('Error', 'Phone number must be 10 digits')
    elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', Email):
        messagebox.showerror('Error', 'Email id not valid')
    elif len(Password) < 8 or not re.search("[_@$]", Password) or Password.isdigit() or Password.islower():
        messagebox.showerror('Error',
                             'Password must be at least 8 characters, contain a special character, and include both uppercase and lowercase letters')
    elif ConformPassword != Password:
        messagebox.showerror('Error', 'Passwords do not match')
    elif amount != '100':
        messagebox.showerror('Error', 'Amount only Rs.100 accepted')
    else:
        # Check if date is valid
        try:
            datetime.strptime(regdate, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror('Error', 'Date must be in YYYY-MM-DD format')
            return

        # Check if CVV is valid
        if not cvv.isdigit() or len(cvv) != 3:
            messagebox.showerror('Error', 'CVV must be a 3-digit number')
            return

        conn(id, Name, Email, Phone, Password, ConformPassword, cname, card_number, cvv, regdate, amount)
        import studentmodule


def conn(id, Name, Email, Phone, Password, ConformPassword, cname, card_number, cvv, regdate, amount):
    try:
        mysqlcon = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()
        query = 'INSERT INTO register (studentid, studentname, email, phone, password, conformpassword, cardname, cardnumber, cvv, regdate, amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (id, Name, Email, Phone, Password, ConformPassword, cname, card_number, cvv, regdate, amount)
        mycursor.execute(query, values)
        mysqlcon.commit()
        messagebox.showinfo('Success', 'Registration successful')
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error occurred: {err}')
    finally:
        if mysqlcon.is_connected():
            mycursor.close()
            mysqlcon.close()


# Create the main frame
main_frame = Frame(w, bg='white')
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas widget
canvas = Canvas(main_frame, bg='white')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a Scrollbar widget
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a Frame to contain the form
form_frame = Frame(canvas, bg='white', highlightbackground='black', highlightthickness=2, highlightcolor='black')

# Create a window in the canvas for the form frame
canvas.create_window((60, 0), window=form_frame, anchor='nw')

# Update the scrollbar when the canvas scrolls
form_frame.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

# Add your widgets to the form frame
lab = Label(form_frame, text="Registration Form", font=('times', 20, 'bold'), fg='black', bg='white')
lab.grid(row=0, column=0, columnspan=2, pady=30)

id_label = Label(form_frame, text='Student ID', width=8, pady=5, font=('times', 20, 'bold'), fg='black', bg='white')
id_label.grid(row=2, column=0, pady=10)

sid = Entry(form_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
sid.config(highlightcolor='black', highlightbackground='black')
sid.grid(row=2, column=1, padx=20, pady=10)

name_label = Label(form_frame, text='Student Name', width=10, padx=50, pady=5, font=('times', 20, 'bold'), fg='black',
                   bg='white')
name_label.grid(row=3, column=0, ipadx=0, pady=10)

n1 = Entry(form_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
n1.config(highlightcolor='black', highlightbackground='black')
n1.grid(row=3, column=1, padx=20, pady=20)

email_label = Label(form_frame, text='Student Email', width=13, padx=5, pady=5, font=('times', 20, 'bold'), fg='black',
                    bg='white')
email_label.grid(row=4, column=0, padx=10, pady=10)
e1 = Entry(form_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
e1.config(highlightcolor='black', highlightbackground='black')
e1.grid(row=4, column=1, padx=20, pady=20)

phone_label = Label(form_frame, text='Student Ph.no', width=13, pady=5, font=('times', 20, 'bold'), fg='black',
                    bg='white')
phone_label.grid(row=5, column=0, padx=10, pady=10)
phone1 = Entry(form_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
phone1.config(highlightcolor='black', highlightbackground='black')
phone1.grid(row=5, column=1, padx=20, pady=20)

password_label = Label(form_frame, text='Student Password', width=13, padx=90, pady=5, font=("times", 20, 'bold'),
                       fg='black', bg='white')
password_label.grid(row=6, column=0, padx=20, pady=10)
p1 = Entry(form_frame, width=20, show='*', font=('times', 15, 'bold'), highlightthickness=1)
p1.config(highlightcolor='black', highlightbackground='black')
p1.grid(row=6, column=1, padx=20, pady=20)

cp_label = Label(form_frame, text='Confirm Password', width=13, padx=90, pady=5, font=("times", 20, 'bold'), fg='black',
                 bg='white')
cp_label.grid(row=7, column=0, padx=10, pady=10)
c1 = Entry(form_frame, width=20, show='*', font=('times', 15, 'bold'), highlightthickness=1)
c1.config(highlightcolor='black', highlightbackground='black')
c1.grid(row=7, column=1, padx=20, pady=20)

Cardname = Label(form_frame, text='Card Name', font=('times', 20, 'bold'), fg='black', bg='white')
Cardname.grid(row=8, column=0, pady=10, padx=20)
name_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
name_entry.config(highlightcolor='black', highlightbackground='black')
name_entry.grid(row=8, column=1)

Cardnumber = Label(form_frame, text='Card Number', font=('times', 20, 'bold'), fg='black', bg='white')
Cardnumber.grid(row=9, column=0, padx=20, pady=10)
card_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', show='*', highlightthickness=1)
card_entry.config(highlightcolor='black', highlightbackground='black')
card_entry.grid(row=9, column=1)

registerdate = Label(form_frame, text='Register Date', font=('times', 20, 'bold'), fg='black', bg='white')
registerdate.grid(row=10, column=0, padx=20, pady=10)
d_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
d_entry.config(highlightcolor='black', highlightbackground='black')
d_entry.grid(row=10, column=1)

Cvv = Label(form_frame, text='CVV', font=('times', 20, 'bold'), fg='black', bg='white')
Cvv.grid(row=11, column=0, padx=20, pady=10)
cvv_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1, show='*')
cvv_entry.config(highlightcolor='black', highlightbackground='black')
cvv_entry.grid(row=11, column=1)

Amount = Label(form_frame, text='Amount', font=('times', 20, 'bold'), fg='black', bg='white')
Amount.grid(row=12, column=0, padx=20, pady=10)
amount_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
amount_entry.config(highlightcolor='black', highlightbackground='black')
amount_entry.grid(row=12, column=1)

sub_button = Button(form_frame, text='Submit', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black',
                    bg='#55efc4', command=Ok)
sub_button.grid(row=13, column=1, sticky=W, padx=120, pady=10)

login_button = Button(form_frame, text='Login', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black',
                      bg='#74b9ff', command=log)
login_button.grid(row=13, column=1, sticky=E, padx=20, pady=10)

clear_button = Button(form_frame, text='Clear', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black',
                      bg='#ff7675', command=clear)
clear_button.grid(row=13, column=2, sticky=W, pady=10)

w.mainloop()
