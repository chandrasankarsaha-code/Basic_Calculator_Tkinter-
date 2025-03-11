import tkinter
from tkinter import *
from tkinter import messagebox

# Create main window
window=Tk()
window.title("Basic_Calculator")


# Function to add numbers to the entry field
def btn_add(number):
    current=entry_text.get()
    e1.insert(END,number)

# Function to clear the entry field
def btn_clear():
    e1.delete(0,END)

# Function to clear the entry field
def btn_Backspace():
    current_num=e1.get()
    if current_num:
        e1.delete(len(current_num) -1,END)

# Function to add a decimal point (only if not already present)
def btn_Dot():
    current1 =e1.get()
    if "." not in current1:
        e1.insert(END,".")
        
# Function to toggle negative/positive numbers
def btn_Negact():
    current=e1.get()
    if current:
        if current[0]=="-":
            e1.delete(0,1)
        else:
            e1.insert(0,"-")
    
# Function for addition operation
def btn_addition():
    first_number=e1.get()
    global f_num,math
    try:
      f_num=float(first_number)
      math="addition"
      e1.delete(0,END)
    except ValueError:
        messagebox.showerror("Error","you have enterd wrong input")
        
# Function for subtraction operation
def btn_subtract():
    first_number=e1.get()
    try:
        global f_num,math
        f_num=float(first_number)
        math="subtraction"
        e1.delete(0,END)
    except ValueError:
        messagebox.showerror("Error","you have enterd wrong input")

# Function for multiplication operation
def btn_multiply():
    first_number=e1.get()
    try:
        global f_num,math
        f_num=float(first_number)
        math="multiplication"
        e1.delete(0,END)
    except ValueError:
        messagebox.showerror("Error","you have enterd wrong input")


# Function for division operation
def btn_division():
    first_number=e1.get()
    try:
        global f_num,math
        f_num=float(first_number)
        math="division"
        e1.delete(0,END)
    except ValueError:
        messagebox.showerror("Error","you have enterd wrong input")

# Function for modulus operation
def btn_modulas():
    first_number=e1.get()
    global f_num,math
    try:
       f_num=float(first_number)
       math="modulas"
       e1.delete(0,END)
    except ValueError:
        messagebox.showerror("Error","you have enterd wrong input")

# Function to compute and display the result
def btn_equal():
    second_number=e1.get()
    e1.delete(0,END)
    try:
     s_num=float(second_number) 
     if math=="addition":
            result=f_num + s_num
     elif math == "subtraction":
            result=f_num - s_num
     elif math =="multiplication":
            result=f_num * s_num
     elif math =="division":
            if s_num==0:
                messagebox.showerror("Error","Can't be divided by zero.")
            result=f_num / s_num
     elif math =="modulas":
            result=f_num % s_num
     """elif math == "sq_root":
            result=f_num ^ s_num"""

# Display result (as integer if there's no decimal part)
     e1.insert(0,int(result)
               if result.is_integer()
               else result)
     
    except ValueError:
         messagebox.showerror("Error","you have enterd wrong input")
   

# Entry field for user input
entry_text=StringVar()
e1=Entry(
    window,
    font=("Helvetica",15),
    width=25,
    borderwidth=5,
    textvariable=entry_text

)
e1.grid(row=0,column=0,columnspan=3,ipady=5)

# Number buttons
btn0=Button(window,text="0",padx=30,pady=10,command=lambda:btn_add(0))
btn1=Button(window,text="1",padx=30,pady=10,command=lambda:btn_add(1))
btn2=Button(window,text="2",padx=30,pady=10,command=lambda:btn_add(2))
btn3=Button(window,text="3",padx=30,pady=10,command=lambda:btn_add(3))
btn4=Button(window,text="4",padx=30,pady=10,command=lambda:btn_add(4))
btn5=Button(window,text="5",padx=30,pady=10,command=lambda:btn_add(5))
btn6=Button(window,text="6",padx=30,pady=10,command=lambda:btn_add(6))
btn7=Button(window,text="7",padx=30,pady=10,command=lambda:btn_add(7))
btn8=Button(window,text="8",padx=30,pady=10,command=lambda:btn_add(8))
btn9=Button(window,text="9",padx=30,pady=10,command=lambda:btn_add(9))

# Special buttons
btn_dot=Button(window,text=".",padx=30,pady=10,command=btn_Dot)
btn_negect=Button(window,text="+/-",padx=25,pady=10,command=btn_Negact)
btn_backspace=Button(window,text="⌫",padx=25,pady=10,command=btn_Backspace)
btn_clear=Button(window,text="Clear",command=btn_clear,)

# Operator buttons
btn_Plus=Button(window,text="+",padx=30,pady=10,command=btn_addition)
btn_subtract=Button(window,text="-",padx=30,pady=10,command=btn_subtract)
btn_multiplication=Button(window,text="*",padx=30,pady=10,command=btn_multiply)
btn_division=Button(window,text="/",padx=30,pady=10,command=btn_division)
btn_Modular=Button(window,text="%",padx=30,pady=10,command=btn_modulas)

# Equal button
btn_eql=Button(window,text="=",padx=30,pady=10,command=btn_equal,)

# Positioning buttons in grid layout
btn0.grid(row=5,column=1,sticky="nsew")

btn1.grid(row=4,column=0,sticky="nsew")
btn2.grid(row=4,column=1,sticky="nsew")
btn3.grid(row=4,column=2,sticky="nsew")

btn4.grid(row=3,column=0,sticky="nsew")
btn5.grid(row=3,column=1,sticky="nsew")
btn6.grid(row=3,column=2,sticky="nsew")

btn7.grid(row=2,column=0,sticky="nsew")
btn8.grid(row=2,column=1,sticky="nsew")
btn9.grid(row=2,column=2,sticky="nsew")

btn_negect.grid(row=5,column=0,sticky="nsew")
btn_dot.grid(row=5,column=2,sticky="nsew")
btn_backspace.grid(row=0,column=3,sticky="nsew")
btn_clear.grid(row=4,column=3,sticky="nsew")

btn_Plus.grid(row=1,column=0,sticky="nsew")
btn_subtract.grid(row=1,column=1,sticky="nsew")
btn_multiplication.grid(row=1,column=2,sticky="nsew")
btn_division.grid(row=1,column=3,sticky="nsew")
btn_Modular.grid(row=2,column=3,sticky="nsew")

btn_eql.grid(row=5,column=3,sticky="nsew")


# Run the GUI application
window.mainloop()
