from tkinter import *
from tkinter import messagebox
import tkinter
import os
import threading
from PIL import Image, ImageTk


window1= Tk()        #creating parent window
window1.geometry("{0}x{1}+0+0".format(window1.winfo_screenwidth(), window1.winfo_screenheight()))      #for full screen geometry of parent window
window1.configure(bg='pink')         #setting background colour
window1.title("Registration Form")   #title of parent window

logo = Image.open("ClearIT [Logo].png")
test = ImageTk.PhotoImage(logo)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1200, y=50)

Label(window1, text="Welcome to ClearIt Mock Interview", bg='pink', font=("Times New Roman", 25)).place(x=480, y=100)
Label(window1, text="Instructions:", bg='pink', font=("Times New Roman", 20)).place(x=220, y=170)
Label(window1, text="1. Please ensure you have a valid internet connection. ", bg='pink', font=("Times New Roman", 15)).place(x=200, y=220)
Label(window1, text="2. Turn on your microphone and camera.", bg='pink', font=("Times New Roman", 15)).place(x=200,y=270)
Label(window1, text="3. Questions to be answered within 40 sec.", bg='pink', font=("Times New Roman", 15)).place(x=200, y=320)
Label(window1, text="4. At the end of interview process a report will be mailed on to your registered email ID.", bg='pink',font=("Times New Roman", 15)).place(x=200, y=370)
Label(window1, text="5. Kindly fill in the Feedback form, link will be mailed to you after interview", bg='pink', font=("Times New Roman", 15)).place(x=200, y=420)
Label(window1, text="ALL THE BEST", bg='pink', font=("Times New Roman", 20)).place(x=650, y=500)

checkbox ="The personal details provided and camera-audio inputs will be solely be used for interview purposes and not shared with any 3rd party"

Label(window1, text= checkbox, bg='pink', font=("Times New Roman", 16)).place(x=350, y=600)

Value = IntVar()


def window2():
    os.system('window2.py')

next2 = Button(window1, text="Next", background="orange", height=2, width=7, fg="white", command=lambda : window2())
next2.place(x=750, y=700)
quit = Button(window1, text="Quit", background="Red", height=2, width=7, fg="white", command=window1.destroy)
quit.place(x=500, y=700)

next2.config(state='disable')
def check():
    if (Value.get() == 1) :
        next2.config(state='normal')
    else :
        next2.config(state='disable')
        messagebox.showerror("Error", "Please check I Agree box ")
        next2.config(state='disable')

c1 = Checkbutton(window1, text='i agree',font=("algerian", 12),variable=Value,onvalue=1, offvalue=0, height=5, width=5, activebackground='Orange', bg='Pink', command=check)
c1.place(relx = 0.17,rely = 0.79,anchor='sw')

window1.mainloop()