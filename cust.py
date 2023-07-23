from tkinter import*
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox


class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_ref = StringVar()
        x = random.randint(1000, 2000)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 20, "bold"), fg="gold", bg="black", relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer details", font=("times new roman", 14, "bold"), padx=2,)
        lblframeleft.place(x=5, y=50, width=425, height=490)

        lbl_cust_ref = Label(lblframeleft, text="Customer Ref:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(lblframeleft, width=29, textvariable=self.var_ref, font=("times new roman", 13, "bold"), cursor="hand2", state="readonly")
        enty_ref.grid(row=0, column=1)

        cname = Label(lblframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(lblframeleft, width=29, textvariable=self.var_cust_name, font=("times new roman", 13, "bold"), cursor="hand2")
        txtcname.grid(row=1, column=1)

        mname = Label(lblframeleft, text="Mother Name:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        mname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(lblframeleft, width=29, textvariable=self.var_mother, font=("times new roman", 13, "bold"), cursor="hand2")
        txtmname.grid(row=2, column=1)

        lblpostcode = Label(lblframeleft, text="Post Code:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblpostcode.grid(row=4, column=0, sticky=W)

        txtpostcode = ttk.Entry(lblframeleft, width=29, textvariable=self.var_post, font=("times new roman", 13, "bold"), cursor="hand2")
        txtpostcode.grid(row=4, column=1)

        label_gender = Label(lblframeleft, font=("times new roman", 13, "bold"), text="Gender:", padx=2, pady=6, cursor="hand2")
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(lblframeleft, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        lblmob = Label(lblframeleft, text="Mobile:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblmob.grid(row=5, column=0, sticky=W)

        txtmob = ttk.Entry(lblframeleft, textvariable=self.var_mobile, width=29, font=("times new roman", 13, "bold"), cursor="hand2")
        txtmob.grid(row=5, column=1)

        lblemail = Label(lblframeleft, text="E-Mail:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)

        txtemail = ttk.Entry(lblframeleft, width=29, textvariable=self.var_email, font=("times new roman", 13, "bold"), cursor="hand2")
        txtemail.grid(row=6, column=1)

        lblnationality = Label(lblframeleft, text="Nationality:", font=("times new roman", 14, "bold"), padx=2, pady=6, cursor="hand2")
        lblnationality.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(lblframeleft, textvariable=self.var_nationality, font=("times new roman", 13, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ("Indian", "American", "Nepali")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        lblidproof = Label(lblframeleft, text="Id-Proof:", font=("times new roman", 14, "bold"), padx=2, pady=6, cursor="hand2")
        lblidproof.grid(row=8, column=0, sticky=W)
        combo_idproof = ttk.Combobox(lblframeleft, textvariable=self.var_id_proof, font=("times new roman", 13, "bold"), width=27, state="readonly")
        combo_idproof["value"] = ("Adhaar", "Pan", "Passport", "Driving Licence")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)

        lblidnumber = Label(lblframeleft, text="Id-Number:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblidnumber.grid(row=9, column=0, sticky=W)

        txtidnumber = ttk.Entry(lblframeleft, textvariable=self.var_id_number, width=29, font=("times new roman", 13, "bold"), cursor="hand2")
        txtidnumber.grid(row=9, column=1)

        lbladdress = Label(lblframeleft, text="Address:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbladdress.grid(row=10, column=0, sticky=W)

        txtaddress = ttk.Entry(lblframeleft, textvariable=self.var_address, width=29, font=("times new roman", 13, "bold"), cursor="hand2")
        txtaddress.grid(row=10, column=1)

        btn_frame = Frame(lblframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=410, width=412, height=40)

        btnadd = Button(btn_frame, text="ADD", command=self.add_data, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="UPDATE", command=self.update, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, text="DELETE", command=self.mdelete, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="RESET", command=self.reset, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnreset.grid(row=0, column=3, padx=1)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 14, "bold"), padx=2, )
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblsearch = Label(Table_Frame, text="SEARCH BY:", font=("times new roman", 14, "bold"), bg="black", fg="gold")
        lblsearch.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("times new roman", 13, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_idsearch = StringVar()
        txtidsearch = ttk.Entry(Table_Frame, textvariable=self.txt_idsearch, width=29, font=("times new roman", 13, "bold"), cursor="hand2")
        txtidsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(Table_Frame, command=self.serach, text="SEARCH", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(Table_Frame, command=self.fetch_data, text="SHOW ALL", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnshowall.grid(row=0, column=4, padx=1)

        details_table = LabelFrame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=("ref", "name","mother", "gender", "post", "mobile",
                                              "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="Post Code")
        self.Cust_Details_Table.heading("mobile", text="Mobile No")
        self.Cust_Details_Table.heading("email", text="E-Mail")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="ID-Proof")
        self.Cust_Details_Table.heading("idnumber", text="ID-No")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)


        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mother.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_ref.get(), self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                    self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                    self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get()))
                con.commit()
                self.fetch_data()
                con.close()

                messagebox.showinfo("Success", "Customer added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select * from customer")
        row = cur.fetchall()
        if len(row)!= 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in row:
                self.Cust_Details_Table.insert("", END, values=i)
            con.commit()
        con.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "please enter mobile number", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="register")
            cur = con.cursor()
            cur.execute("update customer set Name=%s, Mother=%s, Gender=%s, Postcode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s where ref=%s", (
                                                                    self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                                                                    self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                                                                    self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get(),  self.var_ref.get()))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success", "Update Successfully done", parent=self.root)

    def mdelete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this details", parent=self.root)
        if mdelete>0:
            con = pymysql.connect(host="localhost", user="root", password="root", database="register")
            cur = con.cursor()
            query = "delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            cur.execute(query, value)
        else:
            if not mdelete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        # self.var_ref.set(""),
          self.var_cust_name.set(""),
          self.var_mother.set(""),
        # self.var_gender.set(""),
          self.var_post.set(""),
          self.var_mobile.set(""),
          self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
          self.var_id_number.set(""),
          self.var_address.set("")

          x = random.randint(1000, 2000)
          self.var_ref.set(str(x))

    def serach(self):
        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_idsearch.get())+"%'")
        row = cur.fetchall()
        if len(row)!= 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            con.commit()
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
