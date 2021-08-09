from tkinter import *
from tkinter import messagebox
import tkinter
import os
import threading
from PIL import Image, ImageTk

window2 = Tk()  # creating parent window
window2.geometry("{0}x{1}+0+0".format(window2.winfo_screenwidth(),window2.winfo_screenheight()))  # for full screen geometry of parent window
window2.configure(bg='pink')  # setting background colour
window2.title("ClearIt Interview")  # title of parent window


logo = Image.open("ClearIT [Logo].png")
test = ImageTk.PhotoImage(logo)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1250, y=50)


E1 = StringVar()  # creating instance of class StringVar
E2 = StringVar()
E3 = StringVar()
E7 = StringVar()
l0 = Label(window2, text="Enter Your Details Here", bg='pink', width=20, font=("Times New Roman", 25))  # creating labels
l0.place(x=500, y=60)  # placing label to appropriate position
name = Label(window2, bg='pink', text="Name: ", font=("algerian", 12)).place(x=80, y=130)
email = Label(window2, bg='pink', text="Email : ", font=("algerian", 12)).place(x=80, y=180)
department = Label(window2, bg='pink', text="Department : ", font=("algerian", 12)).place(x=80, y=230)
Projects = Label(window2, bg='pink', text="Projects Undertaken : ", font=("algerian", 12)).place(x=80, y=280)
technical_skills = Label(window2, bg='pink', text="Technical Skills : ", font=("algerian", 12)).place(x=80, y=340)
internship = Label(window2, bg='pink', text="Internships : ", font=("algerian", 12)).place(x=80, y=410)
int1 = Label(window2, bg='pink', text="(eg.projects/technology worked on) ").place(x=80, y=430)
hobbies = Label(window2, bg='pink', text="Hobbies : ", font=("algerian", 12)).place(x=80, y=480)

e1 = Entry(window2, textvariable=E1, width=133)  # creating a entry widget
e1.place(x=350, y=130)  # placing it at appropriate postion
e2 = Entry(window2, textvariable=E2, width=133)
e2.place(x=350, y=180)
e3 = Entry(window2, textvariable=E3, width=133)
e3.place(x=350, y=230)

text1 = Text(window2, height=1, width=100)  # creating text widget to support multi line entries
text1.place(x=350, y=280)
text2 = Text(window2, height=1, width=100)
text2.place(x=350, y=340)
text3 = Text(window2, height=1, width=100)
text3.place(x=350, y=410)

e7 = Entry(window2, textvariable=E7, width=133)
e7.place(x=350, y=480)


def add_data():
    a1= E1.get()       #storing data entered by user into entry field in a1
    a2= E2.get()
    a3= E3.get()
    a4= text1.get("1.0", END)   #storing data entered by user into text widget in a4
    a5= text2.get("1.0", END)
    a6= text3.get("1.0", END)
    a7= E7.get()

    if(a1 and a2 and a3 and a4 and a5 and a6 and a7):
        Submit.config(state='normal')       #enabling submit button if all the entries are filled
        next3.config(state='normal')         #enabling next button
        messagebox.showinfo("information","Records inserted successfully")  #dialog box will appear to assure candiate that data has been stored successfully
        print("saved")
    else:
        Submit.config(state='disable')      #if all fields are not empty submit button will be disabled
        messagebox.showerror("Error", "Please enter all the fields")  #dialog box
        Submit.config(state='normal')

Submit= Button(window2, text="Submit", height=5, width=15, command= add_data, background= "green", fg="white")       #creating submit button
Submit.place(x=640, y=580)

def window3():
    os.system('window3.py')

next3 = Button(window2, text="Next", background="orange", height=2, width=7, fg="white" , command=window3)
next3.place(x=840, y=700)
next3.config(state='disable')        #initially next button is disabled

quit = Button(window2, text="Quit", background="Red", height=2, width=7, fg="white", command=window2.destroy)
quit.place(x=500, y=700)

window2.mainloop()
