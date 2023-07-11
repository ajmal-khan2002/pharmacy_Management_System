import tkinter as tk
import tkinter.ttk as ttk
import csv
from tkinter import messagebox


class Expiry:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1366x786')
        self.master.state('zoomed')
        # self.master.geometry("865x430+300+130")
        # self.master.resizable(False, False)
        self.master.title("Expiry Medicine")
        self.master.configure(background='white')

        # Set the icon of the window
        self.master.iconbitmap('image/icon.ico')

        def dash():
            import home_page
            self.master.destroy()
            home_page.Homepage()

        self.frame = tk.Frame(width=1280, height=648, bg='cyan4')
        self.frame.place(x=0, y=0)

        # ============= CSV File
        self.tree = ttk.Treeview(
            columns=("Name", "Quantity", "Category", "GST", "Purchase Price", "MRP",  "Manufacture Date",
                     "Expiring Date","code","Company Name"), show="headings", height=28)

        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Category", text="Category")
        self.tree.heading("GST", text="GST")
        self.tree.heading("Purchase Price", text="Purchase Price")
        self.tree.heading("MRP", text="MRP")
        self.tree.heading("Manufacture Date", text="Manufacture Date")
        self.tree.heading("Expiring Date", text="Expiring Date")
        self.tree.heading("code", text="code")
        self.tree.heading("Company Name", text="Company Name")

        self.tree.column("Name", width=200)
        self.tree.column("Quantity", width=100)
        self.tree.column("Category", width=145)
        self.tree.column("GST", width=80)
        self.tree.column("Purchase Price", width=80)
        self.tree.column("MRP", width=80)
        self.tree.column("Manufacture Date", width=150)
        self.tree.column("Expiring Date", width=160)
        self.tree.column("code", width=100)
        self.tree.column("Company Name", width=160)
        self.tree.place(x=20, y=35)

        # Create a label widget to display the total number of medicines
        self.count_label = tk.Label(text=f"Total Products: {self.tree.get_children()}",font=("bold", 12),bg="cyan4",)
        self.count_label.place(x=20, y=5)

        self.filepath = "deleted_medicines.csv"



        # Read data from the CSV file
        with open(self.filepath, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                self.tree.insert("", tk.END, values=row)
                count = len(self.tree.get_children())
                self.count_label.config(text=f"Total Product : {count}")



        # ============= Delete the data===============
        self.button = tk.Button(text="delete", font=("bold", 12), command=self.delete_item, bd=0, background="cyan4",
                                activebackground="cyan4", cursor='hand2')
        self.button.place(x=970, y=5)

        # ============= HOMEPAGE===============
        self.button = tk.Button(text="Dashboard", font=("bold", 12), command=dash, bd=0, background="cyan4",
                                activebackground="cyan4", cursor='hand2')
        self.button.place(x=850, y=5)

        # ========== Search bar===============
        self.search_entry = tk.Entry(width=22)
        self.search_entry.place(x=1050, y=10)
        self.search_button = tk.Button(text=": Search ", font=("bold", 12), command=self.search_item, bd=0,
                                       background="cyan4",
                                       activebackground="cyan4", cursor='hand2')
        self.search_button.place(x=1180, y=5)

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

        # Update the count label
        self.update_count_label()
    def update_count_label(self):
        # Update the count label with the number of rows in the Treeview
        count = len(self.tree.get_children())
        self.count_label.config(text=f"Total Medicines: {count}")

    # Refresh the entry fields
        self.search_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = Expiry(root)
    root.mainloop()
