import tkinter as Toplevel
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql


class Registration(Toplevel.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1040x580+120+40")
        self.resizable(False, False)
        # self.state('zoomed')

        # =====Background  color ==========#
        self.configure(background='light sea green')

        # =====Title===========#
        self.title(" Registration")

        # ======Icon==========#
        self.iconbitmap('image/icon.ico')

        # Create a frame for the login form
        self.frame = Toplevel.Frame(self, width=990, height=530, bg='white')
        self.frame.place(x=27, y=27)

       #Function back button
        def back():
            import login
            self.destroy()
            login =login.LoginPage()


        # ======side Image==========#
        image = Image.open("image/Background.jpg")
        self.photo = ImageTk.PhotoImage(image)
        self.label = Toplevel.Label(self, image=self.photo, bd=0)
        self.label.place(x=48, y=27)

        # =========Create label for heading=======================
        head = Toplevel.Label(self, text="PLUS PHARMACY", font=('Microsoft Yahei Ul Light', 18, 'underline bold'),
                              bg='white',
                              fg='gray')
        head.place(x=640, y=60)

        # =========Create label for first name=======================
        first_name = Toplevel.Label(self, text="First Name", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                    fg='Gray')
        first_name.place(x=510, y=140)

        # Create entry for first name
        self.first_name_entry = Toplevel.Entry(self, bd=0)
        self.first_name_entry.place(x=510, y=170, height=20, width=185)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=510, y=190)

        # ============Create label for last name=========================
        last_name = Toplevel.Label(self, text="Last Name ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                   fg='Gray')
        last_name.place(x=510, y=205)

        # Create entry for last name
        self.last_name_entry = Toplevel.Entry(self, bd=0)
        self.last_name_entry.place(x=510, y=235, height=20, width=185)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=510, y=255)

        # ===================Create label for shop name===========================
        shop_name = Toplevel.Label(self, text="Shop Name ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                   fg='Gray')
        shop_name.place(x=510, y=270)
        # Create entry for shop name
        self.shop_name_entry = Toplevel.Entry(self, bd=0)
        self.shop_name_entry.place(x=510, y=300, height=20, width=185)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=510, y=320)

        # ============Create label for Contact Number=========================
        contact_number = Toplevel.Label(self, text="Contact No ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                        fg='Gray')
        contact_number.place(x=510, y=335)

        # Create entry for Contact Number
        self.contact_number_entry = Toplevel.Entry(self, bd=0)
        self.contact_number_entry.place(x=510, y=365, height=20, width=185)
        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=510, y=385)

        # ==== the entry field to only accept numbers and no other characters.=====
        self.contact_number_entry.config(validate="key",
                                         validatecommand=(self.register(lambda P: P.isdigit()), '%S'))

        # =======================Frame Boder=================================
        self.frame1 = Toplevel.Frame(self, width=2, height=240, bg='cyan4')
        self.frame1.place(x=750, y=145)

        # ===================Create label for Drug licence Number ===========================
        drug_licence = Toplevel.Label(self, text="Drug license ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                      fg='Gray')
        drug_licence.place(x=790, y=140)

        # Create entry for Drug licence Number
        self.drug_licence_entry = Toplevel.Entry(self, bd=0)
        self.drug_licence_entry.place(x=790, y=170, height=20, width=140)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=790, y=190)

        # ============Create label for Company code =========================
        company_code = Toplevel.Label(self, text="code       ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                      fg='Gray')
        company_code.place(x=790, y=205)

        # Create entry for Password
        self.company_code_entry = Toplevel.Entry(self, bd=0, show="*")
        self.company_code_entry.place(x=790, y=235, height=20, width=185)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=790, y=255)

        # ===================Create label for Email ===========================
        email = Toplevel.Label(self, text="E-Mail       ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                               fg='Gray')
        email.place(x=790, y=270)

        # Create entry for E-mail
        self.email_entry = Toplevel.Entry(self, bd=0)
        self.email_entry.place(x=790, y=300, height=20, width=185)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=790, y=320)

        # ============Create label for Password =========================
        password = Toplevel.Label(self, text="Password   ", font=('Microsoft Yahei Ul Light', 14), bg='white',
                                  fg='Gray')
        password.place(x=790, y=335)

        # Create entry for Password
        self.password_entry = Toplevel.Entry(self, bd=0, show="*")
        self.password_entry.place(x=790, y=365, height=20, width=185)

        # Frame
        self.frame1 = Toplevel.Frame(self, width=185, height=2, bg='cyan4')
        self.frame1.place(x=790, y=385)

        # Create a checkbox to show/hide password
        self.show_password_var = Toplevel.IntVar()
        self.show_password_checkbox = Toplevel.Checkbutton(self, variable=self.show_password_var, bg='white',
                                                           cursor='hand2', command=self.show_hide_password)
        self.show_password_checkbox.place(x=955, y=360)

        # ===========Create submit button===============
        self.submit_button = Toplevel.Button(self.frame, command=self.on_submit, text="Submit",
                                             font=('Microsoft Yahei Ul Light', 14),
                                             bg='cyan4', fg='white', bd=0, activebackground='white',
                                             activeforeground='gray',cursor='hand2')
        self.submit_button.place(x=620, y=400, width=210, height=30)

        # ===========Create Back button===============

        # SIGNUP BUTTON
        self.signuplabel = Toplevel.Label(self, text='All ready have an account?', font=('yu gothic ui', 9), fg='cyan4', bg='white')
        self.signuplabel.place(x=647, y=468)

        self.back_button = Toplevel.Button(self.frame, text="Sign in", font=('Microsoft Yahei Ul Light', 10),
                                           bg='white', fg='black', bd=0, activebackground='white',
                                           activeforeground='gray',cursor='hand2',command=back)
        self.back_button.place(x=760, y=440, width=80, height=20)

        # Function to show/hide

    def show_hide_password(self):
        if self.show_password_var.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def on_submit(self):
        # ===========Get values from entries======================
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        shop_name = self.shop_name_entry.get()
        contact_number = self.contact_number_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        drug_licence = self.drug_licence_entry.get()
        company_code = self.company_code_entry.get()

        # ====================== Perform validation checks=============
        if first_name and last_name and shop_name and contact_number and email and password and drug_licence and company_code:
            # Check if email is at least 4 characters long
            if len(email) >= 4:
                # Check if email starts with a letter
                if email[0].isalpha():
                    # Check if email contains exactly one '@' symbol
                    if ('@' in email) and (email.count("@") == 1):
                        if len(password) < 8:
                            messagebox.showerror("Error", "Password must be at least 8 characters long! ..")
                        else:
                              # Check if company code is equal to '1234'
                            if company_code != '1234':
                                messagebox.showerror("Error", "Invalid company code ! ..")
                            else:
                                try:
                                    # Connect to database using PyMySQL
                                    con = pymysql.connect(host="localhost", user="root", password="",
                                                          database="plus pharmacy database")
                                    cur = con.cursor()
                                    # Check if email is already registered
                                    cur.execute("select * from plus_pharmacy_user_data where email = %s",
                                                self.email_entry.get())
                                    row = cur.fetchone()
                                    if row != None:
                                        messagebox.showerror("Error",
                                                             " User already Exist , Please try with another email")
                                    else:
                                        # Insert user information into database
                                        cur.execute(
                                            "insert into plus_pharmacy_user_data (first_name,last_name,shop_name,contact_no,email,password,drug_licenese) values(%s,%s,%s,%s,%s,%s,%s)",
                                            (self.first_name_entry.get(),
                                             self.last_name_entry.get(),
                                             self.shop_name_entry.get(),
                                             self.contact_number_entry.get(),
                                             self.email_entry.get(),
                                             self.password_entry.get(),
                                             self.drug_licence_entry.get()
                                             ))
                                        con.commit()
                                        con.close()
                                        # Display success message
                                        messagebox.showinfo("Registration Successful", " Registeration successfully!")

                                except Exception as es:
                                    messagebox.showerror("Error", f"Error due to :{str(es)}")

                                # ==== After the register this code refresh the registration page
                                self.first_name_entry.delete(0, Toplevel.END)
                                self.last_name_entry.delete(0, Toplevel.END)
                                self.shop_name_entry.delete(0, Toplevel.END)
                                self.contact_number_entry.delete(0, Toplevel.END)
                                self.email_entry.delete(0, Toplevel.END)
                                self.password_entry.delete(0, Toplevel.END)
                                self.drug_licence_entry.delete(0, Toplevel.END)
                                self.company_code_entry.delete(0, Toplevel.END)

                    else:
                        messagebox.showerror("Email ", "Invalid Email")
                else:
                    messagebox.showerror("Email ", "Invalid Email")
            else:
                messagebox.showerror("Email ", "Invalid Email")
        else:
            messagebox.showerror("Error", "Please fill out all fields.")


if __name__ == "__main__":
    registration = Registration()
    registration.mainloop()
