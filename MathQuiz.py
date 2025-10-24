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

#Generate Random First Number
image_paths = [f"Images/{i}.png" for i in range(10)]

#First Number Image
num1 = Image.open(random.choice(image_paths))
num1 = num1.resize((75, 75))
num1 = ImageTk.PhotoImage(num1)

label1 = tk.Label(window, image=num1)
label1.image = num1
label1.place(x=175, y=150, width=75, height=75)

#Generate Second Number Image
image_paths = [f"Images/{i}.png" for i in range(10)]

#Second Number Image
num2 = Image.open(random.choice(image_paths))
num2 = num2.resize((75, 75))
num2 = ImageTk.PhotoImage(num2)

label2 = tk.Label(window, image=num2)
label2.image = num2
label2.place(x=350, y=150, width=75, height=75)


#Pack frames and widgets in order you want on page


# Create window with elements 


window.mainloop()