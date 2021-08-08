from tkinter import *

from PIL import ImageTk, Image

from gtts import gTTS
from playsound import playsound

import os

import speech_recognition as sr
import threading
import tkinter
from time import sleep
import mysql.connector
import gtts

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



TimeToAnswer=5

#window3 settings
window3 = Tk()
window3.configure(bg='pink')
window3.geometry("{0}x{1}+0+0".format(window3.winfo_screenwidth(), window3.winfo_screenheight()))
window3.title("ClearIt Interview")


#Question and answer words
ques = Label(window3, text="Text : ", bg='pink', font=("Times New Roman", 25)).place(x=22, y=460)
ans = Label(window3, text="your Audio : ", bg='pink', font=("Times New Roman", 25)).place(x=22, y=560)


rule1="1. please speak as written in textbox"
rule2="2. Ensure your sitting in quite place and there is no external disturbance"
rule3="3. Be clear while speaking, use of a microphone is suggested"
rule4="4. Once your result is declared you either retry or press next"


Rules = Label(window3, text="Audio Testing window", bg='pink', foreground="brown",font=("Times New Roman", 32)).place(x=14, y=80)

Rules = Label(window3, text=rule1, bg='pink', font=("Times New Roman", 18)).place(x=30, y=180)
Rules = Label(window3, text=rule2, bg='pink', font=("Times New Roman", 18)).place(x=30, y=230)
Rules = Label(window3, text=rule3, bg='pink', font=("Times New Roman", 18)).place(x=30, y=280)
Rules = Label(window3, text=rule4, bg='pink', font=("Times New Roman", 18)).place(x=30, y=330)


#QuestionBox
quesT = Text(window3,bg='white', relief='flat', height=5, width=120)
quesT.place(x=210, y=460)

#AnswerBox
ansT = Text(window3,bg='white', relief='flat', height=5, width=120)
ansT.place(x=210, y=550)

#interviewBot
ClearIT_text = Label(window3, text="ClearIt :", bg='pink', foreground="brown",font=("Times New Roman", 50, "bold")).place(x=520, y=30)
InterviewBot_text = Label(window3, text="InterviewBot", bg='pink',foreground="brown", font=("Times New Roman", 50, "bold")).place(x=620, y=100)

#adding logo
logo = Image.open("ClearIT [Logo].png")
test = ImageTk.PhotoImage(logo)
label_logo = tkinter.Label(image=test)
label_logo.image = test
label_logo.place(x=1200, y=60)


#Cosine Function
def cos(Original, User):
    # Oringal answer put into variable X and User answer in variable Y
    X=str(Original)
    Y= str(User)

    #printing variable X and Variable Y
    #print("Your answer is : ", X)
    #print("Original answer is : ",Y)

    X_list = word_tokenize(X) #Tokenization of X
    Y_list = word_tokenize(Y) #Tokenization of Y

    # stopwords in english are stored in sw
    sw = stopwords.words('english')

    # 2 lists are made 1 for X and other for Y
    l1 = []; l2 = []

    X_set = {w for w in X_list if not w in sw} #
    Y_set = {w for w in Y_list if not w in sw}

    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    print("similarity: ", cosine)
    return cosine


#Function for listening audio from user
def listen():
    #print("Say something")
    r = sr.Recognizer()
    #print("recognizing...")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=TimeToAnswer)
        text = r.recognize_google(audio_data)
        print(text)
    return text


def mainloop():
    testing_text = "I will clear the interview"
    QuesLabel = Label(window3, text=testing_text, bg='white', font=("Times New Roman", 25))  # prints question
    QuesLabel.place(x=210, y=460)
    UserAnswer = listen()
    AnsLabel = Label(window3, text=UserAnswer, bg='white', font=("Times New Roman", 25))
    AnsLabel.place(x=220, y=560)
    UserAnswer = str(UserAnswer)
    CosineVal = cos(UserAnswer, testing_text)  # cos value stored in CosineVal
    CosineString = str(CosineVal)
    print(CosineVal)
    if (CosineVal > 0.6):
        Result = Label(window3, text="Audio test Success", bg='pink', font=("Times New Roman", 40))  # prints question
        Result.place(x=1000, y=660)
        print("audio test successfull")
        next3.config(state='normal')
    else:
        Result = Label(window3, text="Audio test Failed", bg='pink', font=("Times New Roman", 40))  # prints question
        Result.place(x=1000, y=660)
        print(" audio test unsucessful")


Mainloop = tkinter.Button(window3, text="", background="pink", relief="flat", height=4, width=8, fg="white", command=threading.Thread(target=mainloop).start()).place(x=1200, y=560)



def retry():
    window3.after(500, lambda: Result.destroy())
    threading.Thread(target=mainloop).start()

retry= Button(window3, text="Retry", background="orange", relief="flat", height=4, width=8, fg="white", command= retry)
retry.place(x=1200, y=560)


def Cameratesting():
    os.system('Camera_Testing.py')

next3 = Button(window3, text="Next", background="orange", height=2, width=7, fg="white" , command=Cameratesting)
next3.place(x=840, y=700)
next3.config(state='disable')        #initially next button is disabled

quit = Button(window3, text="Quit", background="Red", height=2, width=7, fg="white", command=window3.destroy)
quit.place(x=500, y=700)

window3.mainloop()
