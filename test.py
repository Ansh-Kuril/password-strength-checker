import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = any(char.isupper() for char in password)
    lower_case_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)
    
    strength = 0
    if length_criteria:
        strength += 1
    if upper_case_criteria:
        strength += 1
    if lower_case_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1
        
    return strength

def evaluate_password():
    password = entry.get()
    strength = check_password_strength(password)
    
    if strength == 5:
        messagebox.showinfo("Password Strength", "Very Strong")
    elif strength == 4:
        messagebox.showinfo("Password Strength", "Strong")
    elif strength == 3:
        messagebox.showinfo("Password Strength", "Medium")
    elif strength == 2:
        messagebox.showinfo("Password Strength", "Weak")
    else:
        messagebox.showinfo("Password Strength", "Very Weak")

# Set up the main application window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the label and entry widgets
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

# Create and place the button widget
button = tk.Button(root, text="Check Strength", command=evaluate_password)
button.pack(pady=10)

# Start the main event loop
root.mainloop()
