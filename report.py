from tkinter import*
import smtplib

master = Tk()
master.title("Report")
master.geometry("1295x550+230+220")

def send():
    try:
        email=temp_Email.get()
        password=temp_Password.get()
        to=temp_receiver.get()
        subject=temp_Subject.get()
        body=temp_Body.get()
        if email == "" or password == "" or to == "" or subject == "" or body == "":
            notif.config(text="Error sending email", fg = "red")
            return
        else:
            finalMessage = "Subject: {}\n\n{}".format(subject, body)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, to, finalMessage)
            notif.config(text="Email has been sent", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")

def reset():
    EmailEntry.delete(0, "end")
    PasswordEntry.delete(0, "end")
    receiverEntry.delete(0, "end")
    SubjectEntry.delete(0, "end")
    BodyEntry.delete(0, "end")

lbl_title = Label(master, text="Report", font=("times new roman", 25), fg="gold", bg="black", relief=RIDGE)
lbl_title.place(x=0, y=350, width=1295, height=50)

lbl_desc = Label(master, text="Use the form above to send an email", font=("times new roman", 20), fg="gold", bg="black", relief=RIDGE)
lbl_desc.place(x=0, y=400, width=1295, height=50)

lbl_email = Label(master, text="Email:", font=("times new roman", 30, "bold"), padx=2, pady=6)
lbl_email.grid(row=0, sticky=W, padx=5)

lbl_pass = Label(master, text="Password:", font=("times new roman", 30, "bold"), padx=2, pady=6)
lbl_pass.grid(row=0, column=10, sticky=E, padx=5)

lbl_to = Label(master, text="To:", font=("times new roman", 30, "bold"), padx=2, pady=6)
lbl_to.grid(row=10, sticky=W, padx=5)

lbl_subject = Label(master, text="Subject:", font=("times new roman", 30, "bold"), padx=2, pady=6)
lbl_subject.grid(row=10, column=10, sticky=E, padx=5)

lbl_body = Label(master, text="Body:", font=("times new roman", 30, "bold"), padx=2, pady=6)
lbl_body.grid(row=20, sticky=W, padx=5)

notif = Label(master, text="", font=("times new roman", 30, "bold"), padx=2, pady=6)
notif.grid(row=22, sticky=S, padx=5)

temp_Email = StringVar()
temp_Password = StringVar()
temp_receiver = StringVar()
temp_Subject = StringVar()
temp_Body = StringVar()

EmailEntry = Entry(master, width=29,  textvariable=temp_Email, font=("times new roman", 18, "bold"))
EmailEntry.grid(row=0, column=1, sticky=W)

PasswordEntry = Entry(master, width=29, show="*", textvariable=temp_Password, font=("times new roman", 18, "bold"))
PasswordEntry.grid(row=0, column=12, sticky=E)

receiverEntry = Entry(master, width=29, textvariable=temp_receiver, font=("times new roman", 18, "bold"))
receiverEntry.grid(row=10, column=1, sticky=W)

SubjectEntry = Entry(master, width=29, textvariable=temp_Subject, font=("times new roman", 18, "bold"))
SubjectEntry.grid(row=10, column=12, sticky=E)

BodyEntry = Entry(master, width=45, textvariable=temp_Body, font=("times new roman", 18, "bold"))
BodyEntry.grid(row=20, column=1, sticky=W)

btn_send = Button(master, text="Send", command=send, font=("times new roman", 20, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
btn_send.grid(row=40, column=1, padx=1)
btn_reset = Button(master, text="Reset", command=reset, font=("times new roman", 20, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
btn_reset.grid(row=40, column=10, padx=1)

master.mainloop()