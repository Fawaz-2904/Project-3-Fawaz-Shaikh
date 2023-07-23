from tkinter import*
from tkinter import ttk
import random
from time import strptime
from datetime import datetime
import pymysql
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        lbl_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 20, "bold"), fg="gold", bg="black", relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room details", font=("times new roman", 14, "bold"), padx=2, )
        lblframeleft.place(x=5, y=50, width=540, height=350)

        lbl_floor = Label(lblframeleft, text="Floor:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        enty_floor = ttk.Entry(lblframeleft, textvariable=self.var_floor, width=20, font=("times new roman", 13, "bold"), cursor="hand2")
        enty_floor.grid(row=0, column=1, sticky=W)

        lbl_RoomNo = Label(lblframeleft, text="Room No:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomNo = StringVar()
        enty_RoomNo = ttk.Entry(lblframeleft, textvariable=self.var_roomNo, width=20, font=("times new roman", 13, "bold"), cursor="hand2")
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        lbl_RoomType = Label(lblframeleft, text="Room Type:", font=("times new roman", 14, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_RoomType = StringVar()
        enty_RoomType = ttk.Entry(lblframeleft, textvariable=self.var_RoomType, width=20, font=("times new roman", 13, "bold"), cursor="hand2")
        enty_RoomType.grid(row=2, column=1, sticky=W)

        btn_frame = Frame(lblframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnadd = Button(btn_frame, text="ADD", command=self.add_data, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="UPDATE", command=self.update, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, command=self.mdelete, text="DELETE", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="RESET", command=self.reset_data, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9, cursor="hand2")
        btnreset.grid(row=0, column=3, padx=1)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text=" Show Room Details", font=("times new roman", 14, "bold"), padx=2 )
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_Details_Table = ttk.Treeview(Table_Frame,
                                       columns=("floor", "roomno", "roomType"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_Details_Table.xview)
        scroll_y.config(command=self.room_Details_Table.yview)

        self.room_Details_Table.heading("floor", text="Floor")
        self.room_Details_Table.heading("roomno", text="Room No")
        self.room_Details_Table.heading("roomType", text="Room Type")
        self.room_Details_Table["show"] = "headings"

        self.room_Details_Table.column("floor", width=100)
        self.room_Details_Table.column("roomno", width=100)
        self.room_Details_Table.column("roomType", width=100)

        self.room_Details_Table.pack(fill=BOTH, expand=1)
        self.room_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="register")
                cur = con.cursor()
                cur.execute("insert into details values(%s,%s,%s)", (
                                                                                self.var_floor.get(),
                                                                                self.var_roomNo.get(),
                                                                                self.var_RoomType.get()
                                                                                 ))
                con.commit()
                self.fetch_data()
                con.close()

                messagebox.showinfo("Success", "Details Added  Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="root", database="register")
        cur = con.cursor()
        cur.execute("select * from details")
        row = cur.fetchall()
        if len(row)!= 0:
            self.room_Details_Table.delete(*self.room_Details_Table.get_children())
            for i in row:
                self.room_Details_Table.insert("", END, values=i)
            con.commit()
        con.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_Details_Table.focus()
        content = self.room_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "please enter floor details", parent=self.root)
        else:
            con = pymysql.connect(host="localhost", user="root", password="root", database="register")
            cur = con.cursor()
            cur.execute(
                "update details set Floor=%s, RoomType=%s where RoomNo=%s",
                (
                    self.var_floor.get(),
                    self.var_RoomType.get(),
                    self.var_roomNo.get()
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
            query = "delete from details where RoomNo=%s"
            value = (self.var_roomNo.get(),)
            cur.execute(query, value)
        else:
            if not mdelete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()