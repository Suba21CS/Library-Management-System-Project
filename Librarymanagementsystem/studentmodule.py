from tkinter import *
w=Tk()
w.geometry("900x500")
w.iconbitmap('homework_fJt_1.ico')
f=Frame(w)
f.pack()
def availablebook():
    import Availablebook
def returnbook():
    import Returnbook
def addbook():
    import addbook

def issuebook():
    import issuebook
def latereturnbook():
    import returnbookpayment
def logout():
    import logout
b=Button(f,text="Available book",width='13',height='1',border=0,font=('times',20,'bold'),padx=20,pady=5,fg='black',bg='#34ace0',command=availablebook)
b.grid(row=1,column=0,padx=10,pady=80)
b1=Button(f,text="Add book",border=0,width='13',height='1',font=('times',20,'bold'),padx=20,pady=5,fg='black',bg='#34ace0',command=addbook)
b1.grid(row=1,column=1,padx=10,pady=80)
b2=Button(f,text="Return book",border=0,width='13',height='1',font=('times',20,'bold'),padx=20,pady=5,fg='black',bg='#34ace0',command=returnbook)
b2.grid(row=1,column=2,padx=10,pady=80)
b3=Button(f,text="Issue book",border=0,width='13',height='1',font=('times',20,'bold'),padx=20,pady=5,fg='black',bg='#34ace0',command=issuebook)
b3.grid(row=2,column=0)
b3=Button(f,text="Fine Payment",border=0,width='13',height='1',font=('times',20,'bold'),padx=20,pady=5,fg='black',bg='#34ace0',command=latereturnbook)
b3.grid(row=2,column=1)

b4=Button(f,text="Logout",border=0,width='13',height='1',font=('times',20,'bold'),padx=20,pady=5,fg='black',bg='#34ace0',command=logout)
b4.grid(row=2,column=2,columnspan=3)




w.mainloop()