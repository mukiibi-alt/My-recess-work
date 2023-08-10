import tkinter as tk
from tkinter import messagebox


class ReceiptGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Receipt Generator")

        # Create labels and entry fields
        self.label_name = tk.Label(master, text="Customer Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_items = tk.Label(master, text="Purchased Items:")
        self.label_items.grid(row=1, column=0, sticky="e")
        self.entry_items = tk.Entry(master)
        self.entry_items.grid(row=1, column=1)

        self.label_total = tk.Label(master, text="Total Amount:")
        self.label_total.grid(row=2, column=0, sticky="e")
        self.entry_total = tk.Entry(master)
        self.entry_total.grid(row=2, column=1)

        # Create a button to generate the receipt
        self.button_generate = tk.Button(master, text="Generate Receipt", command=self.generate_receipt)
        self.button_generate.grid(row=3, columnspan=2)

    def generate_receipt(self):
        customer_name = self.entry_name.get()
        purchased_items = self.entry_items.get()
        total_amount = self.entry_total.get()

        # Validate inputs
        if not customer_name or not purchased_items or not total_amount:
            messagebox.showerror("Error", "Please enter all the details.")
            return

        # Create the receipt
        receipt = f"--- Receipt ---\n\nCustomer Name: {customer_name}\n\nPurchased Items: {purchased_items}\n\nTotal Amount: {total_amount}"

        # Print the receipt (you can replace this with your own logic for printing)
        print(receipt)

        # Show a success message
        messagebox.showinfo("Success", "Receipt generated successfully.")

        # Clear the entry fields
        self.entry_name.delete(0, tk.END)
        self.entry_items.delete(0, tk.END)
        self.entry_total.delete(0, tk.END)


root = tk.Tk()
receipt_generator = ReceiptGeneratorGUI(root)
root.mainloop()
