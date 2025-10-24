# Import Tkinter Libraries
import tkinter as tk
from tkinter import ttk
import random
from tkinter import *
from PIL import Image, ImageTk

# Create Window with title and set size of window.
Mode = "None"
window = tk.Tk()
window.title('Simple Math Game')
window.geometry('700x400')  

#Check What Mode To Run
def Start():
    match Mode:
        case "Mul":
            print("Mul")
            Mlabel = tk.Label(window, image=(r"+.png"))
            Mlabel1.image = num1
            Mlabel1.place(x=225, y=125, width=75, height=75)
        case "Div":
            print("Div")
        case "Add":
            print("Add")
        case "Sub":
            print("Sub")
        case "None":
            print("None")
        case _:
            print("Error")

# Create Frames to organise widgets
def Mul():
    global Mode
    Mode = 'Mul'
    Start()

def Div():
    global Mode
    Mode = 'Div'
    Start()

def Add():
    global Mode
    Mode = 'Add'
    Start()

def Sub():
    global Mode
    Mode = 'Sub'
    Start()

#Buttons For Selecting Mode
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
label1.place(x=225, y=125, width=75, height=75)

#Generate Second Number Image
image_paths = [f"Images/{i}.png" for i in range(10)]

#Second Number Image
num2 = Image.open(random.choice(image_paths))
num2 = num2.resize((75, 75))
num2 = ImageTk.PhotoImage(num2)

label2 = tk.Label(window, image=num2)
label2.image = num2
label2.place(x=400, y=125, width=75, height=75)


#Pack frames and widgets in order you want on page


# Create window with elements 


window.mainloop()