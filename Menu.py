from tkinter import *
from PIL import ImageTk, Image

class FrontPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x650")
        self.window.resizable(0, 0)

        # ===BG IMG===
        self.bg_frame = Image.open('/Users/joel/Desktop/Python/JoelSpendingsCalculator/App/Images/eyba.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=0)

        # ===Add Record====
        self.btn_add_record = Button(window, text="Add New Record", font=('yu gothic ui', 13, 'bold'), bg='black',
                                     cursor='hand2', activebackground='black', command=self.addNewButton)
        self.btn_add_record.place(x=230, y=200)

        # ===Show Record====
        self.btn_show_record = Button(window, text="Show Previous Record", font=('yu gothic ui', 13, 'bold'),
                                      bg='black', cursor='hand2', activebackground='black')
        self.btn_show_record.place(x=210, y=300)

        # ===Set Window Icon====
        photo = PhotoImage(file="Images/aj.png")
        window.iconphoto(False, photo)

    def addNewButton(self):
        window.destroy()
        from SavingCalc import AddNewRecord
        AddNewRecord(Tk())



if __name__ == "__main__":
    window = Tk()
    FrontPage(window)
    window.title("Joel-Menu")
    window.mainloop()
