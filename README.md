# 📇 Contact Book - Python GUI App

A lightweight desktop Contact Book application built using Python and Tkinter. This app allows users to manage their personal or professional contacts through an intuitive graphical interface. Data is securely stored in a local JSON file.

---

## 🚀 Features

- ➕ **Add Contacts** (Name, Phone, Email)
- 🔄 **Update Existing Contacts**
- ❌ **Delete Contacts**
- 🔍 **Search Contact by Name**
- 📋 **View All Contacts**
- 💾 **Persistent Storage** in a JSON file
- 📑 **Clean and Minimal GUI** using Tkinter

---

## 📦 Libraries Used

This app uses **only Python's standard library** — no external installations required.

- `tkinter` – GUI framework
- `json` – For saving/loading contacts
- `os` – For file checking

---

## 🧠 How It Works

- Contacts are stored in a file called `contacts.json`.
- When you add, update, or delete a contact, changes are immediately saved to the file.
- On app startup, the JSON file is loaded automatically.
- You can search for contacts by name and see details like phone and email.
- All contacts are displayed in a scrollable text box.

---

## 🚀 How to Run the App

# 1️⃣ Clone or Download the Repository

bash
`git clone https://github.com/YourUsername/contact-book-app.git
cd contact-book-app`


# 2️⃣ Run the Application

`bash
`python contact_book.py

---

## 📁 Project Structure

```bash
ContactBookApp/
├── contact_book.py        # Main Python script (this app)
├── contacts.json          # Auto-generated storage file
├── README.md              # Project documentation
