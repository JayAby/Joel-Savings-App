from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3


class ShowRecord:
    def __init__(self, root):
        self.amount_received = None
        self.root = root
        self.root.title("View Records")
        self.root.geometry("1000x530+0+0")
        # self.root.resizable(0,0)
        self.create_widgets()

    def create_widgets(self):
        self.amount_received = DoubleVar()
        self.tithevalue = DoubleVar()
        self.accommodation = DoubleVar()
        self.fees = DoubleVar()
        self.transport = DoubleVar()
        self.bills = DoubleVar()
        self.save = DoubleVar()
        self.balance = DoubleVar()
        self.date = StringVar()

        # ===Set Window Icon====
        photo = PhotoImage(file="Images/aj.png")
        root.iconphoto(False, photo)

        # Creating Frames
        main_frame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="#dee8da")
        main_frame.grid()

        top_frame1 = Frame(main_frame, bd=5, width=1370, height=70, relief=RIDGE)
        top_frame1.grid(row=2, column=0, pady=8)
        title_frame = Frame(main_frame, bd=7, width=1370, height=120, relief=RIDGE)
        title_frame.grid(row=0, column=0)
        top_frame3 = Frame(main_frame, bd=5, width=1370, height=520, relief=RIDGE)
        top_frame3.grid(row=1, column=0)

        left_frame = Frame(top_frame3, bd=5, width=1340, height=400, padx=2, relief=RIDGE, bg="#dee8da")
        left_frame.pack(side=LEFT)
        left_frame1 = Frame(left_frame, bd=5, width=600, height=180, padx=2, pady=4, relief=RIDGE, bg="#dee8da")
        left_frame1.pack(side=TOP, padx=0, pady=4)

        # Title
        self.lbTitle = Label(title_frame, font=('arial', 56, 'bold'), text="View Records",
                             fg="white", bd=7)
        self.lbTitle.grid(row=0, column=0, padx=132)

        # Table
        scroll_x = Scrollbar(left_frame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(left_frame1, orient=VERTICAL)

        self.savingsList = ttk.Treeview(left_frame1, height=12, columns=(
            "no", "Salary", "Tithe", "Accommodation", "Fees", "Transport", "Bills", "Save", "AmountLeft", "Date"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_y.config(command=self.savingsList.yview)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.savingsList.xview)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.savingsList.heading("no", text="No")
        self.savingsList.heading("Salary", text="Salary")
        self.savingsList.heading("Tithe", text="Tithe")
        self.savingsList.heading("Accommodation", text="Accommodation")
        self.savingsList.heading("Fees", text="Fees")
        self.savingsList.heading("Transport", text="Transport")
        self.savingsList.heading("Bills", text="Bills")
        self.savingsList.heading("Save", text="Save")
        self.savingsList.heading("AmountLeft", text="AmountLeft")
        self.savingsList.heading("Date", text="Date")

        self.savingsList['show'] = 'headings'

        self.savingsList.column("no", width=25)
        self.savingsList.column("Salary", width=100)
        self.savingsList.column("Tithe", width=100)
        self.savingsList.column("Accommodation", width=110)
        self.savingsList.column("Fees", width=90)
        self.savingsList.column("Transport", width=110)
        self.savingsList.column("Bills", width=110)
        self.savingsList.column("Save", width=90)
        self.savingsList.column("AmountLeft", width=90)
        self.savingsList.column("Date", width=110)

        self.savingsList.pack()

        # Buttons
        Button(top_frame1, pady=1, bd=4, font=('arial', 20, 'bold'), text=" Back ", padx=24,
               command=self.back, fg="black", bg="#dee8da", width=6, height=2).grid(row=0, column=0,
                                                                                    padx=1)
        Button(top_frame1, pady=1, bd=4, font=('arial', 20, 'bold'), text=" View Table ", padx=24,
               command=self.showTable, fg="black", bg="#dee8da", width=12, height=2).grid(row=0, column=1,
                                                                                          padx=1)

    def back(self):
        tkinter.messagebox.showinfo("Info", "Works")

    def showTable(self):
        self.savingsList.delete(*self.savingsList.get_children())
        db = sqlite3.connect('AddNewRec.db')
        cur = db.cursor()
        cur.execute('SELECT * FROM addNew')
        fetch = cur.fetchall()
        for data in fetch:
            self.savingsList.insert('', 'end', values=(
            data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
        cur.close()


root = Tk()
application = ShowRecord(root)
root.mainloop()
