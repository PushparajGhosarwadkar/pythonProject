from tkinter import *
from tkinter import messagebox
import os
import sys
import tkinter
import threading
from PIL import Image, ImageTk
import math
#import labelchange

parent= Tk()        #creating parent window
parent.geometry("{0}x{1}+0+0".format(parent.winfo_screenwidth(), parent.winfo_screenheight()))      #for full screen geometry of parent window
parent.configure(bg='pink')         #setting background colour
parent.title("Internet Speed Test")   #title of parent window

#interviewBot
ClearIT_text = Label( text="ClearIt :", bg='pink', foreground="brown",font=("Times New Roman", 50, "bold")).place(x=520, y=30)
InterviewBot_text = Label( text="InterviewBot", bg='pink',foreground="brown", font=("Times New Roman", 50, "bold")).place(x=620, y=100)

logo = Image.open("ClearITFinal.png")
test = ImageTk.PhotoImage(logo)
label_logo = tkinter.Label(image=test)
label_logo.image = test
label_logo.place(x=1050, y=10)

l0= Label(parent, text="Internet Speed Test", bg= 'pink',foreground="brown" ,width=20, font=("Times New Roman",32))    #creating labels
l0.place(x=14, y=80)       #placing label to appropriate position

Label(text="Instructions:", bg='pink', font=("Times New Roman", 20)).place(x=220, y=170)
Label(text="1. Please ensure you have a Stable Internet connectivity. ", bg='pink', font=("Times New Roman", 15)).place(x=200, y=220)
Label(text="2. Internet connectivity : 2 Mbps un-interrupted internet speed is desirable with sufficient data.", bg='pink', font=("Times New Roman", 15)).place(x=200,y=270)

#logo1 = Image.open("wifi.png")
#test1 = ImageTk.PhotoImage(logo1)
#label2 = tkinter.Label(image=test1)
#label2.image = test1
#label2.place(x=520, y=170)

#Speed check
import speedtest
from speedtest import *
def speed():
    st = speedtest.Speedtest()
    z=st.download()
    k=math.trunc(z)
    #s = "{:.2}".format(z)
    state = Label(parent, text=("{:.2e}".format(k)), bg='pink', foreground="brown", width=15,font=("Times New Roman", 20)).place(x=520, y=440)
    Label(parent, text="Speed : (In Mbps)", bg='pink', foreground="brown", width=20, font=("Times New Roman", 20)).place(x=500,y=400)

    if z > 2000000000:  # 2mbps speed


        name = Label(parent, bg='pink', text="Sufficient Speed",foreground="brown" ,font=("Times New Roman", 22)).place(x=550, y=350)
        # Label(parent, text="Speed :", bg='pink', foreground="brown", width=10, font=("Times New Roman", 20)).place(x=450,y=440)
        messagebox.showinfo("Internet", "Internet Test Successful")
    else:

        name = Label(parent, bg='pink', text="Insufficient Speed",foreground="brown" , font=("Times New Roman", 22)).place(x=550, y=350)
        # Label(parent, text="Speed :", bg='pink', foreground="brown", width=10, font=("Times New Roman", 20)).place(x=490,y=440)
        messagebox.showerror("Error", "Please Check Your Internet Connectivity")

'''
#Label(parent, text="Speed :", bg='pink',foreground="brown" , width=20, font=("Times New Roman", 20)).place(x=700,y=440)
# creating labels
#st = speedtest.Speedtest()
#z=st.download()
#state= Label(parent, text=round(st.download(),3), bg= 'pink', width=20, font=("Times New Roman",20)).place(x=500, y=400)    #creating labels
'''



speed()
exit= Button(parent, text= "Exit", background="red", height=1, width=5, fg="white",command= parent.destroy)    #creating a buttton to exit the window
exit.place(x=600, y=620)

#function to add a new window
#function to add a new window
def openNewWindow():
    parent.destroy()
    newwindow= Tk()     #toplevel widget is used to create a window on top of parent window

    newwindow.configure(bg='pink')
    newwindow.geometry("{0}x{1}+0+0".format(newwindow.winfo_screenwidth(), newwindow.winfo_screenheight()))
    Label(newwindow, text= "Welcome to ClearIt Mock Interview",bg= 'pink', font=("Times New Roman",25)).place(x=480, y=100)


    def nw():
        os.system('python labelchange.py')
    next = Button(newwindow, text="Next", background="blue", height=1, width=5, fg="white", command= nw)
    next.place(x=720, y=620)
    newwindow.mainloop()

def retry_funct():
    parent.after(1000, lambda: state.destroy())
    speed()


#function to add user data into db
#button= Button(parent, text="Submit", height=1, width=10, command= 0, background= "green", fg="white")       #creating submit button
#button.place(x=640, y=580)

retry= Button(parent, text="Retry", height=1, width=5, background= "green", fg="white",command= retry_funct)
retry.place(x=660, y=580)
next = Button(parent, text="Next", background="blue", height=1, width=5, fg="white", command=openNewWindow)    #creating next button
next.place(x=720, y=620)

#next.config(state='disable')        #initially next button is disabled
parent.mainloop()       #this method listens event such as button clicks etc until window is closed