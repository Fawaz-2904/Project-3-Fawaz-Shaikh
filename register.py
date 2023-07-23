from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql  # pip install pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("REGISTER")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True, True)

        # register frame
        Frame_register = Frame(self.root, bg="lightgreen")
        Frame_register.place(x=480, y=100, height=500, width=700)

        title = Label(Frame_register, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="blue", bg="lightgreen").place(x=90, y=20)

        lbl_first = Label(Frame_register, text="FIRST NAME", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=90, y=90)
        self.txt_first = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_first.place(x=90, y=120, width=250)

        lbl_last = Label(Frame_register, text="LAST NAME", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=370, y=90)
        self.txt_last = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_last.place(x=370, y=120, width=250)

        lbl_contact = Label(Frame_register, text="CONTACT No.", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=90, y=170)
        self.txt_contact = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=90, y=200, width=250)

        lbl_email = Label(Frame_register, text="E-MAIL", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=370, y=170)
        self.txt_email = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        lbl_question = Label(Frame_register, text="SECURITY QUESTION", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=90, y=250)
        self.cmb_question = ttk.Combobox(Frame_register, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_question['values'] = ("Select", "Your School Name", "Your College Name", "Your favourite destination")
        self.cmb_question.place(x=90, y=280, width=250)
        self.cmb_question.current(0)

        lbl_answer = Label(Frame_register, text="ANSWER", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=370, y=250)
        self.txt_answer = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=280, width=250)

        lbl_pass = Label(Frame_register, text=" PASSWORD", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=90, y=330)
        self.txt_pass = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=360, width=250)

        lbl_confirm = Label(Frame_register, text="CONFIRM PASSWORD", font=("Goudy old style", 15, "bold"), fg="black", bg="lightgreen").place(x=370, y=330)
        self.txt_confirm = Entry(Frame_register, font=("times new roman", 15), bg="lightgray")
        self.txt_confirm.place(x=370, y=360, width=250)

        self.var_chk = IntVar()
        self.chk = Checkbutton(Frame_register, text="I Agree the T&C", variable=self.var_chk, onvalue=1, offvalue=0, bg="lightgreen", font=("times new roman", 15)).place(x=90, y=420)

        register_btn = Button(Frame_register, cursor="hand2", command=self.register_data, text="REGISTER", fg="white", bg="#d11220", font=("times new roman", 25)).place(x=240, y=460, width=230, height=40)
        Login_btn = Button(self.root, cursor="hand2", text="SIGN IN",command=self.login_window, fg="white", bg="#d11220", font=("times new roman", 25)).place(x=200, y=460, width=230, height=40)

    def clear(self):
        self.txt_first.delete(0, END)
        self.txt_last.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0, END)
        self.txt_confirm.delete(0, END)

    def login_window(self):
        self.root.destroy()
        import second

    def register_data(self):
        if self.txt_first.get() == "" or self.txt_last.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.txt_answer.get() == "" or self.txt_pass.get() == "" or self.txt_confirm.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get() != self.txt_confirm.get():
            messagebox.showerror("Error", "Password's aren't matching", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree the T&C", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("select * from student where email=%s", self.txt_email.get())
                row = cur.fetchone()
                print(row)
                cur.execute("insert into student (first,last,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_first.get(),
                             self.txt_last.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmb_question.get(),
                             self.txt_answer.get(),
                             self.txt_pass.get()
                             ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
                self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
root = Tk()
obj = Register(root)
root.mainloop()
