# Import Tkinter Libraries
import tkinter as tk
from tkinter import ttk
import random

# Create Window with title and set size of window.

window = tk.Tk()
window.title('Simple Math Game')
window.geometry('700x400')  

# Create Frames to organise widgets
def Mul():
    Mode = 'Multiplication'

def Div():
    Mode = 'Division'

def Add():
    Mode = 'Addition'

def Sub():
    Mode = 'Subtraction'

btnm = tk.Button(window, text="Multiplication",width= 15,height= 2, command=Mul)
btnm.pack()
btnd = tk.Button(window, text="Division", command=Div)
btnd.pack()

#Create Widgets and images to use for UI


#Pack frames and widgets in order you want on page


# Create window with elements 


window.mainloop()