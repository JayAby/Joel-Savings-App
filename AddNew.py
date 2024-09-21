import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import date



class AddNewRecord:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1024x768')
        self.window.resizable(0, 0)

        # Variables
        self.current_amount = DoubleVar()
        self.amount_received = DoubleVar()
        self.tithevalue = DoubleVar()
        self.accommodation = DoubleVar()
        self.fees = DoubleVar()
        self.transport = DoubleVar()
        self.sim = DoubleVar()
        self.save = DoubleVar()
        self.balance = DoubleVar()
        self.date = StringVar()

        # ===BG IMG===
        self.bg_frame = Image.open('Images/mone.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=0)

        # ===Frame===
        self.add_new_frame = Frame(self.window, bg='#dee8da', width='986', height=230)
        self.add_new_frame.pack(fill="x", expand=0, padx=20)
        self.add_new_frame.place(x=15, y=50)

        # ===Labels===
        self.txt_salary_calc = Label(self.add_new_frame, text="Salary Calculator", font=('Helvetica', 35, 'bold'),
                                     bg='#dee8da', fg='black')
        self.txt_salary_calc.place(x=380, y=12)
        self.txt_salary_calc_line = Canvas(self.add_new_frame, width=980, height=2.0, bg='grey', highlightthickness=0)
        self.txt_salary_calc_line.place(x=2, y=56)
        # ===Amount Received===
        self.amount_received_label = Label(self.add_new_frame, text="Amount Received(£):", font=('Arial', 20, 'bold'),
                                           bg='#dee8da', fg='black')
        self.amount_received_label.place(x=50, y=92)
        self.amount_received_txt = Entry(self.add_new_frame, highlightthickness=0, textvariable=self.amount_received,
                                         relief=FLAT, bg='white', fg='black',
                                         font=('yu gothic ui', 12, 'bold'))
        self.amount_received_txt.place(x=256, y=97)
        self.current_amount_label = Label(self.add_new_frame, text="Current Amount(£):", font=('Arial', 20, 'bold'),
                                           bg='#dee8da', fg='black')
        self.current_amount_label.place(x=490, y=92)
        self.current_amount_txt = Entry(self.add_new_frame, highlightthickness=0, textvariable=self.current_amount,
                                         relief=FLAT, bg='white', fg='black',
                                         font=('yu gothic ui', 12, 'bold'))
        self.current_amount_txt.place(x=681, y=97)
        # ===Calculate Button===
        self.btn_amount_calc = Button(self.add_new_frame, text='CALCULATE', font=('Arial', 15, 'bold'), fg='black',
                                      bg='#dee8da', cursor='hand2', command=self.calculateButton)
        self.btn_amount_calc.place(x=400, y=146)

        # ===Lower Frame===
        self.down_frame = Frame(self.window, bg='#dee8da', width='986', height=430)
        self.down_frame.pack(fill="x", expand=0, padx=20)
        self.down_frame.place(x=15, y=320)

        # ===Labels and Textbox
        self.tithe_label = Label(self.down_frame, text='Tithe:', font=('Arial', 18, 'bold'), fg='black', bg='#dee8da')
        self.tithe_label.place(x=120, y=45)
        self.tithe_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.tithevalue,
                               relief=FLAT, bg='white', fg='black',
                               font=('yu gothic ui', 12, 'bold'))
        self.tithe_txt.place(x=178, y=49)
        self.accommodation_label = Label(self.down_frame, text='Accommodation:', font=('Arial', 18, 'bold'), fg='black',
                                         bg='#dee8da')
        self.accommodation_label.place(x=520, y=45)
        self.accommodation_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.accommodation,
                                       relief=FLAT, bg='white', fg='black',
                                       font=('yu gothic ui', 12, 'bold'))
        self.accommodation_txt.place(x=680, y=49)
        self.fees_label = Label(self.down_frame, text='Fees:', font=('Arial', 18, 'bold'), fg='black', bg='#dee8da')
        self.fees_label.place(x=120, y=105)
        self.fees_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.fees,
                              relief=FLAT, bg='white', fg='black',
                              font=('yu gothic ui', 12, 'bold'))
        self.fees_txt.place(x=178, y=109)
        self.transport_label = Label(self.down_frame, text='Transport:', font=('Arial', 18, 'bold'), fg='black',
                                     bg='#dee8da')
        self.transport_label.place(x=520, y=105)
        self.transport_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.transport,
                                   relief=FLAT, bg='white', fg='black',
                                   font=('yu gothic ui', 12, 'bold'))
        self.transport_txt.place(x=618, y=109)
        self.sim_label = Label(self.down_frame, text='Sim:', font=('Arial', 18, 'bold'), fg='black', bg='#dee8da')
        self.sim_label.place(x=120, y=165)
        self.sim_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.sim,
                             relief=FLAT, bg='white', fg='black',
                             font=('yu gothic ui', 12, 'bold'))
        self.sim_txt.place(x=178, y=169)
        self.save_label = Label(self.down_frame, text='Save:', font=('Arial', 18, 'bold'), fg='black', bg='#dee8da')
        self.save_label.place(x=120, y=225)
        self.save_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.save,
                              relief=FLAT, bg='white', fg='black',
                              font=('yu gothic ui', 12, 'bold'))
        self.save_txt.place(x=178, y=229)
        self.amount_left_label = Label(self.down_frame, text='Amount Left:', font=('Arial', 18, 'bold'), fg='black',
                                       bg='#dee8da')
        self.amount_left_label.place(x=520, y=165)
        self.amount_left_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.balance,
                                     relief=FLAT, bg='white', fg='black',
                                     font=('yu gothic ui', 12, 'bold'))
        self.amount_left_txt.place(x=638, y=169)
        self.date_label = Label(self.down_frame, text='Date:', font=('Arial', 18, 'bold'), fg='black',
                                bg='#dee8da')
        self.date_label.place(x=520, y=225)
        self.date_txt = Entry(self.down_frame, highlightthickness=0, textvariable=self.date,
                              relief=FLAT, bg='white', fg='black',
                              font=('yu gothic ui', 12, 'bold'))
        self.date_txt.place(x=578, y=229)

        # ===Buttons===
        self.btn_back = Button(self.down_frame, text='BACK', font=('Arial', 15, 'bold'), fg='black',
                               bg='#dee8da', cursor='hand2')
        self.btn_back.place(x=350, y=296)
        self.btn_save = Button(self.down_frame, text='SAVE', font=('Arial', 15, 'bold'), fg='black',
                               bg='#dee8da', cursor='hand2', command=self.saveButton)
        self.btn_save.place(x=440, y=296)

    def calculations(self):

        self.textBoxEdit()

        # Tithe Calculations
        salaryvalue = self.amount_received_txt.get()
        tithevalue = self.tithe_txt.get()

        storage_tithe_value = 10 / 100 * float(salaryvalue)
        tithevalue = round(storage_tithe_value, 2)
        currentvalue = float(salaryvalue) - float(tithevalue)
        self.tithe_txt.delete(0, END)
        self.tithe_txt.insert(END, tithevalue)
        self.current_amount_txt.delete(0,END)
        self.current_amount_txt.insert(END,currentvalue)


        # Accommodation Calculation
        tempaccommodationvalue = self.accommodation_txt.get()
        accommodationvalue = 0.5 * currentvalue
        currentvalue = currentvalue - accommodationvalue
        self.accommodation_txt.delete(0,END)
        self.accommodation_txt.insert(END, round(accommodationvalue, 2))
        self.current_amount_txt.delete(0,END)
        self.current_amount_txt.insert(END,round(currentvalue, 2))

        #Fees calculation
        # I plan to make Fees done in such a way that it's done manually
        feesvalue = self.fees_txt.get()
        try:
            feesvalue = float(feesvalue)  # Convertfeesvaluetofloat
        except ValueError:
            messagebox.showerror("Error", "Invalid input for fees.Please enter a valid number.")
            return

        currentvalue = float(currentvalue) - feesvalue

        if feesvalue <= currentvalue:
            self.current_amount_txt.delete(0, END)
            self.current_amount_txt.insert(END, round(currentvalue, 2))
        else:
            messagebox.showerror("Error", "Fees value cannot be more than the current amount")
            self.fees_txt.delete(0, END)
            self.fees_txt.insert(END, float(0.0))

        # TransportCalculation
        transvalue = self.transport_txt.get()
        try:
            transvalue = float(transvalue)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Transport.Please enter a valid number.")
            return  # Stop further execution if conversion fails

        currentvalue = float(currentvalue) - transvalue

        if feesvalue <= currentvalue:
            self.current_amount_txt.delete(0, END)
            self.current_amount_txt.insert(END, round(currentvalue, 2))
        else:
            messagebox.showerror("Error", "Transport value cannot be more than the current amount")
            self.transport_txt.delete(0, END)
            self.transport_txt.insert(END, float(0.0))

        # SimCalculation
        simvalue = self.sim_txt.get()
        try:
            simvalue = float(simvalue)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for Sim.Please enter a valid number.")
            return  # Stop further execution if conversion fails

        currentvalue = float(currentvalue) - simvalue

        if simvalue <= currentvalue:
            self.current_amount_txt.delete(0, END)
            self.current_amount_txt.insert(END, round(currentvalue, 2))
        else:
            messagebox.showerror("Error", "Sim value cannot be more than the current amount")
            self.sim_txt.delete(0, END)
            self.sim_txt.insert(END, float(0.0))

        #Savings Calculation
        tempsavevalue = self.save_txt.get()
        savevalue = 0.4 * currentvalue
        currentvalue = currentvalue - savevalue
        self.save_txt.delete(0,END)
        self.save_txt.insert(END, round(savevalue, 2))
        self.current_amount_txt.delete(0,END)
        self.current_amount_txt.insert(END,round(currentvalue, 2))

        #Input date
        current_date = date.today()
        self.date_txt.delete(0, END)
        self.date_txt.insert(END, current_date)

        #Amount Left
        currentvalue = float(self.current_amount_txt.get())
        self.amount_left_txt.delete(0, END)
        self.amount_left_txt.insert(END, round(currentvalue, 2))



    def textBoxNoEdit(self):
        self.amount_left_txt.config(state='disabled')
        self.tithe_txt.config(state='disabled')
        # self.amount_received_txt.config(state='disabled')
        self.current_amount_txt.config(state='disabled')
        self.accommodation_txt.config(state='disabled')
        self.save_txt.config(state='disabled')
        self.date_txt.config(state='disabled')

    def textBoxEdit(self):
        self.amount_left_txt.config(state='normal')
        self.tithe_txt.config(state='normal')
        # self.amount_received_txt.config(state='normal')
        self.current_amount_txt.config(state='normal')
        self.accommodation_txt.config(state='normal')
        self.save_txt.config(state='normal')
        self.date_txt.config(state='normal')

    def clear(self):
        self.amount_received_txt.delete(0, END)
        self.current_amount_txt.delete(0, END)
        self.tithe_txt.delete(0, END)
        self.accommodation_txt.delete(0, END)
        self.fees.delete(0, END)
        self.transport_txt.delete(0, END)
        self.sim_txt.delete(0, END)
        self.save_txt.delete(0, END)
        self.date_txt.delete(0, END)

    def saveButton(self):
        amount_received_data = self.amount_received.get()
        tithe_data = self.tithevalue.get()
        accommodation_data = self.accommodation.get()
        fees_data = self.fees.get()
        transport_data = self.transport.get()
        sim_data = self.sim.get()
        save_data = self.save.get()
        balance_data = self.balance.get()
        date = self.date.get()

        if amount_received_data == 0.0:
            messagebox.showerror("Error","Field can't be left empty")
        else:
            #connect to database
            db = sqlite3.connect('AddNewRec.db')

            insert_savings_query = "insert into addNew(amountreceived,tithe,accommodation,fees,transport,sim,save,balance,date) values (?,?,?,?,?,?,?,?,?);"

            try:
                cursor = db.cursor()

                cursor.execute(insert_savings_query,(amount_received_data,tithe_data,accommodation_data,fees_data,transport_data,sim_data,save_data,balance_data,date))

                db.commit()
                messagebox.showinfo("Confirmation","Saved")
                self.clear()

            except Exception as e:
                print("Error:", e)
                messagebox.showerror("Error", "Data can't be saved - Insert SQL Error")
                db.rollback()
            db.close()









    def calculateButton(self):
        self.calculations()
        self.textBoxNoEdit()





if __name__ == "__main__":
    window = Tk()
    AddNewRecord(window)
    window.title("Joel-AddNewRecord")
    window.mainloop()
