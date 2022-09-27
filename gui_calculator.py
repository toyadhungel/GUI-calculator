# importing the required libraries  
import tkinter  
from tkinter import *  
from tkinter import messagebox  
  
# setting the initial values of some variables  
var = ""  
A = 0  
operator = ""  
  
# defining the function for Button 1  
def btn_1_is_Clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
  
# defining the function for Button 2  
def btn_2_is_Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
  
# defining the function for Button 3  
def btn_3_is_Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
# defining the function for Button 4  
def btn_4_is_Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  
  
# defining the function for Button 5  
def btn_5_is_Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
# defining the function for Button 6  
def btn_6_is_Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
# defining the function for Button 7  
def btn_7_is_Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
  
# defining the function for Button 8  
def btn_8_is_Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
# defining the function for Button 9  
def btn_9_is_Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
  
# defining the function for Button 0  
def btn_0_is_Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
# defining the function for Button +  
def btn_Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  
# defining the function for Button -  
def btn_Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
  
# defining the function for Button *  
def btn_Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
  
# defining the function for Button /  
def btn_Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  
  
# defining the function for Button =  
def btn_Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  
# defining the function for Button C  
def btn_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  
# defining the function to display result  
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
  
# creating an object of the Tk() class  
guiWindow = tkinter.Tk()  
# setting the size of the window  
guiWindow.geometry("320x500+400+400")  
# disabling the resize option for better UI  
guiWindow.resizable(0, 0)  
# setting the title of the Calculator window  
guiWindow.title("GUI Calculator")  
  
# creating the label for the window  
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
# using the pack() method  
guiLabel.pack(expand = True, fill = "both")  
  
# creating the frames for the buttons  
# first frame  
frameOne = Frame(guiWindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both") # frame can expand if it gets some space  
  
# second frame  
frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  
# third frame  
frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  
  
# fourth frame  
frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
  
# creating buttons for each frame  
# buttons for first frame  
# button 1  
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_1_is_Clicked  
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 2  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_2_is_Clicked  
)  
# placing buttons side by side  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  
  
# button 3  
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_3_is_Clicked  
)  
# placing buttons side by side  
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  
# button C  
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_C_is_Clicked  
)  
# placing buttons side by side  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for second frame  
# button 4  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_4_is_Clicked  
)  
# placing buttons side by side  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
# button 5  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_5_is_Clicked  
)  
# placing buttons side by side  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 6  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_6_is_Clicked  
)  
# placing buttons side by side  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Add_is_Clicked  
)  
# placing buttons side by side  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for third frame  
# button 7  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_7_is_Clicked  
)  
# placing buttons side by side  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
# button 8  
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_8_is_Clicked  
)  
# placing buttons side by side  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
# button 9  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_9_is_Clicked  
)  
# placing buttons side by side  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Sub_is_Clicked  
)  
# placing buttons side by side  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for fourth frame  
# button 0  
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_0_is_Clicked  
)  
# placing buttons side by side  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
# button *  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Mul_is_Clicked  
)  
# placing buttons side by side  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
# button /  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = btn_Div_is_Clicked  
)  
# placing buttons side by side  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Sitka ", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  
# placing buttons side by side  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
  
# running the GUI  
guiWindow.mainloop()  
