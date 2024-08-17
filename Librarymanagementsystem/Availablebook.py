from tkinter import *
from tkinter import ttk
import mysql.connector

w = Tk()
w.title('availablebook')
w.geometry('800x500')
w.iconbitmap('homework_fJt_1.ico')
def take():
    import takebook

# Connect to the database
db = mysql.connector.connect(host='localhost', port=3306, user='suba', password='suba123', database='lib')
cur = db.cursor()

# Query to fetch book details
query = 'SELECT  sno,bookid,bookname,author FROM bookdetail'
cur.execute(query)
res = cur.fetchall()

# Frame and button
f = Frame(w)
f.pack()
b = Button(f, text="Take Book", border=0, font=('times', 10, 'bold'), bg='#686de0', fg='white', padx=20, pady=5,command=take)
b.grid(pady=10)


# Treeview for displaying book details

t = ttk.Treeview(w)
t['show']='headings'
s=ttk.Style(w)
s.theme_use('clam')
s.configure('.',font=('Helvetica',9))
s.configure('Treeview.Heading',foreground='#f53b57',font=('Helvetica',11,'bold'))
t['columns'] = ('S.no', 'Bookid', 'Bookname', 'Author')
t.column('#0', width=0, stretch=NO)
t.column('#1', width=150)
t.column('#2', width=150)
t.column('#3', width=150)
t.column('#4', width=150)
t.heading('#1', text='S.no')
t.heading('#2', text='Bookid')
t.heading('#3', text='Bookname')
t.heading('#4', text='Author')



# Insert data into Treeview
i = 0
for row in res:
    t.insert('', i, text='', values=(row[0], row[1], row[2],row[3]))
    i += 1

t.pack()

w.mainloop()





