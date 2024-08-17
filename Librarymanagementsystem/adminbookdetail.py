from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def delete_selected_entry():
    selected_item = t.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'No item selected')
        return

    # Get the values from the selected row
    selected_values = t.item(selected_item, 'values')
    bookid, bookname, author = selected_values

    try:
        mysqlcon = mysql.connector.connect(
            host='localhost', port=3306, user='suba', password='suba123', database='lib')
        mycursor = mysqlcon.cursor()

        # Check if the selected row exists in the `returnbook` table
        query = '''
        SELECT * FROM issuebook
        WHERE  bookid=%s AND bookname=%s AND author=%s
        '''
        mycursor.execute(query, ( bookid, bookname, author))
        res = mycursor.fetchall()

        if res:
            # Delete the row from `takebook` if a match is found in `returnbook`
            delete_query = '''
            DELETE FROM bookdetail
            WHERE  bookid=%s AND bookname=%s AND author=%s
            '''
            mycursor.execute(delete_query, (bookid, bookname, author))
            mysqlcon.commit()
            messagebox.showinfo('Message', 'Matching entry deleted successfully!')

            # Remove the item from Treeview
            t.delete(selected_item)
        else:
            messagebox.showerror('Error', 'No matching entry found in returnbook')

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error: {err}')
    finally:
        mycursor.close()
        mysqlcon.close()

# Set up the Tkinter window
w = Tk()
w.geometry('800x500')
w.title('adminaddbookdetail')
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
t['columns'] = ('Bookid', 'Bookname', 'Author')
t.column('#0', width=0, stretch=NO)
t.column('#1', width=150)
t.column('#2', width=150)
t.column('#3', width=150)


t.heading('#1', text='Bookid')
t.heading('#2', text='Bookname')
t.heading("#3", text='Author')

# Populate Treeview with data from `takebook` table
try:
    mysqlcon = mysql.connector.connect(
        host='localhost', port=3306, user='suba', password='suba123', database='lib')
    mycursor = mysqlcon.cursor()

    query = "SELECT bookid, bookname, author FROM bookdetail"
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

# Button to delete selected entry
delete_button = Button(f, text="Delete Selected Entry", command=delete_selected_entry, bg='#ff7675', fg='black')
delete_button.pack(pady=10)

w.mainloop()