from tkinter import *
from tkinter import ttk
import mysql.connector

w = Tk()
w.geometry('1000x500')
w.title('returnbookdetail')
w.iconbitmap('homework_fJt_1.ico')

# Connect to the database
db = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
cur = db.cursor()

# Query to fetch book details
query = 'SELECT * FROM returnbook'
cur.execute(query)
res = cur.fetchall()

# Frame and button
f = Frame(w)
f.pack()



# Treeview for displaying book details

t = ttk.Treeview(w)
t['show']='headings'
s=ttk.Style(w)
s.theme_use('clam')
s.configure('.',font=('Helvetica',9))
s.configure('Treeview.Heading',foreground='#f53b57',font=('Helvetica',11,'bold'))
t['columns'] = ('Studentid','Studentname', 'Bookid', 'Bookname', 'Author','Return Date')
t.column('#0', width=0, stretch=NO)
t.column('#1', width=150)
t.column('#2', width=150)
t.column('#3', width=150)
t.column('#4', width=150)
t.column('#5',width=150)
t.column('#6',width=150)
t.heading('#1',text='Studentid')
t.heading('#2', text='Studentname')
t.heading('#3', text='Bookid')
t.heading('#4', text='Bookname')
t.heading('#5', text='Author')
t.heading('#6', text='Return Date')



# Insert data into Treeview
i = 0
for row in res:
    t.insert('', i, text='', values=(row[0], row[1], row[2],row[3],row[4],row[5]))
    i += 1

t.pack()

w.mainloop()





