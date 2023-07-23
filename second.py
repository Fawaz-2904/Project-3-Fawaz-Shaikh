from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pymysql
from hotel import HotelManagementSystem


class Login:
    def __init__(self, root, login_frame=None):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #self.bg = ImageTk.PhotoImage(file="D:\images\login.jpg")
        #bg=Label(self.root,image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)


        #login frame
        Frame_login=Frame(self.root, bg="gray")
        Frame_login.place(x=150, y=150, height=390, width=500)


        title=Label(Frame_login, text="LOGIN HERE", font=("Impact", 35, "bold"), fg="#d11220", bg="gray").place(x=90, y=30)
        desc = Label(Frame_login, text="STUDENT LOGIN", font=("Goudy old style", 20, "bold"), fg="#d12230", bg="gray").place(x=90, y=100)

        lbl_email = Label(Frame_login, text="E-MAIL", compound=LEFT, font=("Goudy old style", 15, "bold"), fg="black", bg="gray").place(x=90, y=140)
        self.txt_email = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="PASSWORD", font=("Goudy old style", 15, "bold"), fg="black", bg="gray").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn = Button(Frame_login, text="FORGET PASSWORD ?",cursor="hand2", command=self.forget_function, bg="gray",fg="#d11220",bd=0, font=("times new roman", 12)).place(x=90, y=280)
        Login_btn = Button(self.root,command=self.login_function, cursor="hand2", text="LOGIN", fg="darkgray", bg="#d11220", font=("times new roman", 20)).place(x=160, y=515, width=180, height=40)
        register_btn = Button(self.root,command=self.register_window, cursor="hand2", text="REGISTER", fg="darkgray",bg="#d11220", font=("times new roman", 20)).place(x=455, y=515, width=180, height=40)

        self.var_chk = IntVar()
        self.chk = Checkbutton(Frame_login, text = "I Agree the T&C", variable=self.var_chk, onvalue = 1, offvalue = 0, bg = "gray", font = ("times new roman", 12)).place(x=90, y=310)

    def forget_password(self):
        if self.cmb_question.get() == "Select" or self.txt_answer.get() == "" or self.txt_new.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("select * from student where email=%s and question=%s and answer=%s",
                            (self.txt_email.get(), self.cmb_question.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please select the correct security question / Enter answer",
                                         parent=self.root)

                else:
                    cur.execute("update student set password=%s where email=%s",
                                (self.txt_new.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Password Reset successfully done", parent=self.root)
                    self.root.destroy()
                    import second
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)


    def forget_function(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter email to reset password", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("select * from student where email=%s", self.txt_email.get())
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please enter valid email to reset password", parent=self.root)

                else:
                    con.close()
                    self.root = Tk()
                    self.root.title("FORGOT PASSWORD")
                    self.root.geometry("1199x600+100+50")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    Frame_forgot = Frame(self.root, bg="light blue")
                    Frame_forgot.place(x=150, y=120, height=440, width=600)

                    title = Label(Frame_forgot, text="Forgot Password??", font=("Impact", 35, "bold"), fg="#d11220", bg="lightblue").place(x=90, y=25)

                    lbl_question = Label(Frame_forgot, text="SECURITY QUESTION", font=("Goudy old style", 20, "bold"), fg="black", bg="lightblue").place(x=90, y=130)
                    self.cmb_question = ttk.Combobox(Frame_forgot, font=("times new roman", 13), state='readonly',
                                                     justify=CENTER)
                    self.cmb_question['values'] = ("Select", "Your School Name", "Your College Name", "Your favourite destination")
                    self.cmb_question.place(x=90, y=170, width=350, height=35)
                    self.cmb_question.current(0)

                    lbl_answer = Label(Frame_forgot, text="ANSWER", font=("Goudy old style", 20, "bold"), fg="black", bg="lightblue").place(x=90, y=215)
                    self.txt_answer = Entry(Frame_forgot, font=("times new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=90, y=255, width=350, height=35)

                    lbl_new = Label(Frame_forgot, text="NEW PASSWORD", font=("Goudy old style", 20, "bold"), fg="black", bg="lightblue").place(x=90, y=300)
                    self.txt_new = Entry(Frame_forgot, font=("times new roman", 15), bg="lightgray")
                    self.txt_new.place(x=90, y=340, width=350, height=35)

                    reset_btn = Button(Frame_forgot, cursor="hand2", text="RESET PASSWORD", command=self.forget_password, fg="white", bg="#d11220", font=("times new roman", 20)).place(x=165, y=400, width=270, height=40)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login_function(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree the T&C", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("select * from student where email=%s and password=%s", (self.txt_email.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Credentials", parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    #import hotel
                con.close()


            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    #def hotel_window(self):
        #self.new_window = Toplevel(self.root)
        #self.app = HotelManagementSystem(self.new_window)


root = Tk()
obj = Login(root)
root.mainloop()
