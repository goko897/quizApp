import tkinter as tk
import mysql.connector
from tkinter import messagebox
import subprocess

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bhavana123',
            database='userData'
        )

        cursor = connection.cursor()

        # Execute a query to check if the credentials are valid
        query = "insert users (password,username) VALUES (%s,%s)"
        cursor.execute(query, (username, password))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            # Successful login, open the main application using subprocess
            subprocess.Popen(['python', 'main.py'])
            login_window.destroy()  # Close the login window
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", str(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Load and display a background image
bg_image = tk.PhotoImage(file="background_image.png")
bg_label = tk.Label(login_window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create labels and entry fields for username and password
username_label = tk.Label(login_window, text="Username", bg="white")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password", bg="white")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Create the login button
login_button = tk.Button(login_window, text="Login", command=check_credentials, bg="green")
login_button.pack()

login_window.geometry("400x400")
login_window.mainloop()
