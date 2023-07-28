import random
import string
import tkinter as tk
from tkinter import messagebox

def gen_passwd(length):
    ch = string.ascii_letters + string.digits + string.punctuation
    passwd = ''.join(random.choice(ch) for _ in range(length))
    return passwd

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        messagebox.showerror("Invalid Length", "Please enter a positive length.")
        return
    password = gen_passwd(length)
    gen_entry.delete(0, tk.END)  # Clear the existing text in the entry
    gen_entry.insert(0, password)  # Insert the generated password in the entry

# Create the main Tkinter window
window = tk.Tk()
window.title("Password Generator")
window.geometry("250x180")
# Create a label and an entry for the username
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

# Create a label and an entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=1, column=0)
length_entry = tk.Entry(window)
length_entry.grid(row=1, column=1)

# Create a label for the generated password
gen_label = tk.Label(window, text="Generated Password:")
gen_label.grid(row=2, column=0)

# Create an entry for the generated password
gen_entry = tk.Entry(window)
gen_entry.grid(row=2, column=1)

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=4, columnspan=2)

# Create a label to display the generated password
password_label = tk.Label(window, text="")
password_label.grid(row=5, columnspan=2)

accept = tk.Button(window, text="Accept")
accept.grid(row=6, columnspan=2)
reset = tk.Button(window, text="Reset")
reset.grid(row=7, columnspan=2)
# Start the Tkinter event loop
window.mainloop()
