import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import csv


class PharmacyApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1100x637+80+2")
        self.master.resizable(False, False)
        self.master.title("General Product")
        self.master.configure(background='white')
        # Set the icon of the window
        self.master.iconbitmap('image/icon.ico')
        # LEFT SIDE FRAME
        self.frame = tk.Frame(width=3, height=160, bg='cyan4')
        self.frame.place(x=0, y=30)

        # RIGHT SIDE FRAME
        self.frame = tk.Frame(width=3, height=160, bg='cyan4')
        self.frame.place(x=1097, y=30)

        # UPPER MID BOARDER FRAME
        self.frame = tk.Frame(width=1100, height=3, bg='cyan4')
        self.frame.place(x=0, y=30)

        # UPPER FRAME
        self.frame = tk.Frame(width=1100, height=30, bg='cyan4')
        self.frame.place(x=0, y=0)

        # LOWER FRAME
        self.frame = tk.Frame(width=1100, height=495, bg='cyan4')
        self.frame.place(x=0, y=145)
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
        self.frame.place(x=845, y=30)

        #  vertoically  frame 2
        self.frame = tk.Frame(width=1100, height=3, bg='cyan4')
        self.frame.place(x=0, y=85)

        # Function back button
        def back():
            import home_page
            self.master.destroy()
            home_page.Homepage()

        # ========== Product Name Label and Entry
        self.name_label = tk.Label(text="Product Name:", bg="white",font=('Oswald', 10,"bold"))
        self.name_label.place(x=10, y=35)
        self.name_entry = tk.Entry()
        self.name_entry.place(x=10, y=60)

        # ==========Create quantity label and spinbox
        self.quantity_label = tk.Label(text="Quantity", bg="white",font=('Oswald', 10,"bold"))
        self.quantity_label.place(x=10, y=90)
        self.quantity_spinbox = ttk.Spinbox(from_=1, to=100, width=10)
        self.quantity_spinbox.place(x=10, y=115)

        # ========== Create GST label and spinbox
        self.gst_label = tk.Label(text="G.S.T %", bg="white",font=('Oswald', 10,"bold"))
        self.gst_label.place(x=210, y=35)
        self.gst_spinbox = ttk.Spinbox(from_=12, to=18, width=10)
        self.gst_spinbox.place(x=210, y=60)

        # ========== Create purchase price label and entry
        self.pur_label = tk.Label(text="Purchase Price", bg="white",font=('Oswald', 10,"bold"))
        self.pur_label.place(x=210, y=90)
        self.pur_entry = tk.Entry()
        self.pur_entry.place(x=210, y=115)

        # ========== Create price label and entry
        self.price_label = tk.Label(text="MRP", bg="white",font=('Oswald', 10,"bold"))
        self.price_label.place(x=410, y=35)
        self.price_entry = tk.Entry()
        self.price_entry.place(x=410, y=60)

        # =========== create the Manufacture Date label and entry
        self.manuf_label = tk.Label(text="Manufacture Date", bg="white",font=('Oswald', 10,"bold"))
        self.manuf_label.place(x=410, y=90)
        self.manuf_entry = DateEntry(width=12, background='cyan4', foreground='white', borderwidth=2)
        self.manuf_entry.place(x=410, y=115)

        # create the Expiring Date label and entry
        self.exp_label = tk.Label(text="Expiring Date", bg="white",font=('Oswald', 10,"bold"))
        self.exp_label.place(x=610, y=35)
        self.exp_entry = DateEntry(width=12, background='cyan4', foreground='white', borderwidth=2)
        self.exp_entry.place(x=610, y=60)

        # Add a label to display the count of medicine notes
        self.count_label = tk.Label(text="Total Product : 0", bg='white',font=('Oswald', 17,))
        self.count_label.place(x=890, y=43)

        # Save button
        self.button = tk.Button(text="Save", command=self.add_item,font=('Oswald', 17),
                                bd=0, background="white", activebackground="white", cursor='hand2')
        self.button.place(x=630, y=95)

        # ===========Referesh the date ===========
        self.button = tk.Button(text="Refresh", command=self.refresh_page,font=('Oswald', 17),
                                bd=0, background="white", activebackground="white", cursor='hand2')
        self.button.place(x=730, y=95)

        # ============= Delete the data===============
        self.button = tk.Button(text="Delete", command=self.delete_item, font=('Oswald', 17),
                                bd=0, background="white", activebackground="white", cursor='hand2')
        self.button.place(x=870, y=95)

        # ============= Delete the data===============
        self.button = tk.Button(text="Dashboard", command=back, font=('Oswald', 17),
                                bd=0, background="white", activebackground="white", cursor='hand2')
        self.button.place(x=969, y=95)

        # ========== Search bar===============
        self.search_entry = tk.Entry()
        self.search_entry.place(x=965, y=7)
        self.search_button = tk.Button(text="Search :", command=self.search_item, cursor='hand2',
                                       font=('Roboto Condensed', 11),
                                       bd=0, background="cyan4", activebackground="cyan4")
        self.search_button.place(x=900, y=4)

        # ============= CSV File

        self.tree = ttk.Treeview(
            columns=("Name", "Quantity", "GST %", "Purchase Price", "MRP", "Manufacture Date",
                     "Expiring Date"), show="headings", height=23,)

        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("GST %", text="GST %")
        self.tree.heading("Purchase Price", text="Purchase Price")
        self.tree.heading("MRP", text="MRP")
        self.tree.heading("Manufacture Date", text="Manufacture Date")
        self.tree.heading("Expiring Date", text="Expiring Date")
        self.tree.column("Name", width=206)
        self.tree.column("Quantity", width=135)
        self.tree.column("GST %", width=130)
        self.tree.column("Purchase Price", width=166)
        self.tree.column("MRP", width=125)
        self.tree.column("Manufacture Date", width=166)
        self.tree.column("Expiring Date", width=166)
        self.tree.place(x=2, y=148)

        self.filepath = "general.csv"
        self.load_data()

    def add_item(self):
        # Get the values from the form
        name = self.name_entry.get()
        quantity = self.quantity_spinbox.get()
        gst = self.gst_spinbox.get()
        pur = self.pur_entry.get()
        price = self.price_entry.get()
        manu = self.manuf_entry.get()
        exp = self.exp_entry.get()

        # ====================== Perform validation checks=============
        # Check if all fields are filled
        if not all((name, quantity, gst, pur, price, manu, exp)):
            messagebox.showwarning("Error", "Please fill all fields!")
            return

        # Check if the name is valid (contains only letters and spaces)
        if not name.replace(" ", ""):
            messagebox.showwarning("Error", "Invalid name!")
            return

        # Check if the quantity is valid (integer between 1 and 100)
        try:
            quantity = int(quantity)
            if quantity < 1 or quantity > 100:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Error", "Invalid quantity!")
            return

        # Check if the GST is valid (integer between 12 and 18)
        try:
            gst = int(gst)
            if gst < 12 or gst > 18:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Error", "Invalid GST!")
            return

        # Check if the purchase price is valid (float)
        try:
            pur = float(pur)
        except ValueError:
            messagebox.showwarning("Error", "Invalid purchase price!")
            return

        # Check if the MRP is valid (float)
        try:
            price = float(price)
        except ValueError:
            messagebox.showwarning("Error", "Invalid MRP!")
            return
        else:
            messagebox.showinfo("successfull", "Successfully submited")
        # Insert the values into the treeview
        self.tree.insert("", tk.END, values=(name, quantity, gst, pur, price, manu, exp))
        count = len(self.tree.get_children())
        self.count_label.config(text=f"Total Product : {count}")

        # Clear the form
        self.name_entry.delete(0, tk.END)
        self.quantity_spinbox.delete(0, tk.END)
        self.gst_spinbox.delete(0, tk.END)
        self.pur_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.manuf_entry.delete(0, tk.END)
        self.exp_entry.delete(0, tk.END)

        # Append the new row to the CSV file
        with open(self.filepath, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, quantity, gst, pur, price, manu, exp])

    def refresh_page(self):
        # Reload the data from the CSV file
        self.filepath = "general.csv"

    def load_data(self):
        # Clear the existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Read data from the CSV file
        with open(self.filepath, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                self.tree.insert("", tk.END, values=row)
                count = len(self.tree.get_children())
                self.count_label.config(text=f"Total Product : {count}")

        # ======= delete funcation==============

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
        with open(self.filepath, "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != name]
        with open(self.filepath, "w", newline="") as f:
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
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()
