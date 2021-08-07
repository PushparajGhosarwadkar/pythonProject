from tkinter import *
import tkinter.messagebox
import tkinter.font as font
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from docx2pdf import convert
from PIL import Image, ImageTk


#convert(r"report.docx",r"report.pdf")
#print('docx to pdf converted')

def send_mail():
    Sender_Email = "beprojectece@gmail.com"
    Reciever_Email = "beproject@gmail.com"
    Password = "pisaproject"

    newMessage = EmailMessage()
    newMessage['Subject'] = "Test Mail"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Thank you for having interview with us.. '
                           '\n Please fill the feedback form  : https://forms.gle/NuSYfi4kbmxoaaev5'
                           '\n Thanks and Regards '
                           '\n Team CleatIT')
    files = ['report.pdf']

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
    print('mail successfully sent')

master=tkinter.Tk()
master.title("place() method")
master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
master.configure(bg='pink')


logo = Image.open("ClearIT [Logo].png")
test = ImageTk.PhotoImage(logo)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=150, y=480)


Mail=tkinter.Button(master, text="Mail Report", height=5, width=12, command= lambda : send_mail(), background= "green", fg="white", font=("Times New Roman", 15)).place(x=700, y=500)
Quit=tkinter.Button(master, text="Quit", height=3, width=10, command= master.destroy, background= "red", fg="white").place(x=720, y=650)

text1= """Thank you for having your mock interview with us.
Hope you enjoyed the experience. We wish you a very successful career.

Please click on the below button, to get your interview report mailed to your Email ID."""

text= Label(master, text=text1, bg= 'pink', height=10, width=80, font=("Times New Roman",25)).place(x=100, y=40)
master.mainloop()