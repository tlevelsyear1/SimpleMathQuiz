# Import Tkinter Libraries
import tkinter as tk
from tkinter import ttk
import random
from tkinter import *
from PIL import Image, ImageTk

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

btnm = tk.Button(window, text="Multiplication", command=Mul)
btnm.place(x=30, y=20, width=125, height=50)
btnd = tk.Button(window, text="Division", command=Div)
btnd.place(x=30, y=100, width=125, height=50)
btna = tk.Button(window, text="Addition", command=Add)
btna.place(x=30, y=180, width=125, height=50)
btns = tk.Button(window, text="Subtraction", command=Sub)
btns.place(x=30, y=260, width=125, height=50)

#Create Widgets and images to use for UI
images = [
    tk.PhotoImage(file=f"Images/{i}.png") for i in range(10)
]
num1 = random.choice(images)
label = tk.Label(window, image=num1)
num1 = image.resize((50, 50))
label.place(x=150, y=150, width=50, height=50)

images = [
    tk.PhotoImage(file=f"Images/{i}.png") for i in range(10)
]
num2 = random.choice(images)
label = tk.Label(window, image=num2)
label.place(x=300, y=150, width=50, height=50)


#Pack frames and widgets in order you want on page


# Create window with elements 


window.mainloop()