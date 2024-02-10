import subprocess
from tkinter import *

# Define a function to open the 'main.py' GUI app
def open_main_app():
    subprocess.Popen(['python', 'main.py'])

# Create the main window
root = Tk()
root.title("SmartQuiz")

# Create a menu
menu = Menu()
menu.add_command(label="Quit", command=root.destroy)
root.config(menu=menu)

# Define a function to load images
def image(smp):
    img = PhotoImage(file="mainLogo.png")
    img = img.subsample(smp)
    return img

# Create the GUI elements
title = Label(root, text="SmartQuiz Application", width=50, bg="green", fg="white", font=("arial", 20, "bold"))
title.pack()

but = Button(root, bd=0, relief="groove", compound=CENTER, bg="white", activeforeground="light blue", activebackground="white", pady=10, padx=20)

title.lbl1 = Label(root, text="Welcome To The Quiz!", font=("Arial", 45), background="cyan", compound=CENTER)
title.lbl1.pack()

img = image(2)
but.config(image=img)
but.pack()

lbl2 = Label(root, text="Press enter to begin", font=("Arial", 20), background="cyan")
lbl2.pack()

# Create the "Enter" button to open the 'main.py' app
enterButton = Button(root, text="Enter", font=("Arial", 25), relief="groove", background="white", command=open_main_app, compound=CENTER)
enterButton.pack()

root.geometry("650x500")
root.mainloop()
