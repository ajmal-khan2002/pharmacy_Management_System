# Importing the modules
import tkinter as tk
import csv
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

class MedicineNote:

    def __init__(self, master):
        # Setting the master window as an attribute
        self.master = master

        # Setting the title of the master window
        self.master.title("Medicine Note")
        self.master.configure(background='white')
        self.master.geometry("450x400")
        self.master.resizable(False, False)
        self.master.iconbitmap('image/icon.ico')
        # Creating a frame to hold the widgets
        self.frame = tk.Frame(self.master, bg='white')
        self.frame.place(x=5, y=5, width=430, height=130)

        # Creating the labels and entries for medicine name and date
        self.name_label = tk.Label(self.frame, text="Medicine Name:", bg='white')
        self.name_label.place(x=10, y=15)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.place(x=107, y=16)
        self.date_label = tk.Label(self.frame, text="Date:", bg='white')
        self.date_label.place(x=25, y=50)
        self.date_entry = DateEntry(self.frame)
        self.date_entry.place(x=108, y=51)
        # Creating a button to add data
        self.add_button = tk.Button(self.frame, text="Save", command=self.add_data, bg='white', width=10)
        self.add_button.place(x=115, y=100)

        # Creating a button to add data
        self.add_button = tk.Button(self.frame, text="Delete", command=self.delete_item, bg='white', width=10)
        self.add_button.place(x=20, y=100)


        # Creating another frame to hold the treeview
        self.tree_frame = tk.Frame(self.master)
        self.tree_frame.place(x=10, y=150)
        # Creating a scrollbar for the treeview
        self.scrollbar = tk.Scrollbar(self.tree_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Creating a treeview to display the data from the csv file
        self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.scrollbar.set)
        self.tree.pack()
        # Configuring the scrollbar to scroll with the treeview
        self.scrollbar.config(command=self.tree.yview)
        # Defining the columns for the treeview
        self.tree["columns"] = ("Name", "Date")
        # Formatting the columns for the treeview
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Name", anchor=tk.W, width=200)
        self.tree.column("Date", anchor=tk.W, width=200)
        # Creating the headings for the treeview
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Date", text="Date", anchor=tk.W)
        self.load_data()

        # Defining a method to add the data to the csv file and the treeview

    def add_data(self):
        # Getting the values from the entries
        name = self.name_entry.get()
        date = self.date_entry.get()
        # Checking if the values are not empty
        if name and date:
            # Opening the csv file in append mode
            with open("medicine_notes.csv", "a", newline="") as f:
                # Creating a csv writer object
                writer = csv.writer(f)
                # Writing the values as a row in the csv file
                writer.writerow([name, date])
                # Clearing the entries
                self.name_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
            # Inserting the values as an item in the treeview
            self.tree.insert("", tk.END, values=(name, date))

    def load_data(self):
        # Clear the existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Read data from the CSV file
        with open('medicine_notes.csv', "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                self.tree.insert("", tk.END, values=row)

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
        with open('medicine_notes.csv', "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != name]
        with open('medicine_notes.csv', "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        messagebox.showinfo("Success", f"{name} has been deleted.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicineNote(root)
    root.mainloop()


