import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    # Define regex patterns for different criteria
    length_pattern = r'^.{8,}$'  # At least 8 characters
    uppercase_pattern = r'[A-Z]'  # At least one uppercase letter
    lowercase_pattern = r'[a-z]'  # At least one lowercase letter
    digit_pattern = r'[0-9]'      # At least one digit
    special_char_pattern = r'[^A-Za-z0-9]'  # At least one special character

    # Check each criterion
    length = bool(re.match(length_pattern, password))
    uppercase = bool(re.search(uppercase_pattern, password))
    lowercase = bool(re.search(lowercase_pattern, password))
    digit = bool(re.search(digit_pattern, password))
    special_char = bool(re.search(special_char_pattern, password))

    # Calculate overall strength score
    strength_score = sum([length, uppercase, lowercase, digit, special_char])

    # Determine strength level
    if strength_score == 5:
        return "Very Strong"
    elif strength_score >= 3:
        return "Strong"
    elif strength_score >= 2:
        return "Moderate"
    elif strength_score >= 1:
        return "Weak"
    else:
        return "Very Weak"

def evaluate_password():
    password = password_entry.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password strength: {strength}")

# Create a Tkinter window
window = tk.Tk()
window.title("Password Strength Tester")

# Increase the size of the text entry
password_entry = tk.Entry(window, show="*", width=50)
password_entry.pack(pady=20)

# Center the entry field and button horizontally
password_entry.pack(ipadx=10, ipady=5)
password_entry.pack(fill=tk.X, padx=20)

# Add a button to evaluate the password
evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_password, width=20)
evaluate_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
