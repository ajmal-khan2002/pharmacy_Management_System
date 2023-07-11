import tkinter as Toplevel
import tkinter as tk
from PIL import Image, ImageTk
import csv


class Homepage(Toplevel.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('1366x786')
        self.state('zoomed')

        # =====Background  color ==========#
        self.configure(background='white')

        # =====Title===========#
        self.title(" Plus Pharmacy")

        # ======Icon==========#
        self.iconbitmap('image/icon.ico')

        # Function logout button
        def logout():
            import login
            self.destroy()
            self.login = login.LoginPage()

        # Function add_medicine button
        def inven():
            import inventory
            self.destroy()
            self.inventory = inventory.MedicineInventoryApp()

        # # Function add_medicine button
        # def add():
        #     import add_medicine
        #     self.add_medicine = add_medicine.MedicineApp(self)

        def abc():
            import general_item
            self.destroy()
            root = tk.Tk()
            self.general_item = general_item.PharmacyApp(root)

        def note():
            import medicine_note
            root = tk.Tk()
            self.medicine_note = medicine_note.MedicineNote(root)

        def expiry():
            import expiry
            self.destroy()
            root = tk.Tk()
            self.expiry = expiry.Expiry(root)

        def invoice():
            import invoice
            self.destroy()
            self.invoice = invoice.Invoice()

        # ======header Image==========#
        image = Image.open("image/head.jpg")
        self.photo = ImageTk.PhotoImage(image)
        self.label = Toplevel.Label(self, image=self.photo, bd=0)
        self.label.place(x=250, y=-20)

        # ======== Body frame 1 ===============
        self.frame1 = Toplevel.Frame(self, width=250, height=90, bg='#A0E8FF')
        self.frame1.place(x=305, y=300)

        # ============Create label for Total medicine show in home page =========================

        # Open the CSV file and create a csv.reader object
        with open('medicine.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            # Count the remaining rows
            total_medicines = sum(1 for row in reader)

        today_sale = Toplevel.Label(self, text="Total Medicine", font=('Roboto Condensed', 10), bg='#A0E8FF',
                                    fg='#000000')
        today_sale.place(x=315, y=300)

        today = Toplevel.Label(self, text=f' {total_medicines}', font=('Roboto Condensed', 10), bg='#A0E8FF',
                               fg='#000000')
        today.place(x=315, y=330)

        # ======== Body frame 2 ===============
        self.frame2 = Toplevel.Frame(self, width=250, height=90, bg='#80BEFF')
        self.frame2.place(x=580, y=300)

        # ============Create label for Total medicine show in home page =========================

        # Open the CSV file and create a csv.reader object
        with open('general.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            # Count the remaining rows
            total_medicines = sum(1 for row in reader)
        # today inventory in number
        inventory_item = Toplevel.Label(self, text="General Product", font=('Roboto Condensed', 10), bg='#80BEFF',
                                        fg='#000000')
        inventory_item.place(x=590, y=305)
        # today  in inventory
        inventory = Toplevel.Label(self, text=f' {total_medicines}', font=('Roboto Condensed', 10), bg='#80BEFF',
                                   fg='#000000')
        inventory.place(x=590, y=330)

        # ======== Body frame 3 ===============
        self.frame3 = Toplevel.Frame(self, width=250, height=90, bg='#FFD6C4')
        self.frame3.place(x=855, y=300)

        # Open the CSV file and create a csv.reader object
        with open('deleted_medicines.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            # Count the remaining rows
            total_medicines = sum(1 for row in reader)
        # today Alert in number
        alert = Toplevel.Label(self, text="Alert", font=('Roboto Condensed', 10), bg='#FFD6C4',
                               fg='#000000')
        alert.place(x=865, y=305)
        # today  in inventory
        alert_text = Toplevel.Label(self, text=f' {total_medicines}', font=('Roboto Condensed', 10), bg='#FFD6C4',
                                    fg='#000000')
        alert_text.place(x=865, y=330)
        # user image
        user_image = Image.open("image/user.png")
        self.user_photo = ImageTk.PhotoImage(user_image)
        self.user_label = Toplevel.Label(self, image=self.user_photo, bd=0, bg="White")
        self.user_label.place(x=10, y=20)
        # ============= User name=============
        user_text = Toplevel.Label(self, text="USER", font=('Nanum Myeongjo', 16),
                                   bg='white',
                                   fg='black')
        user_text.place(x=40, y=155)

        # ============= Dashboard =============

        self.dashboard_button = Toplevel.Button(self, text="Home", font=('Merriweather', 14),
                                                bg='white', fg='#0C090A', bd=0, activebackground='white',
                                                 cursor='hand2')
        self.dashboard_button.place(x=30, y=210)

        # ============= Inventory.py items =============

        self.invertory_item_button = Toplevel.Button(self, text="Inventory", font=('Merriweather', 14),
                                                     bg='white', fg='#0C090A', bd=0, activebackground='white',
                                                     cursor='hand2', command=inven)
        self.invertory_item_button.place(x=30, y=250)

        # ============= General items =============

        self.general_item_button = Toplevel.Button(self, text="General Items", font=('Merriweather', 14),
                                                   bg='white', fg='#0C090A', bd=0, activebackground='white',
                                                   cursor='hand2', command=abc)
        self.general_item_button.place(x=30, y=290)


        # ============= Expired medicine =============

        self.expired_medicine_button = Toplevel.Button(self, text="Expired Medicine", font=('Merriweather', 14),
                                                       bg='white', fg='#0C090A', bd=0, activebackground='white',
                                                       cursor='hand2', command=expiry)
        self.expired_medicine_button.place(x=30, y=330)

        # ============= invoice  =============

        self.invoice_button = Toplevel.Button(self, text="Invoice", font=('Merriweather', 14),
                                              bg='white', fg='#0C090A', bd=0, activebackground='white', cursor='hand2',
                                              command=invoice)
        self.invoice_button.place(x=30, y=370)

        # ============= Medicine Note =============

        self.notee_button = Toplevel.Button(self, text="Note", font=('Merriweather', 14), bg='white', fg='#0C090A',
                                            bd=0, activebackground='white', cursor='hand2', command=note)
        self.notee_button.place(x=30, y=410)

        # ============= Logout =============

        self.logout_button = Toplevel.Button(self, text="Logout", font=('Merriweather', 14), bg='white', fg='#0C090A',
                                             bd=0, activebackground='white', cursor='hand2', command=logout)
        self.logout_button.place(x=30, y=450)

        # ============= Compamy name=============

        company_text = Toplevel.Label(self, text="Design By : Plus Pharma Industry ", font=('Monotype Corsiva', 15),
                                      bg='white',
                                      fg='#0C090A')
        company_text.place(x=950, y=600)

if __name__ == "__main__":
    home_page = Homepage()
    home_page.mainloop()
