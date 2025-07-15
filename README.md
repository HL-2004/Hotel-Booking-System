# 🏨 Hotel Booking System (Tkinter + SQLite3)

A simple, interactive desktop application built with Python using **Tkinter** and **SQLite3** that allows you to **manage hotel room bookings**. This project is ideal for beginners and demonstrates database integration, GUI layout design, and CRUD operations.

---

## 🚀 Features

✅ **Book New Room**
- Enter customer name, room type, and number of nights
- Stores data with timestamp in SQLite3 database

✅ **View Booking History**
- Scrollable log of all past bookings
- Shows ID, name, room type, nights, check-in date

✅ **Delete Booking by ID**
- Delete a single booking using its unique ID

✅ **Clear All Bookings**
- Delete all records with one click (with confirmation)

✅ **Input Validation**
- Ensures name is entered and number of nights is valid

✅ **Improved UI**
- Clean layout using frames and labels
- Organized sections: Booking, History, Manage

---

## 🧰 Tech Stack

- `Python 3`
- `Tkinter` – GUI Framework
- `SQLite3` – Lightweight embedded database
- `datetime` – Timestamp check-in records

---

## 📁 Folder Structure

HotelBookingSystem/ │ ├── hotel.db                # SQLite3 database (auto-generated) ├── main.py                 # Main application script ├── README.md               # This file └── assets/ └── hotel_logo.png      # Project logo for portfolio (optional)

---

## ▶️ How to Run

1. Install Python (if not already)
2. Run the script:
   ```bash
   python main.py

3. No dependencies required. Works offline in environments like Pydroid 3 or IDLE.




---

📚 What You’ll Learn

Building real-world GUI apps in Python

SQLite database operations (insert, select, delete)

Organizing code for maintainability

GUI event handling and input validation



---

📌 To-Do / Enhancements

[ ] Export booking history to CSV or PDF

[ ] Add pricing and billing features

[ ] Add room availability and check-out system
