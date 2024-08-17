from tkinter import *
from tkinter import messagebox
import mysql.connector

def clear_fields():
    sname.delete(0, END)
    id.delete(0, END)
    bid.delete(0, END)
    bname.delete(0, END)
    a.delete(0, END)
    name_entry.delete(0, END)
    card_entry.delete(0, END)
    expiry_entry.delete(0, END)
    cvv_entry.delete(0, END)
    amount_entry.delete(0, END)

def make_payment():
    studentid = id.get()
    studentname = sname.get()
    bookid = bid.get()
    bookname = bname.get()
    author = a.get()
    name = name_entry.get()
    card_number = card_entry.get()
    expiry_date = expiry_entry.get()
    cvv = cvv_entry.get()
    amount = amount_entry.get()

    # Validate fields
    if not studentid or not studentname or not bookid or not bookname or not author or not name or not card_number or not expiry_date or not cvv or not amount:
        messagebox.showerror("Error", "All fields are required")
        return
    try:
        amount = float(amount)
        if amount != 100:
            messagebox.showerror("Error", "Amount only Rs.100 accepted")
            return

        # Connect to the database
        db = mysql.connector.connect(
            host='localhost',
            user='suba',
            password='suba123',
            database='lib'
        )
        cur = db.cursor()

        # Check if the book and student details exist
        query = '''SELECT due_date, date_borrowed FROM takebook 
                   WHERE studentid=%s AND studentname=%s AND bookid=%s AND bookname=%s AND author=%s'''
        cur.execute(query, (studentid, studentname, bookid, bookname, author))
        res = cur.fetchone()

        if res:
            # Insert payment details into the database
            query = '''INSERT INTO payments 
                       (studentid, studentname, bookid, bookname, author, name, card_number, expiry_date, cvv, amount) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            values = (studentid, studentname, bookid, bookname, author, name, card_number, expiry_date, cvv, amount)
            cur.execute(query, values)
            db.commit()

            messagebox.showinfo("Success", "Payment successful!")
            clear_fields()
        else:
            messagebox.showerror("Error", "Book or student details not found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")
    finally:
        cur.close()
        db.close()

# Tkinter GUI setup
w = Tk()
w.geometry('1000x800')
w.title('Return Book Payment')
w.iconbitmap('homework_fJt_1.ico')

main_frame = Frame(w, bg='white')
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame, bg='white')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

form_frame = Frame(canvas, bg='white', highlightthickness=2, highlightbackground='black', padx=50)
canvas.create_window((200, 0), window=form_frame, anchor='nw')

# Form title
onlinepayment = Label(form_frame, text='Online Payment', font=('times', 20, 'bold'), fg='black', bg='white', padx=20, pady=10)
onlinepayment.grid(row=0, column=0, columnspan=2)

Studentid = Label(form_frame, text='Student ID', font=('times', 20, 'bold'), fg='black', bg='white', padx=20, pady=1)
Studentid.grid(row=1, column=0, pady=10, padx=20)
id = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
id.config(highlightcolor='black', highlightbackground='black')
id.grid(row=1, column=1)

Studentname = Label(form_frame, text='Student Name', font=('times', 20, 'bold'), fg='black', bg='white')
Studentname.grid(row=2, column=0, padx=20, pady=10)
sname = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
sname.config(highlightcolor='black', highlightbackground='black')
sname.grid(row=2, column=1)

Bookname = Label(form_frame, text='Book Name', font=('times', 20, 'bold'), fg='black', bg='white')
Bookname.grid(row=3, column=0, padx=20, pady=10)
bname = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
bname.config(highlightcolor='black', highlightbackground='black')
bname.grid(row=3, column=1)

Bookid = Label(form_frame, text='Book ID', font=('times', 20, 'bold'), fg='black', bg='white')
Bookid.grid(row=4, column=0, padx=20, pady=10)
bid = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
bid.config(highlightcolor='black', highlightbackground='black')
bid.grid(row=4, column=1)

Author = Label(form_frame, text='Author', font=('times', 20, 'bold'), fg='black', bg='white')
Author.grid(row=5, column=0, padx=20, pady=10)
a = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
a.config(highlightcolor='black', highlightbackground='black')
a.grid(row=5, column=1)

Cardname = Label(form_frame, text='Card Name', font=('times', 20, 'bold'), fg='black', bg='white')
Cardname.grid(row=6, column=0, pady=10, padx=20)
name_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
name_entry.config(highlightcolor='black', highlightbackground='black')
name_entry.grid(row=6, column=1)

Cardnumber = Label(form_frame, text='Card Number', font=('times', 20, 'bold'), fg='black', bg='white')
Cardnumber.grid(row=7, column=0, padx=20, pady=10)
card_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', show='*', highlightthickness=1)
card_entry.config(highlightcolor='black', highlightbackground='black')
card_entry.grid(row=7, column=1)

Expirydate = Label(form_frame, text='Expiry Date', font=('times', 20, 'bold'), fg='black', bg='white')
Expirydate.grid(row=8, column=0, padx=20, pady=10)
expiry_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
expiry_entry.config(highlightcolor='black', highlightbackground='black')
expiry_entry.grid(row=8, column=1)

Cvv = Label(form_frame, text='CVV', font=('times', 20, 'bold'), fg='black', bg='white')
Cvv.grid(row=9, column=0, padx=20, pady=10)
cvv_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1, show='*')
cvv_entry.config(highlightcolor='black', highlightbackground='black')
cvv_entry.grid(row=9, column=1)

Amount = Label(form_frame, text='Amount', font=('times', 20, 'bold'), fg='black', bg='white')
Amount.grid(row=10, column=0, padx=20, pady=10)
amount_entry = Entry(form_frame, font=('times', 15, 'bold'), fg='black', bg='white', highlightthickness=1)
amount_entry.config(highlightcolor='black', highlightbackground='black')
amount_entry.grid(row=10, column=1)

# Buttons
submit_btn = Button(form_frame, text='Submit', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#55efc4', command=make_payment)
submit_btn.grid(row=11, column=1, sticky=W, padx=(30, 5))

clear_btn = Button(form_frame, text='Clear', border=0, padx=20, pady=5, font=("times", 10, 'bold'), fg='black', bg='#ff7675', command=clear_fields)
clear_btn.grid(row=11, column=1, sticky=E, padx=10)

w.mainloop()
