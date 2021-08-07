import os
from tkinter import *
from playsound import playsound
from PIL import ImageTk, Image
import cv2
import speech_recognition as sr
import docx
import threading
import tkinter
from time import sleep
import mysql.connector
import gtts
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

QuestionNo=3
TimeToAnswer=2
delay=TimeToAnswer+2

#object of docx
mydoc = docx.Document()

#window3 settings
window3 = Tk()
window3.configure(bg='pink')
window3.geometry("{0}x{1}+0+0".format(window3.winfo_screenwidth(), window3.winfo_screenheight()))
window3.title("ClearIt Interview")


def video():
    # Create a label in the frame camera capture
    app = Frame(window3, bg="white")
    app.place(x=900, y=10)
    lmain = Label(app)
    lmain.grid()

    #resolution 300*300
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)


    def video_stream():
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #conversion from brg to rgb
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, video_stream)

    video_stream()


#connection to DB
mydb = mysql.connector.connect(host='localhost', user='root', passwd='12345', database='nlp')

#Question and answer text
ques = Label(window3, text="Question : ", bg='white', font=("Times New Roman", 25)).place(x=22, y=360)
ans = Label(window3, text="Answer : ", bg='white', font=("Times New Roman", 25)).place(x=22, y=560)

#QuestionBox
quesT = Text(window3,bg='white', relief='flat', height=5, width=120)
quesT.place(x=210, y=350)

#AnswerBox
ansT = Text(window3,bg='white', relief='flat', height=5, width=120)
ansT.place(x=210, y=550)

#Cosine Function
def cos(Original, User):
    X=str(Original) #Oringal answer put into variable X
    Y= str(User) #Oringal answer put into variable Y

    print("Your answer is : ", X)  #Printing X
    print("Original answer is : ",Y) #Printing Y

    X_list = word_tokenize(X) #Tokenization of X
    Y_list = word_tokenize(Y) #Tokenization of Y

    sw = stopwords.words('english') #stopwords in english are stored in sw

    l1 = []; l2 = [] #2 lists are made 1 for X and other for Y

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

'''
for x in range (5):
    counter = 5

    def counter_label(label):
        counter = 5

        def count():
            global counter
            counter -= 1
            label.config(text=str(counter))
            label.after(1000, count)
            if(counter==0):
                window3.after(1000, lambda: label.destroy())
        count()
        counter =5

    #label for counter
    label = Label(window3, bg="pink",font=("Helvetica", 45), height=3, width=3)
    label.place(relx = 0.92,rely = 0.84, anchor='se')
    counter_label(label)
    x=0
    sleep(1)
    x=x+1
'''

#counter loop
#threading.Thread(target=counter_label(label)).start()
#sleep(5)
#window3.after(1000, lambda: label.destroy())
#threading.Thread(target=counter_label(label)).start()



def info():
    mycur = mydb.cursor()
    name = "SELECT Name FROM tableone ORDER BY srno DESC LIMIT 1;"
    mycur.execute(name)
    data = mycur.fetchone()
    mydoc.add_heading(data, 0)
    email = "SELECT email FROM tableone ORDER BY srno DESC LIMIT 1;"
    mycur.execute(email)
    data2 = mycur.fetchone()
    mydoc.add_heading(data2, 0)
    department = "SELECT department FROM tableone ORDER BY srno DESC LIMIT 1;"
    mycur.execute(department)
    data3 = mycur.fetchone()
    mydoc.add_heading(data3, 0)
    mydoc.save("Name.docx")

info()

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

#label list

QuestionsList = []
ActualAnswersList =[]

#playing text as audio
def mainloop():
    global i
    for i in range(QuestionNo):
        mycursor = mydb.cursor()
        query = "SET @result= (SELECT Questions FROM questionsdb ORDER BY RAND() LIMIT 1);"
        mycursor.execute(query)
        query2 = "SELECT @result;"
        mycursor.execute(query2)
        ques = mycursor.fetchone()
        QuestionsList.append(ques)
        print(ques)
        SelectAnswerQuery = "SELECT ActualAnswer FROM questionsdb WHERE questions= @result;"
        mycursor.execute(SelectAnswerQuery)
        ans = mycursor.fetchone()
        ActualAns = str(ans)
        ActualAnswersList.append(ActualAns)

    i = 0

    def update():
        global i
        if (i<=QuestionNo):
            QuesLabel = Label(window3, text=QuestionsList[i], bg='white', font=("Times New Roman", 25)) #prints question
            QuesLabel.place(x=210, y=350)

            tts = gtts.gTTS(str(QuestionsList[i])) #test to speech progress
            tts.save("QuestionsList[i].mp3") #saves tts file
            sleep(delay)
            playsound("QuestionsList[i].mp3") #plays the tts
            #print(str(labels[i]))
            os.remove("QuestionsList[i].mp3")
            UserAnswer = listen()

            AnsLabel = Label(window3, text=UserAnswer, bg='white', font=("Times New Roman", 25))
            AnsLabel.place(x=220, y=560)

            window3.after(1000, lambda : QuesLabel.destroy())
            window3.after(1000, lambda: AnsLabel.destroy())
            window3.after(1000, update)

            CosineVal=cos(UserAnswer, ActualAns) #cos value stored in CosineVal
            CosineString=str(CosineVal)

            mydoc.add_paragraph(QuestionsList[i]) #able to write answers
            mydoc.add_paragraph(ActualAnswersList[i])
            mydoc.add_paragraph(UserAnswer)
            mydoc.add_paragraph(CosineString)
            mydoc.save("name.docx")

            i = i + 1
        else:
            next.config(state='normal')  # is active only when all the questions r done
            final = "Interview is over Please press Next"
            tts = gtts.gTTS(str(final))
            tts.save("final.mp3")
            label5 = Label(window3, text=str(final), bg='white', font=("Times New Roman", 18))
            label5.place(x=250, y=365)
            playsound("final.mp3")

    update()  # recalls the update function


video = tkinter.Button(window3, text="", background="pink", relief="flat", height=1, width=1, fg="white", command=threading.Thread(target=video).start()).place(x=400, y=500)
Mainloop = tkinter.Button(window3, text="", background="pink", relief="flat", height=1, width=1, fg="white", command=threading.Thread(target=mainloop).start()).place(x=400, y=500)

def window4():
    os.system('window4.py')

next4 = Button(window3, height=2, width=7,text="Next", background="orange", fg="white",command=lambda : threading.Thread(target=window4).start())
next4.place(x=950, y=700)
next4.config(state='disable')

quit = Button(window3, text="Quit", background="Red", height=2, width=7, fg="white", command=window3.destroy)
quit.place(x=500, y=700)

window3.mainloop()