import tkinter as tk
from tkinter import messagebox

# File read Sign In function
def sign_in():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and password == stored_password:
                messagebox.showinfo("Success", "Login Successful!")
                main_menu()
                return

        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users registered yet")


# File write Sign Up function
def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

    messagebox.showinfo("Success", "Account Created Successfully!")
    sign_in_window()


# Sign In Window
def sign_in_window():
    global username_entry, password_entry

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Sign In", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)

    tk.Button(root, text="Go to Sign Up",
              command=sign_up_window).pack()


# Sign Up Window
def sign_up_window():
    global username_entry, password_entry

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Sign Up", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)

    tk.Button(root, text="Back to Sign In",
              command=sign_in_window).pack()


# Main Menu Window
def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(
        root,
        text="Welcome!",
        font=("Arial", 16)
    ).pack(pady=30)

    tk.Button(
        root,
        text="Logout",
        command=sign_in_window
    ).pack()


# Root Window
root = tk.Tk()
root.title("Application")
root.geometry("300x250")

sign_in_window()

root.mainloop()
