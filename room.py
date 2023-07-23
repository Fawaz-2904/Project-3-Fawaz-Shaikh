from tkinter import*
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import pymysql
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_contact = StringVar()
        self.var_checkindate = StringVar()
        self.var_checkoutdate = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomAvailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 20, "bold"), fg="gold", bg="black", relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking details", font=("times new roman", 14, "bold"), padx=2, )
        lblframeleft.place(x=5, y=50, width=425, height=490)

        lbl_cust_contact = Label(lblframeleft, text="Customer Contact:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(lblframeleft, width=20, textvariable=self.var_contact, font=("times new roman", 13, "bold"), cursor="hand2")
        enty_contact.grid(row=0, column=1, sticky=W)

        check_in = Label(lblframeleft, text="Check In date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in.grid(row=1, column=0, sticky=W)

        txtcheck_in = ttk.Entry(lblframeleft, width=27, textvariable=self.var_checkindate, font=("times new roman", 13, "bold"), cursor="hand2")
        txtcheck_in.grid(row=1, column=1)

        check_out = Label(lblframeleft, text="Check Out date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out.grid(row=2, column=0, sticky=W)

        txtcheck_out = ttk.Entry(lblframeleft, width=27, textvariable=self.var_checkoutdate, font=("times new roman", 13, "bold"), cursor="hand2")
        txtcheck_out.grid(row=2, column=1)

        label_Room_Type = Label(lblframeleft, font=("times new roman", 13, "bold"), text="Room Type:", padx=2, pady=6, cursor="hand2")
        label_Room_Type.grid(row=3, column=0, sticky=W)

        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select RoomType from details")
        ide = cur.fetchall()

        combo_Room_Type = ttk.Combobox(lblframeleft, font=("times new roman", 13, "bold"), textvariable=self.var_roomtype, width=25, state="readonly")
        combo_Room_Type["value"] = ide
        combo_Room_Type.current(0)
        combo_Room_Type.grid(row=3, column=1)

        lblavailable = Label(lblframeleft, text="Available Rooms:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblavailable.grid(row=4, column=0, sticky=W)

        #txtavailable = ttk.Entry(lblframeleft, width=27, textvariable=self.var_roomavailable, font=("times new roman", 13, "bold"), cursor="hand2")
        #txtavailable.grid(row=4, column=1)

        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select RoomNo from details")
        row = cur.fetchall()
        combo_RoomNo = ttk.Combobox(lblframeleft, font=("times new roman", 13, "bold"), textvariable=self.var_roomAvailable, width=25, state="readonly")
        combo_RoomNo["value"] = row
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        lblmeal = Label(lblframeleft, text="Meal:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblmeal.grid(row=5, column=0, sticky=W)

        txtmeal = ttk.Entry(lblframeleft, width=27, textvariable=self.var_meal, font=("times new roman", 13, "bold"), cursor="hand2")
        txtmeal.grid(row=5, column=1)

        lblNoofdays = Label(lblframeleft, text="No of Days:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblNoofdays.grid(row=6, column=0, sticky=W)

        txtNoofdays = ttk.Entry(lblframeleft, width=27, textvariable=self.var_noofdays, font=("times new roman", 13, "bold"), cursor="hand2")
        txtNoofdays.grid(row=6, column=1)

        lblpaidtax = Label(lblframeleft, text="Paid Tax:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblpaidtax.grid(row=7, column=0, sticky=W)

        txtpaidtax = ttk.Entry(lblframeleft, width=27, textvariable=self.var_paidtax, font=("times new roman", 13, "bold"), cursor="hand2")
        txtpaidtax.grid(row=7, column=1)

        lblSubtotal = Label(lblframeleft, text="Sub Total:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lblSubtotal.grid(row=8, column=0, sticky=W)

        txtSubtotal = ttk.Entry(lblframeleft, width=27, textvariable=self.var_subtotal, font=("times new roman", 13, "bold"), cursor="hand2")
        txtSubtotal.grid(row=8, column=1)

        lbltotal = Label(lblframeleft, text="Total Cost:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbltotal.grid(row=9, column=0, sticky=W)

        txttotal = ttk.Entry(lblframeleft, width=27, textvariable=self.var_total, font=("times new roman", 13, "bold"), cursor="hand2")
        txttotal.grid(row=9, column=1)

        btnfetch = Button(lblframeleft, text="Fetch Data", command=self.Fetch_contact, font=("times new roman", 10, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnfetch.place(x=347, y=4)

        btnbill = Button(lblframeleft, command=self.total, text="Bill", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnbill.grid(row=10, column=0, padx=1, sticky=W)

        btn_frame = Frame(lblframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=410, width=412, height=40)

        btnadd = Button(btn_frame, command=self.add_data, text="ADD", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, command=self.update, text="UPDATE", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, command=self.mdelete, text="DELETE", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, command=self.reset, text="RESET", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnreset.grid(row=0, column=3, padx=1)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 14, "bold"), padx=2, )
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblsearch = Label(Table_Frame, text="SEARCH BY:", font=("times new roman", 14, "bold"), bg="black", fg="gold")
        lblsearch.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("times new roman", 13, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Contact", "Room No")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_idsearch = StringVar()
        txtidsearch = ttk.Entry(Table_Frame, textvariable=self.txt_idsearch, width=29, font=("times new roman", 13, "bold"), cursor="hand2")
        txtidsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(Table_Frame, command=self.search, text="SEARCH", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(Table_Frame, command=self.fetch_data, text="SHOW ALL", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnshowall.grid(row=0, column=4, padx=1)

        details_table = LabelFrame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_Table = ttk.Treeview(details_table, columns=("contact", "checkindate", "checkoutdate", "roomtype", "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkindate", text="Check-In")
        self.room_Table.heading("checkoutdate", text="Check-Out")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("roomavailable", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noofdays", text="No of Days")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkindate", width=100)
        self.room_Table.column("checkoutdate", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.column("roomavailable", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noofdays", width=100)
        self.room_Table.pack(fill=BOTH, expand=1)

        self.room_Table.pack(fill=BOTH, expand=1)

        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkindate.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                self.var_contact.get(),
                                                                                self.var_checkindate.get(),
                                                                                self.var_checkoutdate.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomAvailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()
                                                                                 ))
                con.commit()
                self.fetch_data()
                con.close()

                messagebox.showinfo("Success", "Room Booked Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select * from room")
        row = cur.fetchall()
        if len(row)!= 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in row:
                self.room_Table.insert("", END, values=i)
            con.commit()
        con.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_Table.focus()
        content = self.room_Table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkindate.set(row[1]),
        self.var_checkoutdate.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomAvailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "please enter mobile number", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="register")
            cur = con.cursor()
            cur.execute( "update room set checkindate=%s, checkoutdate=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s where contact=%s",
                (
                    self.var_checkindate.get(),
                    self.var_checkoutdate.get(),
                    self.var_roomtype.get(),
                    self.var_roomAvailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success", "Update Successfully done", parent=self.root)

    def mdelete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this details", parent=self.root)
        if mdelete > 0:
            con = pymysql.connect(host="localhost", user="root", password="root", database="register")
            cur = con.cursor()
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            cur.execute(query, value)
        else:
            if not mdelete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkindate.set(""),
        self.var_checkoutdate.set(""),
        #self.var_roomtype.set(""),
        self.var_roomAvailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_subtotal.set(""),
        self.var_total.set("")

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact Details", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="register")
            cur = con.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get())
            cur.execute(query, value)
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Number not found", parent=self.root)
            else:
                con.commit()
                con.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=455, y=75, width=300, height=180)

                lblName = Label(showDataframe, text="Name:", font=("times new roman", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl.place(x=90, y=0)

                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get())
                cur.execute(query, value)
                row = cur.fetchone()

                lblgender = Label(showDataframe, text="Gender:", font=("times new roman", 12, "bold"))
                lblgender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl2.place(x=90, y=30)

                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get())
                cur.execute(query, value)
                row = cur.fetchone()

                lblemail = Label(showDataframe, text="Email:", font=("times new roman", 12, "bold"))
                lblemail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl3.place(x=90, y=60)

                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get())
                cur.execute(query, value)
                row = cur.fetchone()

                lblnationality = Label(showDataframe, text="Nationality:", font=("times new roman", 12, "bold"))
                lblnationality.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl4.place(x=90, y=90)

                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get())
                cur.execute(query, value)
                row = cur.fetchone()

                lbladdress = Label(showDataframe, text="Address:", font=("times new roman", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbl5 = Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl5.place(x=90, y=120)

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select * from room where "+str(self.search_var.get())+"LIKE '%"+str(self.txt_idsearch.get())+"%'")
        row = cur.fetchall()
        if len(row)!= 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in row:
                self.room_Table.insert("", END, values=i)
            con.commit()
        con.close()


    def total(self):
        inDate = self.var_checkindate.get()
        outDate = self.var_checkoutdate.get()
        inDate = datetime.strptime(inDate, "%d/%m/%y")
        outDate = datetime.strptime(outDate, "%d/%m/%y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_roomtype.get() == "Luxury" and self.var_meal.get() == "Lunch"):
            q1 = float(400)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f"% ((q5)*0.09))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_roomtype.get() == "Double" and self.var_meal.get() == "Dinner"):
            q1 = float(400)
            q2 = float(650)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()