from tkinter import *
w=Tk()
w.geometry("900x500")
w.title('admin')
w.iconbitmap('homework_fJt_1.ico')
f=Frame(w)
f.pack()

def addbook():
    import adminaddbook

def studentdetail():
    import studentdetail

def bookdetail():
    import adminbookdetail

def returnbook():
    import Returnbookdetail

def takebook():
    import takebookdetail

def studentaddbook():
    import studentaddbookdetails

def issue():
    import issuebookdetail
def latereturnbook():
    import latereturnbookdetail




b1=Button(f,text="Students detail",border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=studentdetail)
b1.grid(row=1,column=0,padx=10,pady=70)
b=Button(f,text="Takebook",width='13',height='1',border=0,font=('times',20,'bold'),fg='white',bg='#30336b',command=takebook)
b.grid(row=1,column=1,padx=30,pady=70)

b2=Button(f,text='Addbook',border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=addbook)
b2.grid(row=1,column=2,padx=10,pady=70)

b3=Button(f,text="book detail",border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=bookdetail)
b3.grid(row=2,column=0,pady=10)
b4=Button(f,text="Addbook detail",border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=studentaddbook)
b4.grid(row=2,column=1,padx=30,pady=10)
b5=Button(f,text="Issuebook",border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=issue)
b5.grid(row=2,column=2,padx=10,pady=10)
b6=Button(f,text='Returnbook',border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=returnbook)
b6.grid(row=3,column=0,pady=70,padx=(0, 15),columnspan=2)
b7=Button(f,text='Latereturnbook',border=0,width='13',height='1',font=('times',20,'bold'),fg='white',bg='#30336b',command=latereturnbook)
b7.grid(row=3,column=1,pady=70, padx=(15, 0),columnspan=3)
w.mainloop()