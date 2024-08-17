from tkinter import ttk
from tkinter.ttk import Progressbar
import os
from tkinter import *
from tkinter import PhotoImage

w = Tk()
w.title('library')
w.iconbitmap('homework_fJt_1.ico')

frame=Frame(w)
frame.grid(row=0,column=0,columnspan=3)

# Create a Label widget to display the image
wid=1100
height=550
sw=w.winfo_screenwidth()
sh=w.winfo_screenheight()
x=(sw/2)-(wid/2)
y=(sh/2)-(height/2)
w.geometry('%dx%d+%d+%d' %(wid,height,x,y))

w.iconbitmap('homework_fJt_1.ico')

photo=PhotoImage(file=(r"C:\Users\subas\Downloads\libraryimg (1).png"))
l=Label(frame,image=photo)
l.pack()
frame1=Frame(w,highlightbackground='white',highlightthickness=2)
frame1.grid(row=0,column=0,sticky=N)
# Create a Label widget to display the image
l2=Label(frame1,text='Library Management System',font=('times',20,'bold'),padx=20,pady=10,bg='white',fg='black')
l2.pack()
photo1=PhotoImage(file=(r"C:\Users\subas\OneDrive\Pictures\little lib.png"))
l1=Label(frame1,image=photo1)
l1.pack()
progress_label=Label(frame1,text='Loading...',font=("Trubuchet Ms",13,'bold'),fg='blue',bg='white')
progress_label.place(x=190,y=330)
progress=ttk.Style()
progress.configure('red.horizontal.TProgressbar',background='gray')
progress =Progressbar(frame1,orient=HORIZONTAL,length=400,mode='determinate',style='red.Horizontal.TProgressbar')
progress.place(x=60,y=370)
def top():
    w.withdraw()
    os.system('python view.py')
    w.destroy()
i=0
def load():
    global i
    if i<=10:
        txt='Loading...'+(str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(600,load)
        progress['value']=10*i
        i +=1
    else:
        top()
load()


# Use place method to position the Label widget


w.mainloop()

