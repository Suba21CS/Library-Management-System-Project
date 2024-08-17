from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def insertentry():
    selected_item = t.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'No item selected')
        return

    selected_values = t.item(selected_item, 'values')
    studentid, studentname, bookid, bookname, author = selected_values

    try:
        mysqlcon = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()

        query = '''
        SELECT * FROM addbook WHERE studentid=%s AND studentname=%s 
        AND bookid=%s AND bookname=%s AND author=%s
        '''
        mycursor.execute(query, (studentid, studentname, bookid, bookname, author))
        res = mycursor.fetchone()

        if res:
            print("Matching entry found. Attempting to insert into bookdetail.")
            print(f"Inserting: BookID={bookid}, BookName={bookname}, Author={author}")

            insert_query = '''
            INSERT INTO bookdetail (bookid, bookname, author)
            VALUES (%s, %s, %s)
            '''
            mycursor.execute(insert_query, (bookid, bookname, author))
            mysqlcon.commit()

            messagebox.showinfo('Message', 'Entry inserted successfully!')

            t.delete(selected_item)
        else:
            messagebox.showerror('Error', 'No matching entry found in addbook')

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        if mycursor:
            mycursor.close()
        if mysqlcon:
            mysqlcon.close()


# Set up the Tkinter window
w = Tk()
w.geometry('800x500')
w.title('Student Add Book Detail')
w.iconbitmap('homework_fJt_1.ico')

# Frame for the Treeview and button
f = Frame(w)
f.pack(fill=BOTH, expand=True)

# Treeview for displaying book details
insert_button = Button(f, text="Insert Selected Entry", border=0, command=insertentry, padx=20, pady=10, bg='#34e7e4', font=('Helvetica', 10, 'bold'), fg='black')
insert_button.pack(pady=10)
t = ttk.Treeview(f)

# Set up Treeview style
s = ttk.Style(w)
s.theme_use('clam')
s.configure('.', font=('Helvetica', 9))
s.configure('Treeview.Heading', foreground='#f53b57', font=('Helvetica', 11, 'bold'))

# Define Treeview columns
t['columns'] = ('Studentid', 'Studentname', 'Bookid', 'Bookname', 'Author')
t.column("#0",width=0,stretch=NO)
t.column('#1', width=150)
t.column('#2', width=150)
t.column('#3', width=150)
t.column('#4', width=150)
t.column('#5', width=150)

t.heading('#1', text='Student ID')
t.heading('#2', text='Student Name')
t.heading('#3', text='Book ID')
t.heading('#4', text='Book Name')
t.heading('#5', text='Author')

# Populate Treeview with data from `addbook` table
try:
    mysqlcon = mysql.connector.connect(
        host='localhost', port=3306, user='suba', password='suba123', database='lib')
    mycursor = mysqlcon.cursor()

    query = "SELECT studentid, studentname, bookid, bookname, author FROM addbook"
    mycursor.execute(query)
    res = mycursor.fetchall()

    for i, row in enumerate(res):
        t.insert('', i, values=row)

except mysql.connector.Error as err:
    messagebox.showerror('Error', f'Error: {err}')
finally:
    if mycursor:
        mycursor.close()
    if mysqlcon:
        mysqlcon.close()

t.pack()

# Button to insert selected entry


w.mainloop()
