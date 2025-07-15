import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
from datetime import datetime

conn = sqlite3.connect('hotel.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bookings
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT, room_type TEXT, nights INTEGER, checkin TEXT)''')
conn.commit()

def book_room():
    name = name_entry.get().strip()
    room = room_var.get()
    try:
        nights_val = int(nights.get())
        if name and room and nights_val > 0:
            checkin_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO bookings (name, room_type, nights, checkin) VALUES (?, ?, ?, ?)",
                      (name, room, nights_val, checkin_time))
            conn.commit()
            messagebox.showinfo("Booking Confirmed", f"{name}, your {room} room is booked for {nights_val} night(s).")
            name_entry.delete(0, tk.END)
            nights.set(1)
            show_bookings()
        else:
            messagebox.showwarning("Missing Info", "Please fill in all fields correctly.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Number of nights must be a valid number.")

def show_bookings():
    bookings_text.delete("1.0", tk.END)
    c.execute("SELECT * FROM bookings ORDER BY id DESC")
    records = c.fetchall()
    if records:
        for r in records:
            bookings_text.insert(tk.END, f"ID: {r[0]}\nName: {r[1]}\nRoom: {r[2]}\nNights: {r[3]}\nCheck-in: {r[4]}\n{'-'*30}\n")
    else:
        bookings_text.insert(tk.END, "No bookings found.\n")

def delete_booking():
    try:
        delete_id = int(delete_entry.get())
        c.execute("DELETE FROM bookings WHERE id = ?", (delete_id,))
        conn.commit()
        if c.rowcount:
            messagebox.showinfo("Deleted", f"Booking ID {delete_id} deleted.")
        else:
            messagebox.showwarning("Not Found", "No booking found with that ID.")
        delete_entry.delete(0, tk.END)
        show_bookings()
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid numeric ID.")

def clear_all_bookings():
    if messagebox.askyesno("Confirm", "Delete ALL bookings?"):
        c.execute("DELETE FROM bookings")
        conn.commit()
        show_bookings()

root = tk.Tk()
root.title("Hotel Booking System")
root.geometry("420x600")
root.resizable(False, False)

booking_frame = tk.LabelFrame(root, text="New Booking", padx=10, pady=10)
booking_frame.pack(padx=10, pady=10, fill="x")

tk.Label(booking_frame, text="Customer Name").pack(anchor='w')
name_entry = tk.Entry(booking_frame, width=30)
name_entry.pack()

tk.Label(booking_frame, text="Room Type").pack(anchor='w')
room_var = tk.StringVar(value="Standard")
tk.OptionMenu(booking_frame, room_var, "Standard", "Deluxe", "Suite").pack(fill='x')

tk.Label(booking_frame, text="Number of Nights").pack(anchor='w')
nights = tk.IntVar(value=1)
tk.Spinbox(booking_frame, from_=1, to=30, textvariable=nights, width=5).pack()

tk.Button(booking_frame, text="Book Room", command=book_room, bg="lightgreen").pack(pady=5)

history_frame = tk.LabelFrame(root, text="Booking History", padx=10, pady=10)
history_frame.pack(padx=10, pady=5, fill="both", expand=True)

bookings_text = scrolledtext.ScrolledText(history_frame, width=50, height=12)
bookings_text.pack()
show_bookings()

delete_frame = tk.LabelFrame(root, text="Manage Bookings", padx=10, pady=10)
delete_frame.pack(padx=10, pady=10, fill="x")

tk.Label(delete_frame, text="Delete by Booking ID:").pack(anchor='w')
delete_entry = tk.Entry(delete_frame, width=10)
delete_entry.pack(anchor='w')

tk.Button(delete_frame, text="Delete Booking", command=delete_booking, bg="tomato").pack(pady=5)

tk.Button(delete_frame, text="Clear All Bookings", command=clear_all_bookings, bg="red", fg="white").pack()

root.mainloop()