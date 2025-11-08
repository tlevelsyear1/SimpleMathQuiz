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

def RandQ():
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

    #Equals Sign Image
    equals = Image.open(r"C:\Users\ayoub\source\repos\KidsMathGame\Images\equals.png")
    equals = equals.resize((75, 75))
    equals = ImageTk.PhotoImage(equals)
    equalLabel = tk.Label(window, image=equals)
    equalLabel.image = equals
    equalLabel.place(x=495, y=125, width=75, height=75)


#Check What Mode To Run
def Start():
    match Mode:
        case "Mul":
            RandQ()
            print("Mul")
            oper = Image.open(r"C:\Users\ayoub\source\repos\KidsMathGame\Images\multiply.png")
            oper = oper.resize((75, 75))
            opertk = ImageTk.PhotoImage(oper)

            Mlabel = tk.Label(window, image=opertk)
            Mlabel.image = opertk
            Mlabel.place(x=315, y=125, width=75, height=75)
        case "Div":
             RandQ()
             print("Div")
             oper = Image.open(r"C:\Users\ayoub\source\repos\KidsMathGame\Images\divide.png")
             oper = oper.resize((75, 75))
             opertk = ImageTk.PhotoImage(oper)

             Dlabel = tk.Label(window, image=opertk)
             Dlabel.image = opertk
             Dlabel.place(x=315, y=125, width=75, height=75)
        case "Add":
            RandQ()
            print("Add")
            oper = Image.open(r"C:\Users\ayoub\source\repos\KidsMathGame\Images\plus.png")
            oper = oper.resize((75, 75))
            opertk = ImageTk.PhotoImage(oper)

            Alabel = tk.Label(window, image=opertk)
            Alabel.image = opertk
            Alabel.place(x=315, y=125, width=75, height=75)
        case "Sub":
            RandQ()
            print("Sub")
            oper = Image.open(r"C:\Users\ayoub\source\repos\KidsMathGame\Images\minus.png")
            oper = oper.resize((75, 75))
            opertk = ImageTk.PhotoImage(oper)

            Alabel = tk.Label(window, image=opertk)
            Alabel.image = opertk
            Alabel.place(x=315, y=125, width=75, height=75)
        case "None":
            print("None")
        case _:
            print("Error")

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

# Entry widget
answer = tk.Entry(window)
answer.place(x=300, y=220, width=100, height=50)

# Function to store input
def store_input():
    user_input = answer.get()  # Retrieve text from Entry
    print(user_input)  # You can now use this variable elsewhere

# Submit button with command
btnsubmit = tk.Button(window, text="Submit", command=store_input)
btnsubmit.place(x=410, y=220, width=100, height=50)


   


#Run the window loop
window.mainloop()