from tkinter import *
from tkinter import ttk
import mysql.connector

w = Tk()
w.geometry('800x500')
w.title('Student Details')
w.iconbitmap('homework_fJt_1.ico')

# Connect to the database
db = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
cur = db.cursor()

# Query to fetch student details
query = 'SELECT studentid, studentname, phone, regdate FROM register'
cur.execute(query)
res = cur.fetchall()

# Frame and button (if you want to add buttons or additional frames, you can place them here)

# Treeview for displaying student details
t = ttk.Treeview(w)
t['show'] = 'headings'
s = ttk.Style(w)
s.theme_use('clam')
s.configure('.', font=('Helvetica', 9))
s.configure('Treeview.Heading', foreground='#f53b57', font=('Helvetica', 11, 'bold'))
t['columns'] = ('Studentid', 'Studentname', 'Phone', 'Register Date')
t.column('#0', width=150)
t.column('#1', width=150)
t.column('#2', width=150)
t.column('#3', width=150)

t.heading('#1', text='Student ID')
t.heading('#2', text='Student Name')
t.heading('#3', text='Phone Number')
t.heading('#4', text='Register Date')

# Insert data into Treeview
for i, row in enumerate(res):
    t.insert('', i, values=(row[0], row[1], row[2], row[3]))

t.pack()

# Close the cursor and connection
cur.close()
db.close()

w.mainloop()
