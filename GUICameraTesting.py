from tkinter import *
from PIL import ImageTk, Image
import cv2
from gtts import gTTS
from docx2pdf import convert
import numpy as np

import pandas as pd
import os
from playsound import playsound
import speech_recognition as sr
import threading
import tkinter
from time import sleep
import mysql.connector
import gtts


import docx
from docx.shared import Inches
from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt




#object of docx
mydoc = docx.Document()

#window3 settings
window3 = Tk()
window3.configure(bg='pink')
window3.geometry("{0}x{1}+0+0".format(window3.winfo_screenwidth(), window3.winfo_screenheight()))
window3.title("ClearIt Interview")



#interviewBot
ClearIT_text = Label(window3, text="ClearIt :", bg='pink', foreground="brown",font=("Times New Roman", 50, "bold")).place(x=520, y=30)
InterviewBot_text = Label(window3, text="InterviewBot", bg='pink',foreground="brown", font=("Times New Roman", 50, "bold")).place(x=620, y=100)

Window3_title = Label(window3, text="Camera Testing window", bg='pink', foreground="brown",font=("Times New Roman", 32)).place(x=14, y=80)


rule1="1. Ensure there is atleast 70-80% of face cover on the camera"
rule2="2. Remove all the unnesessary background and look into the camera"
rule3="3. Once you are satisfied with please press next"

Rules = Label(window3, text="Camera Testing window", bg='pink', foreground="brown",font=("Times New Roman", 32)).place(x=14, y=80)

Rules = Label(window3, text=rule1, bg='pink', font=("Times New Roman", 22)).place(x=30, y=350)
Rules = Label(window3, text=rule2, bg='pink', font=("Times New Roman", 22)).place(x=30, y=400)
Rules = Label(window3, text=rule3, bg='pink', font=("Times New Roman", 22)).place(x=30, y=450)



#adding logo
logo = Image.open("ClearIT [Logo].png")
test = ImageTk.PhotoImage(logo)
label_logo = tkinter.Label(image=test)
label_logo.image = test
label_logo.place(x=1200, y=10)


# Create a label in the frame camera capture
app = Frame(window3, bg="pink")
app.place(x=850, y=280)
lmain = Label(app)
lmain.grid()

#resolution 720*720
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #conversion from brg to rgb
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

video_stream()

def window4():
    os.system('window3.py')

next4 = Button(window3, height=2, width=7,text="Next", background="orange", fg="white")
next4.place(x=550, y=650)

quit = Button(window3, text="Quit", background="Red", height=2, width=7, fg="white",command=window3.destroy)
quit.place(x=200, y=650)

window3.mainloop()