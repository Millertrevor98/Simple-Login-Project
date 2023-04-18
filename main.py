from tkinter import *

# Create a new window
root = Tk()
root.title("Login")

# Set the window size and position
root.geometry("300x250")
root.resizable(False, False)
root.configure(bg='#333333')

# Add a label widget
lbl = Label(root, text="Login", font=("Arial", 20), bg='#333333', fg='#ffffff')
lbl.pack(pady=10)

# Add a username label and entry widget
user_lbl = Label(root, text="Username (min 3, max 10)", font=("Arial", 12), bg='#333333', fg='#ffffff')
user_lbl.pack(pady=5)
user_entry = Entry(root, width=30, bg='#cccccc')
user_entry.pack()

# Add a password label and entry widget
pass_lbl = Label(root, text="Password (min 6, max 15)", font=("Arial", 12), bg='#333333', fg='#ffffff')
pass_lbl.pack(pady=5)
pass_entry = Entry(root, width=30, show="*", bg='#cccccc')
pass_entry.pack()

# Add a login button
def login():
    username = user_entry.get()
    password = pass_entry.get()
    if len(username) < 3 or len(username) > 10 or len(password) < 6 or len(password) > 15:
        result_lbl.configure(text="Login denied")
    else:
        result_lbl.configure(text="Login successful")

login_btn = Button(root, text="Login", font=("Arial", 12), bg='#4CAF50', fg='#fff', pady=5, padx=10, command=login)
login_btn.pack(pady=10)

# Add a result label
result_lbl = Label(root, text="", font=("Arial", 12), bg='#333333', fg='#ffffff')
result_lbl.pack(pady=5)

# Run the window
root.mainloop()
