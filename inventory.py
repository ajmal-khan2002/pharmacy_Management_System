import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import tkinter as Toplevel


class MedicineInventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medicine Inventory")
        self.geometry('1275x640+0+0')
        self.configure(background='white')
        # self.resizable(False, False)
        # Set the icon of the window
        self.iconbitmap('image/icon.ico')

        self.create_widgets()
        self.load_medicines()

    def dash(self):
        import home_page
        self.destroy()
        home_page.Homepage()

    def create_widgets(self):
        # Create the input fields

        # vertically top frame1
        self.frame = tk.Frame(width=1275, height=33, bg='cyan4')
        self.frame.place(x=0, y=0)

        #  vertoically  frame 2
        self.frame = tk.Frame(width=1275, height=3, bg='cyan4')
        self.frame.place(x=0, y=85)

        # LEFT SIDE FRAME
        self.frame = tk.Frame(width=3, height=115, bg='cyan4')
        self.frame.place(x=0, y=30)

        # Right SIDE FRAME
        self.frame = tk.Frame(width=4, height=115, bg='cyan4')
        self.frame.place(x=1271, y=30)

        #  horizontal frame 1
        self.frame = tk.Frame(width=3, height=120, bg='cyan4')
        self.frame.place(x=200, y=30)

        #  horizontal frame 2
        self.frame = tk.Frame(width=3, height=120, bg='cyan4')
        self.frame.place(x=400, y=30)

        #  horizontal frame 3
        self.frame = tk.Frame(width=3, height=120, bg='cyan4')
        self.frame.place(x=600, y=30)

        #  horizontal frame 4
        self.frame = tk.Frame(width=3, height=120, bg='cyan4')
        self.frame.place(x=800, y=30)

        #  horizontal frame 5
        self.frame = tk.Frame(width=3, height=160, bg='cyan4')
        self.frame.place(x=1000, y=30)

        # Tree view  FRAME
        self.frame = tk.Frame(width=1275, height=495, bg='cyan4')
        self.frame.place(x=0, y=145)

        name_label = tk.Label(self, text="+ PHARMACY", bg="cyan4", font=('Oswald', 15))
        name_label.place(x=6, y=3)

        # ====== Name============
        name_label = tk.Label(self, text="Medicine Name:", bg="white",font=("bold",12))
        name_label.place(x=10, y=35)
        self.name_entry = tk.Entry(self)
        self.name_entry.place(x=10, y=60)

        # Create quantity label and spinbox
        self.quantity_label = Toplevel.Label(self, text="Quantity", bg="white", font=("bold", 12))
        self.quantity_label.place(x=10, y=90)
        self.quantity_spinbox = ttk.Spinbox(self, from_=1, to=100)
        self.quantity_spinbox.place(x=10, y=115)

        # ====== Medicine Type ============
        # Create type label and combobox
        type_label = Toplevel.Label(self, text="Type", bg="white" ,font=("bold",12))
        type_label.place(x=210, y=35)
        self.type_combobox = ttk.Combobox(self,
                                          values=["", "Tablets", "Capsules", "Liquids", "Injectables",
                                                  "Topicals", "Inhalers", "Suppositories", "Transdermal",
                                                  "Powders", "Drops"])
        self.type_combobox.place(x=210, y=60)



        # Create GST label and spinbox
        gst_label = Toplevel.Label(self, text="G.S.T %", bg="white" ,font=("bold",12))
        gst_label.place(x=210, y=90)
        self.gst_spinbox = ttk.Spinbox(self, from_=12, to=18)
        self.gst_spinbox.place(x=210, y=115)

        # Create MRP label and entry
        mrp_label = Toplevel.Label(self, text="MRP", bg="white" ,font=("bold",12))
        mrp_label.place(x=410, y=35)
        self.mrp_entry = Toplevel.Entry(self)
        self.mrp_entry.place(x=410, y=60)

        # ====== Price============
        purchase_label = tk.Label(self, text="Purchase:", bg="white" ,font=("bold",12))
        purchase_label.place(x=410, y=90)
        self.purchase_entry = tk.Entry(self)
        self.purchase_entry.place(x=410, y=115)

        # create the Manufacture Date label and entry
        self.manuf_label = Toplevel.Label(self, text="Manufacture Date: [D/M/Y]", bg="white" ,font=("bold",11))
        self.manuf_label.place(x=610, y=35)
        self.manuf_entry = Toplevel.Entry(self)
        self.manuf_entry.place(x=610, y=60)

        # ====== Expiry Date ============
        expiry_label = tk.Label(self, text="Expiry Date: [D/M/Y]", bg="white",font=("bold",11))
        expiry_label.place(x=610, y=90)
        self.expiry_entry = tk.Entry(self)
        self.expiry_entry.place(x=610, y=115)

        # Create batch label and entry
        self.batchCode_label = Toplevel.Label(self, text="Batch Code", bg="white" ,font=("bold",12))
        self.batchCode_label.place(x=810, y=35)
        self.batchCode_entry = Toplevel.Entry(self)
        self.batchCode_entry.place(x=810, y=60)

        # Create Company Name label and entry
        self.company_name_label = Toplevel.Label(self, text="Company Name", bg="white", font=("bold", 12))
        self.company_name_label.place(x=810, y=90)
        self.company_name_entry = Toplevel.Entry(self)
        self.company_name_entry.place(x=810, y=115)

        # Add a label to display the count of medicine notes
        self.count_label = tk.Label(text="Total Product : 0", bg='white', font=("bold", 15))
        self.count_label.place(x=1050, y=45)

        # ====== Save Button ============
        add_button = tk.Button(self, text="Add Medicine", command=self.add_medicine, bg="white", bd=0,
                               font=('Roboto Condensed', 15), cursor='hand2')
        add_button.place(x=1020, y=100)

        # ============= Delete the data===============
        self.button = tk.Button(text="Delete", command=self.delete_item, font=('Roboto Condensed', 15),
                                bd=0, background="white", activebackground="white", cursor='hand2')
        self.button.place(x=1160, y=100)

        # ============= Home page===============
        self.button = tk.Button(text="Dashboard",command=self.dash, font=('Roboto Condensed', 13,"bold"),
                                bd=0, background="cyan4", activebackground="cyan4", cursor='hand2')
        self.button.place(x=950, y=2)

        # ========== Search bar===============
        self.search_entry = tk.Entry()
        self.search_entry.place(x=1070, y=7)
        self.search_button = tk.Button(text=": Search:", command=self.search_item, cursor='hand2',
                                       font=('Roboto Condensed', 11),
                                       bd=0, background="cyan4", activebackground="cyan4")
        self.search_button.place(x=1200, y=4)

        # Create the tree view
        self.tree = ttk.Treeview(self,
                                 columns=("Name",  "Quantity","Types", "GST %", "MRP", "Purchase", "Manufacture Date",
                                          "Expiry Date", "Batch Code","Company Name"), show="headings", height=23)
        self.tree.heading("Name", text="Medicine Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Types", text="Types")
        self.tree.heading("GST %", text="G.S.T %")
        self.tree.heading("MRP", text="MRP")
        self.tree.heading("Purchase", text="Purchase")
        self.tree.heading("Manufacture Date", text="Manufacture Date")
        self.tree.heading("Expiry Date", text="Expiry Date")
        self.tree.heading("Batch Code", text="Batch Code")
        self.tree.heading("Company Name", text="Company Name")



        self.tree.column("Name", width=230)
        self.tree.column("Quantity", width=80)
        self.tree.column("Types", width=130)
        self.tree.column("GST %", width=80)
        self.tree.column("MRP", width=80)
        self.tree.column("Purchase", width=80)
        self.tree.column("Manufacture Date", width=140)
        self.tree.column("Expiry Date", width=140)
        self.tree.column("Batch Code", width=100)
        self.tree.column("Company Name", width=205)

        self.tree.place(x=3, y=149)

    def add_medicine(self):
        name = self.name_entry.get()
        quantity = self.quantity_spinbox.get()
        types = self.type_combobox.get()
        gst = self.gst_spinbox.get()
        mrp = self.mrp_entry.get()
        purchase = self.purchase_entry.get()
        manufacture = self.manuf_entry.get()
        expiry = self.expiry_entry.get()
        batch = self.batchCode_entry.get()
        company = self.company_name_entry.get()

        # ====================== Perform validation checks=============
        # Check if all fields are filled
        if not all((name, quantity, types,  gst, mrp, purchase, manufacture, expiry, batch, company)):
            messagebox.showwarning("Error", "Please fill all fields!")
            return
        else:
            with open('medicine.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, quantity, types,  gst, mrp, purchase, manufacture, expiry, batch , company])

            self.name_entry.delete(0, tk.END)
            self.quantity_spinbox.delete(0, tk.END)
            self.type_combobox.delete(0, tk.END)
            self.gst_spinbox.delete(0, tk.END)
            self.mrp_entry.delete(0, tk.END)
            self.purchase_entry.delete(0, tk.END)
            self.manuf_entry.delete(0, tk.END)
            self.expiry_entry.delete(0, tk.END)
            self.batchCode_entry.delete(0, tk.END)
            self.company_name_entry.delete(0, tk.END)

            messagebox.showinfo("Success", "Medicine added successfully!")

            self.load_medicines()

    def load_medicines(self):
        self.tree.delete(*self.tree.get_children())

        expired_medicines = []
        non_expired_medicines = []

        with open('medicine.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            for row in rows:
                self.tree.insert('', tk.END, values=row)
                count = len(self.tree.get_children())
                self.count_label.config(text=f"Total Product : {count}")

                if len(row) >= 3:
                    quantity = int(row[1])
                    if quantity == 0:
                        messagebox.showwarning("Zero Quantity", f"The medicine '{row[0]}' has a quantity of zero!")
                    else:
                        expiry_date_parts = row[7].split('/')
                        if len(expiry_date_parts) >= 3:
                            expiry_date = date(int(expiry_date_parts[2]), int(expiry_date_parts[1]),
                                               int(expiry_date_parts[0]))

                            if date.today() > expiry_date:
                                messagebox.showwarning("Expired", f"The medicine '{row[0]}' has expired!")
                                expired_medicines.append(row)
                            else:
                                non_expired_medicines.append(row)

        with open('medicine.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(non_expired_medicines)

        with open('deleted_medicines.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expired_medicines)

        self.tree.delete(*self.tree.get_children())  # Clear existing data
        for row in non_expired_medicines:
            self.tree.insert('', tk.END, values=row)
            count = len(self.tree.get_children())
            self.count_label.config(text=f"Total Product : {count}")

    def delete_item(self):
        # Get the selected item
        selected_item = self.tree.focus()

        # Make sure an item is selected
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete.")
            return

        # Get the name of the selected item
        name = self.tree.item(selected_item, "values")[0]

        # Ask for confirmation
        confirmed = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?")
        if not confirmed:
            return

        # Remove the item from the treeview
        self.tree.delete(selected_item)

        # Remove the item from the CSV file
        with open('medicine.csv', "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != name]
        with open('medicine.csv', "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        messagebox.showinfo("Success", f"{name} has been deleted.")
        count = len(self.tree.get_children())
        self.count_label.config(text=f"Total Product : {count}")

    def search_item(self):
        search_query = self.search_entry.get().lower()
        for child in self.tree.get_children():
            item_name = self.tree.item(child, "values")[0].lower()
            if search_query in item_name:
                self.tree.selection_set(child)
                self.tree.focus(child)
                self.tree.see(child)
                break
        else:
            messagebox.showinfo("Not found", f"No item found matching '{search_query}'")


if __name__ == '__main__':
    app = MedicineInventoryApp()
    app.mainloop()

