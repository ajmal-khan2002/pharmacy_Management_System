import tkinter as tk
from tkinter import ttk
import csv
import random
from tkinter import messagebox
import os
import tempfile


class Invoice(tk.Tk):

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
        # ====== variable user data store ========

        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()
        self.customer_email = tk.StringVar()
        search_bill = tk.StringVar()
        self.product = tk.StringVar()
        self.price = tk.IntVar()
        self.quantity = tk.IntVar()
        self.sub_total = tk.StringVar()
        self.gst_tax = tk.StringVar()
        self.total_amount = tk.StringVar()

        # ======Frame===========#
        self.frame = tk.Frame(self, width=350, height=528, bg='white')
        self.frame.place(x=0, y=0)

        # ======Frame1===========#
        self.frame1 = tk.Frame(self, width=1280, height=45, bg='cyan4')
        self.frame1.place(x=0, y=0)

        # =====Frame1 text =====================
        self.text = tk.Label(self.frame1, text="Invoice Bill", font=('Oswald', 20), bg='cyan4',
                             fg='white')
        self.text.place(x=600, y=5)

        # ====== Customer details label Frame===========#

        self.customer_dtls = tk.LabelFrame(self, text="Customer details", font=('Roboto Condensed', 14), bg='white',
                                           fg='black')
        self.customer_dtls.place(x=18, y=86, width=350, height=140)

        # ========== Customer name ==============
        self.name = tk.Label(self.customer_dtls, text=" Customer Name", font=('Roboto Condensed', 12),
                             bg='white',
                             fg='black')
        self.name.place(x=0, y=0)

        # ====Create entry for customer name======
        self.name_entry = tk.Entry(self.customer_dtls, textvariable=self.customer_name, font=('Roboto Condensed', 12),
                                   width=15)
        self.name_entry.place(x=150, y=0)

        # ============Create label for  customer Contact Number=========================
        contact_number = tk.Label(self.customer_dtls, text="Mobile Number", font=('Roboto Condensed', 12), bg='white',
                                  fg='black')
        contact_number.place(x=5, y=35)

        # Create entry for customer Contact Number
        self.contact_number_entry = tk.Entry(self.customer_dtls, textvariable=self.customer_phone,
                                             font=('Roboto Condensed', 12), width=15)
        self.contact_number_entry.place(x=150, y=35)

        # ==== the entry field to only accept numbers and no other characters.=====
        self.contact_number_entry.config(validate="key",
                                         validatecommand=(self.register(lambda P: P.isdigit()), '%S'))

        # ===================Create label for Email ===========================
        email = tk.Label(self.customer_dtls, text="E-Mail", font=('Roboto Condensed', 12), bg='white',
                         fg='black')
        email.place(x=5, y=70)

        # Create entry for E-mail
        self.email_entry = tk.Entry(self.customer_dtls, textvariable=self.customer_email, font=('Roboto Condensed', 12),
                                    width=15)
        self.email_entry.place(x=150, y=70)

        # ====== Product details label Frame===========#

        self.product_dtls = tk.LabelFrame(self, text="Product ", font=('Roboto Condensed', 14),
                                          bg='white',
                                          fg='black')
        self.product_dtls.place(x=18, y=260, width=350, height=200)

        # =================== Variable user data store===============

        # Read the product details from a CSV file
        with open('medicine.csv', 'r') as f:
            reader = csv.reader(f)
            self.products = list(reader)

        # Read the product details from a CSV file
        with open('general.csv', 'r') as f:
            reader = csv.reader(f)
            self.med_products = list(reader)

        # Create a StringVar to store the selected product and category
        self.selected_product = tk.StringVar()
        self.selected_category = tk.StringVar()
        # ========== select category ==============
        self.select_category = tk.Label(self.product_dtls, text="Select Category", font=('Roboto Condensed', 12),
                                        bg='white',
                                        fg='black')
        self.select_category.place(x=5, y=0)

        # # ============select category ========
        selection_var = tk.StringVar()
        selection_var.set('medicine')
        style = ttk.Style()
        style.configure('TRadiobutton', background='white')  # set the background color to white
        medicine_radio = ttk.Radiobutton(self.product_dtls, text="Medicine", variable=self.selected_category,
                                         value="Medicine",
                                         style='TRadiobutton', command=self.update_product_list)
        inventory_radio = ttk.Radiobutton(self.product_dtls, text="General", variable=self.selected_category,
                                          value="Product", style='TRadiobutton', command=self.update_product_list)
        medicine_radio.place(x=150, y=5)
        inventory_radio.place(x=250, y=5)

        # ========== Search medicine ==============

        search_label = tk.Label(self.product_dtls, text="Search", font=('Roboto Condensed', 12), bg='white')
        search_label.place(x=5, y=40)

        self.search_entry = tk.Entry(self.product_dtls)
        self.search_entry.place(x=140, y=40, width=160)

        search_button = tk.Button(self.product_dtls, text="OK", command=self.search_product)
        search_button.place(x=300, y=40, width=40)

        # ========== Product name ==============
        self.product_name = tk.Label(self.product_dtls, text=" Product Name", font=('Roboto Condensed', 12),
                                     bg='white',
                                     fg='black')
        self.product_name.place(x=0, y=70)

        self.product_combo = ttk.Combobox(self.product_dtls, textvariable=self.selected_product)
        self.product_combo.place(x=140, y=75)
        self.product_combo.bind('<<ComboboxSelected>>', self.update_price)
        self.product_entry = tk.Entry(self.product_dtls, textvariable=self.selected_product)
        self.product_name.place(x=0, y=75)

        # ==========  product Price ==============
        self.product_price = tk.Label(self.product_dtls, text=" Price", font=('Roboto Condensed', 12),
                                      bg='white',
                                      fg='black')
        self.product_price.place(x=0, y=115)

        # ====Create entry for product price======
        self.product_price_entry = tk.Entry(self.product_dtls, textvariable=self.price, font=('Roboto Condensed', 12),
                                            width=8)
        self.product_price_entry.place(x=140, y=115)

        # ==========Create quantity label and spinbox
        self.quantity_label = tk.Label(self.product_dtls, text="Quantity", bg="white", font=('Roboto Condensed', 12))
        self.quantity_label.place(x=0, y=150)
        self.quantity_spinbox = ttk.Spinbox(self.product_dtls, textvariable=self.quantity, from_=1, to=100, width=10)
        self.quantity_spinbox.place(x=140, y=150)
        self.quantity_spinbox.delete(0, "end")
        self.quantity_spinbox.insert(0, "1")

        # ============= Bill Area Frame ===================
        self.RightLabelFrame = tk.LabelFrame(self, bg="White")
        self.RightLabelFrame.place(x=480, y=95, width=790, height=450)

        # ======== scroll bar =====================

        self.scroll_y = tk.Scrollbar(self.RightLabelFrame, orient=tk.VERTICAL)
        self.textarea = tk.Text(self.RightLabelFrame, yscrollcommand=self.scroll_y.set, bg="white", fg="Black",
                                font=('Roboto Condensed', 12))
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=tk.BOTH, expand=1)

        # ====== Amount label Frame===========#

        self.amount_frame = tk.LabelFrame(self, text="Amount ", font=('Roboto Condensed', 14),
                                          bg='white',
                                          fg='black')
        self.amount_frame.place(x=18, y=480, width=350, height=160)

        # ========== amount ==============
        self.amount = tk.Label(self.amount_frame, text="Amount", font=('Roboto Condensed', 12),
                               bg='white',
                               fg='black')
        self.amount.place(x=5, y=5)

        # ====Create entry for amount ======
        self.amount_entry = tk.Entry(self.amount_frame, textvariable=self.sub_total, font=('Roboto Condensed', 12),
                                     width=21)
        self.amount_entry.place(x=140, y=5)

        # ========== GST Tax ==============
        self.tax = tk.Label(self.amount_frame, text="GST %", font=('Roboto Condensed', 12),
                            bg='white',
                            fg='black')
        self.tax.place(x=5, y=45)

        # ====Create entry for GST Tax ======
        self.tax_entry = tk.Entry(self.amount_frame, textvariable=self.gst_tax, font=('Roboto Condensed', 12), width=21)
        self.tax_entry.place(x=140, y=45)

        # ========== Total Amount ==============
        self.total = tk.Label(self.amount_frame, text="Total Amount", font=('Roboto Condensed', 12),
                              bg='white',
                              fg='black')
        self.total.place(x=5, y=90)

        # ====Create entry for Total Amount ======
        self.total_entry = tk.Entry(self.amount_frame, textvariable=self.total_amount, font=('Roboto Condensed', 12),
                                    width=21)
        self.total_entry.place(x=140, y=90)

        # ====== button label Frame===========#

        self.button_frame = tk.LabelFrame(self, bg="White")
        self.button_frame.place(x=480, y=550, width=790, height=80)

        # ====== button  add to cart===========#

        self.btnAddToCart = tk.Button(self.button_frame, text="Add to Cart", font=('Roboto Condensed', 12),
                                      bg="#46B8FF", fg="white", activebackground='#46B8FF', cursor="hand2",
                                      command=self.AddItem)
        self.btnAddToCart.place(x=0, y=0, width=130, height=75)

        # ====== button  Generate bill===========#

        self.btngenerate_bill = tk.Button(self.button_frame, text="Generate Bill", font=('Roboto Condensed', 12),
                                          bg="#46B8FF", fg="white", activebackground='#46B8FF',
                                          cursor="hand2", command=self.generate_bill)
        self.btngenerate_bill.place(x=130, y=0, width=130, height=75)

        # ====== button  Save bill===========#

        self.btnsave_bill = tk.Button(self.button_frame, text="Save Bill", font=('Roboto Condensed', 12),
                                      bg="#46B8FF", fg="white", activebackground='#46B8FF',
                                      cursor="hand2", command=self.save_bill)
        self.btnsave_bill.place(x=260, y=0, width=130, height=75)

        # ====== button  print bill===========#

        self.btnprint_bill = tk.Button(self.button_frame, text="Print Bill", font=('Roboto Condensed', 12),
                                       bg="#46B8FF", fg="white", activebackground='#46B8FF',
                                       cursor="hand2", command=self.print_bill)
        self.btnprint_bill.place(x=390, y=0, width=137, height=75)

        # ====== button  clear bill===========#

        self.btnclear_bill = tk.Button(self.button_frame, text="clear", font=('Roboto Condensed', 12),
                                       bg="#46B8FF", fg="white", activebackground='#46B8FF',
                                       cursor="hand2", command=self.clear)
        self.btnclear_bill.place(x=528, y=0, width=136, height=75)

        # ====== button Exit===========#

        self.btnexit_invoice = tk.Button(self.button_frame, text="Exit", font=('Roboto Condensed', 12),
                                         bg="#46B8FF", fg="white", activebackground='#46B8FF',
                                         cursor="hand2", command=self.exit)
        self.btnexit_invoice.place(x=665, y=0, width=120, height=75)
        self.welcome()
        self.l = []

    def search_product(self):
        query = self.search_entry.get()
        matches = []

        if self.selected_category.get() == "Medicine":
            for product in self.products:
                if query.lower() in product[0].lower():
                    matches.append(product[0])  # Append only the product name
        else:
            for product in self.med_products:
                if query.lower() in product[0].lower():
                    matches.append(product[0])  # Append only the product name

        if matches:
            self.product_combo['values'] = matches
            self.product_combo.current(0)
        else:
            messagebox.showinfo("No Results", "No matching products found.")

    # ========== Bill function ==========================
    def generate_invoice_id(self):
        return "INV" + str(random.randint(10000, 99999))

    def AddItem(self):
        product_name = self.product_combo.get()
        quantity = self.quantity.get()
        price = self.price.get()

        if product_name == "":
            messagebox.showerror("Error", "Please select the Product Name")
        elif quantity <= 0:
            messagebox.showerror("Error", "Invalid quantity")
        elif not self.check_available_quantity(product_name, quantity):
            messagebox.showerror("Error", "Insufficient quantity available")
        else:
            total = quantity * price
            self.l.append(total)
            self.textarea.insert(tk.END, f"\n{product_name}\t\t\t\t{quantity}\t\t\t\t{total}")
            self.sub_total.set(f"Rs.{sum(self.l):.2f}")
            self.gst_tax.set(f"Rs.{((sum(self.l) - price) * 1) / 100:.2f}")
            self.total_amount.set(f"Rs.{sum(self.l) + (((sum(self.l) - price) * 1) / 100):.2f}")

    def check_available_quantity(self, product_name, quantity):
        if self.selected_category.get() == "Medicine":
            products_list = self.products
        else:
            products_list = self.med_products

        for product in products_list:
            if product_name == product[0]:
                available_quantity = int(product[1])
                return quantity <= available_quantity
        return False

    def generate_bill(self):
        if self.product_combo.get() == "":
            messagebox.showerror("Error", "please Add to Cart Product")
        else:
            text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(tk.END, text)
            self.textarea.insert(tk.END,
                                 "\n-------------------------------------------------------------------------------------------------------------------------------------------------------")
            self.textarea.insert(tk.END, f"\n Sub Amount :\t\t\t{self.sub_total.get()}")
            self.textarea.insert(tk.END, f"\n GST Amount :\t\t\t{self.gst_tax.get()}")
            self.textarea.insert(tk.END, f"\n Total Amount :\t\t\t{self.total_amount.get()}")
            self.textarea.insert(tk.END,
                                 "\n-------------------------------------------------------------------------------------------------------------------------------------------------------")
            # Reduce quantity in medicine.csv

            with open('medicine.csv', 'r') as f:
                reader = csv.reader(f)
                products = list(reader)
            for i in range(len(products)):
                if products[i][0] == self.product_combo.get():
                    products[i][1] = str(int(products[i][1]) - self.quantity.get())
                    break
            with open('medicine.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(products)

            # Reduce quantity in general.csv
            with open('general.csv', 'r') as f:
                reader = csv.reader(f)
                med_products = list(reader)
            for i in range(len(med_products)):
                if med_products[i][0] == self.product_combo.get():
                    med_products[i][1] = str(int(med_products[i][1]) - self.quantity.get())
                    break
            with open('general.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(med_products)

    def save_bill(self):
        if self.product_combo.get() == "":
            messagebox.showerror("Error", "please Add to Cart Product")
        else:
            if self.customer_name.get() == "":
                messagebox.showerror("Error", "please Enter Customer Name")
            else:
                op = messagebox.askyesno("save Invoice", "Do You want to save Invoice")
                if op > 0:
                    self.bill_data = self.textarea.get(1.0, tk.END)
                    f1 = open('bills/' + str(self.customer_name.get()) + ".txt", "w")
                    f1.write(self.bill_data)
                    messagebox.showinfo("Saved", f"File Name is  :{self.customer_name.get()} Saved Successfully")
                    f1.close()

    def print_bill(self):
        if self.product_combo.get() == "":
            messagebox.showerror("Error", "please Add to Cart Product")
        else:
            q = self.textarea.get(1.0, "end-1c")
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(q)
            os.startfile(filename, "print")

    def clear(self):
        self.textarea.delete(1.0, tk.END)
        self.customer_name.set("")
        self.customer_phone.set("")
        self.customer_email.set("")
        self.generate_invoice_id()
        self.sub_total.set("")
        self.gst_tax.set("")
        self.total_amount.set("")
        self.welcome()

    def welcome(self):
        self.textarea.delete(1.0, tk.END)
        self.textarea.insert(tk.END, "\t\t\t\t  Welcome to Plus pharmacy ")
        self.textarea.insert(tk.END, f"\n Invoice Number: {self.generate_invoice_id()}")
        self.textarea.insert(tk.END, f"\n Customer Name : {self.customer_name.get()}")
        self.textarea.insert(tk.END, f"\n Customer Phone No : {self.customer_phone.get()}")
        self.textarea.insert(tk.END, f"\n Customer Email ID : {self.customer_email.get()}")
        self.textarea.insert(tk.END,
                             "\n-------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.textarea.insert(tk.END, f"\nProduct\t\t\t\t QTY\t\t\t\tPrice")
        self.textarea.insert(tk.END,
                             "\n-------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    def exit(self):
        import home_page
        self.destroy()
        self.home_page = home_page.Homepage()

        # Create a function to update the product list based on the selected category

    def update_product_list(self):
        self.product_combo['values'] = []
        if self.selected_category.get() == "Medicine":
            self.product_combo['values'] = [product[0] for product in self.products]
        elif self.selected_category.get() == "Product":
            self.product_combo['values'] = [product[0] for product in self.med_products]
            self.product_entry.delete(0, tk.END)
        # Create a function to update the price based on the selected product

    def update_price(self, *args):
        for product in self.products:
            if product[0] == self.selected_product.get():
                self.product_price_entry.delete(0, tk.END)
                self.product_price_entry.insert(0, product[5])
                break
        for product in self.med_products:
            if product[0] == self.selected_product.get():
                self.product_price_entry.delete(0, tk.END)
                self.product_price_entry.insert(0, product[4])
                break


if __name__ == "__main__":
    invoice = Invoice()
    invoice.mainloop()
