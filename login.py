import tkinter as tk
from tkinter import messagebox

import pymysql
from PIL import Image, ImageTk


# Create a class for the login page that inherits from tk.Tk
class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set the window size and position
        self.geometry("845x585+200+30")
        self.resizable(False, False)

        # Set the background color of the window
        self.configure(background='light sea green')

        # Set the title of the window
        self.title(" Plus Pharmacy login")

        # Set the icon of the window
        self.iconbitmap('image/icon.ico')

        # Create a frame for the login form
        self.frame = tk.Frame(self, width=790, height=530, bg='white')
        self.frame.place(x=27, y=27)

        def registration():
            import registration
            self.destroy()
            registration = registration.Registration()

        # def registration():
        #     self.destroy()
        #     exec(open("registration.py").read())

        # Insert a background image
        image1 = Image.open("image/Background.jpg")
        self.photo1 = ImageTk.PhotoImage(image1)
        self.label = tk.Label(self.frame, image=self.photo1, bd=0)
        self.label.place(x=41, y=0)

        # Create a label for the username field
        self.username_label = tk.Label(self.frame, text="Username", font=('yu gothic ui', 16), bg='white', fg='gray')
        self.username_label.place(x=475, y=170)

        # Create an entry field for the username
        self.username_entry = tk.Entry(self.frame, bd=0, fg='black')
        self.username_entry.place(x=478, y=207, height=20, width=200)
        # Frame
        self.frame1 = tk.Frame(self.frame, width=200, height=2, bg='cyan4')
        self.frame1.place(x=478, y=225)

        # Create a label for the password field
        self.password_label = tk.Label(self.frame, text="Password", font=('yu gothic ui', 16), bg='white', fg='gray')
        self.password_label.place(x=475, y=235)

        # Create an entry field for the password
        self.password_entry = tk.Entry(self.frame, bd=0, fg='black', show="*")
        self.password_entry.place(x=478, y=272, height=20, width=140)

        # Frame
        self.frame1 = tk.Frame(self.frame, width=200, height=2, bg='cyan4')
        self.frame1.place(x=478, y=290)

        # Create a checkbox to show/hide password
        self.show_password_var = tk.IntVar()
        self.show_password_checkbox = tk.Checkbutton(self.frame, variable=self.show_password_var,
                                                     command=self.show_hide_password, bg="white", cursor='hand2',
                                                     fg='cyan4')
        self.show_password_checkbox.place(x=653, y=265)

        # Create a button for forgotten password
        self.forgot_password_button = tk.Button(self.frame, text="Forgot Password", command=self.forgot_password,
                                                bg="white", bd=0, activebackground='white', cursor='hand2', fg='gray')
        self.forgot_password_button.place(x=585, y=300)

        # Create a login button
        login_button = tk.Button(self.frame, text="Login", width=24, bd=0, activebackground='white',
                                 bg='cyan4', fg='white', activeforeground='gray', font=('yu gothic ui', 11),
                                 cursor='hand2', command=self.open_main_page)
        login_button.place(x=480, y=330)

        # SIGNUP BUTTON
        self.signuplabel = tk.Label(self.frame, text='Dont have an account?', font=('yu gothic ui', 9), fg='gray',
                                    bg='white')
        self.signuplabel.place(x=480, y=370)

        self.newaccountButton = tk.Button(self.frame, text='CREATE NEW', font=('yu gothic ui', 8, 'bold'),
                                          fg='black', bg='white', activebackground='white', activeforeground='gray',
                                          cursor='hand2', bd=0, command=registration)
        self.newaccountButton.place(x=610, y=372)
        # Function to show/hide

    def show_hide_password(self):
        if self.show_password_var.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

        # ===========Get values from entries======================

    def open_main_page(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Perform validation checks on the entered username and password
        if username and password:
            if len(username) >= 4:  # check if the username is at least 4 characters long
                if username[0].isalpha():  # check if the first character of the username is a letter
                    # check if the username is of the format xxx@xxx.com
                    if ('@' in username) and (username.count("@") == 1):

                        try:
                            # Connect to database using PyMySQL
                            con = pymysql.connect(host="localhost", user="root", password="",
                                                  database="plus pharmacy database")
                            cur = con.cursor()
                            cur.execute("select * from plus_pharmacy_user_data where email=%s and password=%s",
                                        (self.username_entry.get(), self.password_entry.get()))
                            row = cur.fetchone()
                            if row is None:
                                messagebox.showerror("Error", "Invalid username and password.")
                            else:

                                    import home_page
                                    self.destroy()
                                    home_page = home_page.Homepage()
                                    home_page.mainloop()

                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to :{str(es)}")

                    else:

                        messagebox.showerror("Login", "Invalid username and password.")
                else:
                    messagebox.showerror("Login", "Invalid username and password.")
            else:
                messagebox.showerror("Login", "Invalid username and password.")
        else:
            messagebox.showerror("Login", "please fill out all fields.")

        # Function to handle forgotten password

    def forgot_password(self):
        # Open a new window to handle the forgot password request
        forgot_password_window = tk.Toplevel(self)
        forgot_password_window.title("Forgot Password")

        self.iconbitmap('image/icon.ico')

        email_label = tk.Label(forgot_password_window, text="Email:")
        email_label.grid(row=0, column=0, padx=5, pady=5)

        email_entry = tk.Entry(forgot_password_window)
        email_entry.grid(row=0, column=0, padx=5, pady=5)

        submit_button = tk.Button(forgot_password_window, text="Submit",
                                  command=lambda: self.submit_email(email_entry.get()))
        submit_button.grid(row=1, column=1, padx=5, pady=5)

    def submit_email(self, email):
        # Handles the submission of the email address for the forgot password request
        if email:
            # Check if email is at least 4 characters long
            if len(email) >= 4:
                # Check if email starts with a letter
                if email[0].isalpha():
                    # Check if email contains exactly one '@' symbol
                    if ('@' in email) and (email.count("@") == 1):
                        pass
                    else:
                        messagebox.showerror("Email ", "Invalid Email")
                else:
                    messagebox.showerror("Email ", "Invalid Email")
            else:
                messagebox.showerror("Email ", "Invalid Email")
        else:
            messagebox.showerror("Error", "Please fill out all fields.")


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()
