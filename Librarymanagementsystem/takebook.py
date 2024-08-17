from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta

def clear():
    n.delete(0, END)
    id.delete(0, END)
    bname.delete(0, END)
    bid.delete(0, END)
    a.delete(0, END)
    bill_label.config(text="")

def submit_form():
    studentid = id.get()
    studentname = n.get()
    bookid = bid.get()
    bookname = bname.get()
    author = a.get()

    # Current date as date_borrowed
    date_borrowed = datetime.now().date()

    # Assume due date is 14 days from the date borrowed
    due_date = date_borrowed + timedelta(days=14)

    # Check if any fields are empty
    if not studentid or not studentname or not bookid or not bookname or not author:
        messagebox.showerror("Error", "All fields are required")
        return

    db = None
    cur = None

    try:
        # Connect to the database
        db = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        cur = db.cursor()

        # Query to check if the book exists in `bookdetail`
        query = 'SELECT * FROM bookdetail WHERE bookid=%s AND bookname=%s AND author=%s'
        cur.execute(query, (bookid, bookname, author))
        res = cur.fetchall()

        # Query to check if the student exists in `register`
        query = 'SELECT * FROM register WHERE studentid=%s AND studentname=%s'
        cur.execute(query, (studentid, studentname))
        res1 = cur.fetchall()

        if res and res1:
            # Insert into `takebook` with `date_borrowed` and `due_date`
            query1 = '''INSERT INTO takebook (studentid, studentname, bookid, bookname, author, date_borrowed, due_date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            values = (studentid, studentname, bookid, bookname, author, date_borrowed, due_date)
            cur.execute(query1, values)
            db.commit()

            # Display the bill format
            win = Toplevel(w)
            win.geometry('600x500')
            bill_label = Label(win, text="", font=('times', 15, 'bold'), fg='black', bg='white', justify=LEFT)
            bill_label.pack()
            bill_text = (
                f"===== Library Bill =====\n"
                f"Student Name: {studentname}\n"
                f"Student ID: {studentid}\n"
                f"Book ID: {bookid}\n"
                f"Book Name: {bookname}\n"
                f"Author: {author}\n"
                f"Date Borrowed: {date_borrowed}\n"
                f"Due Date: {due_date}\n"
                f"========================"
            )
            bill_label.config(text=bill_text, padx=30, pady=10)
            b = Button(win, text='Save as PDF', font=('times', 10, 'bold'), padx=20, pady=20,
                       command=lambda: save_pdf(studentname, studentid, bookid, bookname, author, date_borrowed, due_date))
            b.pack()

        else:
            messagebox.showerror('Error', 'Book or student not found in the database')

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        if cur:
            cur.close()
        if db:
            db.close()

def save_pdf(studentname, studentid, bookid, bookname, author, date_borrowed, due_date):
    folder_selected = filedialog.askdirectory()

    if not folder_selected:
        messagebox.showerror("Error", "No folder selected")
        return

    filename = f"Library_Bill_{studentid}.pdf"
    filepath = f"{folder_selected}/{filename}"

    c = canvas.Canvas(filepath, pagesize=letter)
    c.drawString(100, 750, "===== Library Bill =====")
    c.drawString(100, 730, f"Student Name: {studentname}")
    c.drawString(100, 710, f"Student ID: {studentid}")
    c.drawString(100, 690, f"Book ID: {bookid}")
    c.drawString(100, 670, f"Book Name: {bookname}")
    c.drawString(100, 650, f"Author: {author}")
    c.drawString(100, 630, f"Date Borrowed: {date_borrowed}")
    c.drawString(100, 610, f"Due Date: {due_date}")
    c.drawString(100, 590, "========================")
    c.save()

    messagebox.showinfo("Success", f"Bill saved as {filename} in {folder_selected}")

w = Tk()
w.title('Take Book')
w.iconbitmap('homework_fJt_1.ico')
w.config(bg='white')
w.geometry("700x700")

# Create a frame to hold all entry fields and labels
main_frame = Frame(w, highlightbackground='black', highlightthickness=2, padx=10, pady=10, bg='white')
main_frame.pack(pady=20)

lab = Label(main_frame, text="Take Book", font=('times', 20, 'bold'), fg='black', bg='white')
lab.grid(row=0, column=0, columnspan=2, pady=10, sticky=S)

studentname = Label(main_frame, text='Studentname', font=('times', 20, 'bold'), fg='black', bg='white')
studentname.grid(row=2, column=0, padx=10, pady=10)

n = Entry(main_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
n.config(highlightcolor='black', highlightbackground='black')
n.grid(row=2, column=1, padx=20, pady=10)

studentid = Label(main_frame, text='Studentid', font=('times', 20, 'bold'), fg='black', bg='white')
studentid.grid(row=3, column=0, padx=10, pady=10)

id = Entry(main_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
id.config(highlightcolor='black', highlightbackground='black')
id.grid(row=3, column=1, padx=20, pady=10)

bookid = Label(main_frame, text='Bookid', font=('times', 20, 'bold'), fg='black', bg='white')
bookid.grid(row=4, column=0, padx=10, pady=10)

bid = Entry(main_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
bid.config(highlightcolor='black', highlightbackground='black')
bid.grid(row=4, column=1, padx=20, pady=20)

bookname = Label(main_frame, text='Bookname', font=("times", 20, 'bold'), fg='black', bg='white')
bookname.grid(row=5, column=0, padx=20, pady=10)

bname = Entry(main_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
bname.config(highlightcolor='black', highlightbackground='black')
bname.grid(row=5, column=1, padx=20, pady=20)

author = Label(main_frame, text='Author', font=("times", 20, 'bold'), fg='black', bg='white')
author.grid(row=6, column=0, padx=10, pady=10)

a = Entry(main_frame, width=20, font=('times', 15, 'bold'), highlightthickness=1)
a.config(highlightcolor='black', highlightbackground='black')
a.grid(row=6, column=1, padx=20, pady=20)

submit_button = Button(main_frame, text='Submit', border=0, padx=20, pady=5, fg='black', bg='#55efc4', command=submit_form)
submit_button.grid(row=7, column=1, sticky=W, padx=100)

clear_button = Button(main_frame, text='Clear', border=0, padx=20, pady=5, fg='black', bg='#ff7675', command=clear)
clear_button.grid(row=7, column=1, sticky=E, padx=10)

# Frame for displaying the bill
bill_frame = Frame(w, padx=10, pady=10, bg='white')
bill_frame.pack(pady=20)

w.mainloop()

