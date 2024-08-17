from tkinter import *

w = Tk()
w.geometry("800x600")
w.configure(bg='skyblue')
w.title('library')
w.iconbitmap('homework_fJt_1.ico')

frame1 = Frame(w, bg='skyblue', width=1000, height=600)
frame1.grid(row=0, column=0)
def student():
    import Registeration
def admin():
    import adminlogin

# Load the first image
photo = PhotoImage(file=r"C:\Users\subas\Downloads\ad.png")
l = Label(frame1, image=photo)
l.grid(row=0, column=0, padx=130, pady=(150, 20))

# Load the second image


# Admin button
b = Button(frame1, text='Admin', border=0,bg='blue', fg='black', font=('times', 20, 'bold'), padx=20, pady=5,command=admin)
b.grid(row=1, column=0, pady=(0, 50))  # Adjusted padding to move the button up
photo1 = PhotoImage(file=r'C:\Users\subas\OneDrive\Pictures\student.png')
l1 = Label(frame1, image=photo1)
l1.grid(row=0, column=1, padx=(10,30) ,pady=(150, 20))
b1 = Button(frame1, text='Student',border=0, bg='blue', fg='black', font=('times', 20, 'bold'), padx=20, pady=5,command=student)
b1.grid(row=1, column=1, pady=(0, 50))


w.mainloop()

