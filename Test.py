# Python program to determine which
# button was pressed in tkinter

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Create a function with one parameter, i.e., of
# the text you want to show when button is clicked
from functools import partial


def which_button(button_press):
    # Printing the text when a button is clicked
    print(button_press)

print("rrr")
# Creating and displaying of button b1
g = lambda: partial(which_button, 25)
for r in range(3):
    Button(app, text=r, command=partial(which_button, r)).grid(padx=10, pady=10)
g()
app.mainloop()
