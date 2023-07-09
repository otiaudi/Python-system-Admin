import tkinter as tk
import os

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input_field.get()
        confirm = confirm_label.cget("text")
        if confirm == "Y":
            break
        confirm_label.config(text="remove the user: " + username + " ? (Y/N)")

    os.system("sudo userdel " + username)
    success_label.config(text="User successfully removed")

# Create the main window
window = tk.Tk()
window.title("User Removal")

# Create and position input label and field
input_label = tk.Label(window, text="Enter the name of the user to remove:")
input_label.pack()
input_field = tk.Entry(window)
input_field.pack()

# Create and position confirm label and button
confirm_label = tk.Label(window, text="N")
confirm_label.pack()
confirm_button = tk.Button(window, text="Confirm", command=remove_user)
confirm_button.pack()

# Create and position success label
success_label = tk.Label(window)
success_label.pack()

# Start the GUI event loop
window.mainloop()
