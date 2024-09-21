from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Menu import FrontPage


def open_menu():
    root_menu = Tk()
    FrontPage(root_menu)
    root_menu.title("Joel Menu")
    root_menu.mainloop()


class LoginForm:
    def __init__(self, window):
        self.hide_button = None
        self.window = window
        self.window.geometry('1024x768')
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # ===BG IMG===
        self.bg_frame = Image.open('Images/monw.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=0)

        # ===Login Frame===
        self.login_frame = Frame(self.window, bg='#e9edf0', width='950', height=600)
        self.login_frame.place(x=240, y=68)

        self.txt = 'L E T \' S  S A V E'
        self.heading = Label(self.login_frame, text=self.txt, font=('yu gothic ui', 30, 'bold'), bg='#e9edf0',
                             fg='black')
        self.heading.place(x=100, y=50, width=300, height=30)

        # ===Left Side Image===
        self.side_image = Image.open('Images/Icon-512.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.login_frame, image=photo, bg='#e9edf0')
        self.side_image_label.image = photo
        self.side_image_label.place(x=1, y=120)

        # ===Sign In Text//Image===
        self.sign_in_image = Image.open('Images/Icon199.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.login_frame, image=photo, bg='#e9edf0')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=650, y=140)

        self.sign_in_label = Label(self.login_frame, text="S i g n  I n", font=('yu gothic ui', 20, 'bold'),
                                   bg='#e9edf0', fg='black')
        self.sign_in_label.place(x=720, y=100)

        # ===Username====
        self.username_label = Label(self.login_frame, text="Username:", font=('yu gothic ui', 15, 'bold'), bg='#e9edf0',
                                    fg='black')
        self.username_label.place(x=600, y=357)
        self.username_txt = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg='#e9edf0', fg='black',
                                  font=('yu gothic ui', 12, 'bold'))
        self.username_txt.place(x=690, y=359)
        # For creating a line
        self.username_line = Canvas(self.login_frame, width=190, height=2.0, bg='grey', highlightthickness=0)
        self.username_line.place(x=690, y=377)

        # ===Password===
        self.password_label = Label(self.login_frame, text="Password:", font=('yu gothic ui', 15, 'bold'), bg='#e9edf0',
                                    fg='black')
        self.password_label.place(x=600, y=450)
        self.password_txt = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg='#e9edf0', fg='black',
                                  font=('yu gothic ui', 12, 'bold'), show='*')
        self.password_txt.place(x=690, y=455)
        self.password_line = Canvas(self.login_frame, width=190, height=2.0, bg='grey', highlightthickness=0)
        self.password_line.place(x=690, y=473)

        # ===Login===
        self.login = Button(self.login_frame, text='LOGIN', font=('yu gothic ui', 15, 'bold'), fg='black', bg='#e9edf0',
                            cursor='hand2', command=self.login)
        self.login.place(x=730, y=530)

        # ===Show Password===
        self.show_button = Button(self.login_frame, text='sp', font=('yu gothic ui', 13, 'bold'), bg='black',
                                  cursor='hand2', activebackground='grey', command=self.show)
        self.show_button.place(x=880, y=450)

        # ===Set Window Icon====
        photo = PhotoImage(file="Images/aj.png")
        window.iconphoto(False, photo)

    def show(self):
        self.hide_button = Button(self.login_frame, text='hp', font=('yu gothic ui', 13, 'bold'), bg='black',
                                  cursor='hand2', activebackground='grey', command=self.hide)
        self.hide_button.place(x=880, y=450)
        self.password_txt.config(show='')

    def hide(self):
        self.show_button = Button(self.login_frame, text='sp', font=('yu gothic ui', 13, 'bold'), bg='black',
                                  cursor='hand2', activebackground='grey', command=self.show)
        self.show_button.place(x=880, y=450)
        self.password_txt.config(show='*')

    def login(self):
        strUser = self.username_txt.get()
        strPass = self.password_txt.get()

        if strUser == "" or strPass == "":
            messagebox.showerror("Error", "Incorrect Username or Password format")
        elif strUser == "Joel" and strPass == "Joel1234":
            messagebox.showinfo("Succesful", "Welcome Joel")
            window.destroy()
            open_menu()
        else:
            messagebox.showerror("Error", "Incorrect details entered")


if __name__ == "__main__":
    window = Tk()
    LoginForm(window)
    window.title("Joel-Login")
    window.mainloop()
