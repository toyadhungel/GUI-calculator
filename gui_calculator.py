  
import tkinter  
from tkinter import *  
from tkinter import messagebox  
#basic gui calculator
var = ""  
A = 0  
operator = ""  
   
def btn_1_is_Clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
  
def btn_2_is_Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
    
def btn_3_is_Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
def btn_4_is_Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  
  
def btn_5_is_Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
    
def btn_6_is_Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
 
def btn_7_is_Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
 
def btn_8_is_Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  

def btn_9_is_Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
  

def btn_0_is_Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
def btn_Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  

def btn_Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
  
def btn_Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  


def btn_Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
  

def btn_Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  

def btn_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  

def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 is Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  
  
 
guiWindow = tkinter.Tk()  
 
guiWindow.geometry("320x500+400+400")  

guiWindow.resizable(0, 0)  
 
guiWindow.title("Basic Calculator")  
  
the_data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    text = "Label",  
    anchor = SE,  
    font = ("Sitka  Math", 20),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  
 
guiLabel.pack(expand = True, fill = "both")  

frameOne = Frame(guiWindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both")
  

frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
   
frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  
  
frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
   
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_1_is_Clicked  
)
buttonONE.pack(side = LEFT, expand = True, fill = "both")  

buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_2_is_Clicked  
) 
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  

buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_3_is_Clicked  
)  

buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  

buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_C_is_Clicked  
)  
 
buttonC.pack(side = LEFT, expand = True, fill = "both")  
 
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_4_is_Clicked  
)  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_5_is_Clicked  
)  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_6_is_Clicked  
)   
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
   
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Add_is_Clicked  
)  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_7_is_Clicked  
)    
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_8_is_Clicked  
)  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_9_is_Clicked  
)  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
    
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border =0,  
    command = btn_Sub_is_Clicked  
)  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_0_is_Clicked  
)   
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Mul_is_Clicked  
)   
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
    
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Div_is_Clicked  
)  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
    
guiWindow.mainloop()  
