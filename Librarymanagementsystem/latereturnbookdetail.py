from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

def insertentry():
    selected_item = t.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'No item selected')
        return

    # Get the values from the selected row
    selected_values = t.item(selected_item, 'values')
    studentid, studentname, bookid, bookname, author, payment_date = selected_values

    # Assuming the current date as the return date
    return_date = datetime.now().date()

    try:
        mysqlcon = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()

        # Check if the selected row exists in the `payments` table
        query = '''
        SELECT * FROM payments WHERE studentid=%s AND studentname=%s 
        AND bookid=%s AND bookname=%s AND author=%s AND payment_date=%s
        '''
        mycursor.execute(query, (studentid, studentname, bookid, bookname, author, payment_date))
        res = mycursor.fetchone()

        if res:
            # Insert the record into `returnbook` table
            insert_query = '''
            INSERT INTO returnbook (bookid, bookname, author, return_date)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            bookname=VALUES(bookname), author=VALUES(author), return_date=VALUES(return_date)
            '''
            mycursor.execute(insert_query, (bookid, bookname, author, return_date))
            mysqlcon.commit()

            messagebox.showinfo('Message', 'Entry inserted successfully!')

            # Remove the item from Treeview
            t.delete(selected_item)
        else:
            messagebox.showerror('Error', 'No matching entry found in payments')

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        mycursor.close()
        mysqlcon.close()

# Set up the Tkinter window
w = Tk()
w.geometry('800x500')
w.title('Student Payment Detail')
w.iconbitmap('homework_fJt_1.ico')

# Frame and button
f = Frame(w)
f.pack()

# Treeview for displaying book details
t = ttk.Treeview(w, show='headings')

# Set up Treeview style
s = ttk.Style(w)
s.theme_use('clam')
s.configure('.', font=('Helvetica', 9))
s.configure('Treeview.Heading', foreground='#f53b57', font=('Helvetica', 11, 'bold'))

# Define Treeview columns
t['columns'] = ('Studentid', 'Studentname', 'Bookid', 'Bookname', 'Author', 'Payment_date')
t.column('#0', width=0, stretch=NO)
t.column('#1', width=150)
t.column('#2', width=150)
t.column('#3', width=150)
t.column('#4', width=150)
t.column('#5', width=150)
t.column('#6', width=150)

t.heading('#1', text='Studentid')
t.heading('#2', text='Studentname')
t.heading('#3', text='Bookid')
t.heading('#4', text='Bookname')
t.heading('#5', text='Author')
t.heading('#6', text='Payment_date')

# Populate Treeview with data from `payments` table
try:
    mysqlcon = mysql.connector.connect(
        host='localhost', port=3306, user='suba', password='suba123', database='lib')
    mycursor = mysqlcon.cursor()

    query = "SELECT studentid, studentname, bookid, bookname, author, payment_date FROM payments"
    mycursor.execute(query)
    res = mycursor.fetchall()

    for i, row in enumerate(res):
        t.insert('', i, values=row)

except mysql.connector.Error as err:
    messagebox.showerror('Error', f'Error: {err}')
finally:
    mycursor.close()
    mysqlcon.close()

t.pack()

# Button to insert selected entry
insert_button = Button(f, text="Insert Selected Entry", border=0, command=insertentry, padx=20, pady=10, bg='#34e7e4', font=('Helvetica', 10, 'bold'), fg='black')
insert_button.pack(pady=10)

w.mainloop()
