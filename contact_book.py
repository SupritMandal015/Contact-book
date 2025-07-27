import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()

    def update_contact(self, name, phone, email):
        if name in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return True
        return False

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def get_all_contacts(self):
        return self.contacts


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.manager = ContactManager()

        # Entry fields
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky='e')
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, sticky='e')
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, sticky='e')
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1)

        # Buttons
        tk.Button(self.root, text="Add", command=self.add_contact).grid(row=3, column=0, pady=5)
        tk.Button(self.root, text="Update", command=self.update_contact).grid(row=3, column=1)
        tk.Button(self.root, text="Delete", command=self.delete_contact).grid(row=4, column=0)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=4, column=1)
        tk.Button(self.root, text="View All", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=5)

        # Display Area
        self.result_text = tk.Text(self.root, width=50, height=10)
        self.result_text.grid(row=6, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        if name and phone and email:
            self.manager.add_contact(name, phone, email)
            messagebox.showinfo("Success", f"Contact '{name}' added.")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def update_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        if self.manager.update_contact(name, phone, email):
            messagebox.showinfo("Success", f"Contact '{name}' updated.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.clear_fields()

    def delete_contact(self):
        name = self.name_var.get()
        if self.manager.delete_contact(name):
            messagebox.showinfo("Success", f"Contact '{name}' deleted.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.clear_fields()

    def search_contact(self):
        name = self.name_var.get()
        contact = self.manager.get_contact(name)
        self.result_text.delete(1.0, tk.END)
        if contact:
            self.result_text.insert(tk.END, f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
        else:
            self.result_text.insert(tk.END, "Contact not found.")
        self.clear_fields()

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        contacts = self.manager.get_all_contacts()
        if contacts:
            for name, info in contacts.items():
                self.result_text.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n")
        else:
            self.result_text.insert(tk.END, "No contacts available.")

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
