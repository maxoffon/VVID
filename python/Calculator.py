from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sympy import *

isGraphOn = False;
isSymOn = False;
expressionSee = "";
expressionUnSee = "";

def press(num):
    global expressionSee
    global expressionUnSee
    if(not isSymOn and (num == "x" or num == "y")):
        return
    expressionSee += str(num)
    if (num == "sin("):
        expressionUnSee += "math.sin("
    elif (num == "cos("):
        expressionUnSee += "math.cos("
    elif (num == "pi"):
        expressionUnSee += "math.pi"
    else:
        expressionUnSee += str(num);
    equation.set(expressionSee);
    
def equalPress():
    try:
        global expressionSee
        global expressionUnSee
        global isSymOn
        if (not isSymOn):
            total = str(eval(expressionUnSee))
            equation.set(total)
            expressionSee = total
            expressionUnSee = total
        else:
            press("=")
    except:
        equation.set('error')
        expressionSee = ""
        expressionUnSee = ""

def back():
    global expressionSee
    global expressionUnSee
    expressionSee = expressionSee[0:-1]
    expressionUnSee = expressionUnSee[0:-1]
    if (expressionSee == ""):
        clear();
    elif (expressionSee[len(expressionSee)-1] == "p"):
        expressionSee = expressionSee[0:-1]
        expressionUnSee = expressionUnSee[0:-6]
    elif (expressionSee[len(expressionSee)-1] == "n" or expressionSee[len(expressionSee)-1] == "s"):
        expressionSee = expressionSee[0:-3]
        expressionUnSee = expressionUnSee[0:-8]
    if (expressionSee == ""):
        clear();
    else:
        equation.set(expressionSee);

def clear():
    global expressionSee
    global expressionUnSee
    expressionSee = ""
    expressionUnSee = ""
    equation.set("0");

def changeStatus():
    global isSymOn;
    if (not isSymOn):
        label5 = Label(root, width = 4, height = 2, text = "ON", fg = "black", bg = "skyblue", font = fontson)
        isSymOn = True
    else:
        label5 = Label(root, width = 4, height = 2, text = "OFF", fg = "black", bg = "skyblue", font = fontson)
        isSymOn = False
    label5.place(x = 425, y = 15)
    clear()
    
    
def solveEq():
    global isSymOn;
    global isGraphOn;
    global expressionSee;
    global expressionUnSee;
    x,y = symbols('x y')
    xAr = np.linspace(-1,1,10)
    yAr = []
    if (not isSymOn): 
        return
    else:
        try:   
            if (not expressionSee.__contains__("=")):
                equation.set('error')
                expressionSee = ""
                expressionUnSee = ""
            else: 
                f = str(expressionSee).split("=")
                a = Eq(sympify(f[0]),sympify(f[1])) 
                c = ""
                if (expressionSee.__contains__("y")):
                    s = solve(a,y)
                    for j in range(len(s)):
                        for i in range(len(xAr)):
                            yAr.append(s[j].subs(x, xAr[i])) 
                        do_plot(xAr, yAr)
                        yAr.clear()
                    isGraphOn = True
                    eq = solve(a,y)
                    tempVar = "y" 
                else:
                    yAr = xAr
                    xAr = []
                    for i in range(len(yAr)):
                        xAr.append(solve(a.subs(y,yAr[i])))
                    eq = solve(a,x)
                    tempVar = "x"
                    do_plot(xAr, yAr)
                    isGraphOn = True
                for i in range(len(eq)):
                    if (i == len(eq)-1):
                        c += tempVar + " = " + str(eq[i])
                    else:
                        c += tempVar + " = " + str(eq[i]) + ","
                expressionSee = c
                expressionUnSee = c
                equation.set(c);
        except:
            equation.set('error')
            expressionSee = ""
            expressionUnSee = ""
    
def do_plot(x, y):
    global isGraphOn;
    if (isGraphOn):
        ax.clear()
        isGraphOn = False
    ax.plot(x,y)
    canvas.draw()

if __name__ == "__main__":
    root = Tk()
    root.configure(background = "skyblue")
    root.title("Calculator")
    root.geometry('1000x500')
    
    equation = StringVar()
    fontson = ("Verdana", 18)
    fontsin = ("Verdana", 40)
    fontsan = ("Verdana", 8)
    
    label2 = Label(root, width = 27, height = 7, text = "Calculator", fg = "black", bg = "skyblue", font = fontsin)
    label2.place(x = -290, y = -190)
    label3 = Label(root, width = 15, height = 2, text = "Символьные", fg = "black", bg = "skyblue", font = fontsan)
    label3.place(x = 320, y = 20)
    label4 = Label(root, width = 15, height = 2, text = "вычисления:", fg = "black", bg = "skyblue", font = fontsan)
    label4.place(x = 321, y = 40)
    label5 = Label(root, width = 4, height = 2, text = "OFF", fg = "black", bg = "skyblue", font = fontson)
    label5.place(x = 425, y = 15)
    
    label = Label(root, width = 65, height = 26, bg = "grey")
    label.place(x = 20, y = 90)
    expression_field = Entry(root, width = 20, textvariable = equation, font =("Verdana",25), bg = "white", state="disabled", disabledforeground="black")
    expression_field.place(x = 35, y = 105)
    
    button1 = Button(root, text = "1", fg = "white", border = 6, bg = 'red', command = lambda: press(1), font = fontson)
    button1.place(x = 30, y = 200);
    
    button2 = Button(root, text = "2", fg = "white", border = 6, bg = 'red', command = lambda: press(2), font = fontson)
    button2.place(x = 90, y = 200);
    
    button3 = Button(root, text = "3", fg = "white", border = 6, bg = 'red', command = lambda: press(3), font = fontson)
    button3.place(x = 150, y = 200);
    
    button4 = Button(root, text = "4", fg = "white", border = 6, bg = 'red', command = lambda: press(4), font = fontson)
    button4.place(x = 30, y = 270);
    
    button5 = Button(root, text = "5", fg = "white", border = 6, bg = 'red', command = lambda: press(5), font = fontson)
    button5.place(x = 90, y = 270);
    
    button6 = Button(root, text = "6", fg = "white", border = 6, bg = 'red', command = lambda: press(6), font = fontson)
    button6.place(x = 150, y = 270);
    
    button7 = Button(root, text = "7", fg = "white", border = 6, bg = 'red', command = lambda: press(7), font = fontson)
    button7.place(x = 30, y = 340);
    
    button8 = Button(root, text = "8", fg = "white", border = 6, bg = 'red', command = lambda: press(8), font = fontson)
    button8.place(x = 90, y = 340);
    
    button9 = Button(root, text = "9", fg = "white", border = 6, bg = 'red', command = lambda: press(9), font = fontson)
    button9.place(x = 150, y = 340);
    
    button0 = Button(root, text = "0", fg = "white", border = 6, bg = 'red', command = lambda: press(0), font = fontson)
    button0.place(x = 30, y = 410);
    
    buttonEq = Button(root, text = "=", fg = "white", width = 2, border = 5, bg = 'red', command = lambda: equalPress(), font = fontson)
    buttonEq.place(x = 150, y = 410);
    
    buttonDot = Button(root, text = ".", fg = "white", width = 2, border = 5, bg = 'red', command = lambda: press("."), font = ("Verdana", 18))
    buttonDot.place(x = 90, y = 410);
    
    buttonSum = Button(root, text = "+", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("+"), font = fontson)
    buttonSum.place(x = 300, y = 200);
    
    buttonSubstr = Button(root, text = "-", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("-"), font = fontson)
    buttonSubstr.place(x = 300, y = 270);
    
    buttonMulti = Button(root, text = "*", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("*"), font = fontson)
    buttonMulti.place(x = 300, y = 340);
    
    buttonDivi = Button(root, text = "/", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("/"), font = fontson)
    buttonDivi.place(x = 300, y = 410);
    
    clearB = Button(root, text = "Clear", fg = "white", width = 4, border = 8, bg = 'green', command = lambda: clear(), font = ("Verdana", 15))
    clearB.place(x = 215, y = 412);
    
    backB = Button(root, text = "Back", fg = "white", width = 4, border = 8, bg = 'green', command = lambda: back(), font = ("Verdana", 15))
    backB.place(x = 215, y = 342);
    
    solverB = Button(root, text = "Solve", fg = "white", width = 4, border = 8, bg = 'green', command = lambda: solveEq(), font = ("Verdana", 15))
    solverB.place(x = 215, y = 272);
    
    onOffB = Button(root, text = "On/Off sym", fg = "white", width = 10, border = 3, bg = 'green', command = lambda: changeStatus(), font = ("Verdana", 10))
    onOffB.place(x = 373, y = 163);
    
    buttonX = Button(root, text = "X", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("x"), font = fontson)
    buttonX.place(x = 360, y = 200);
    
    buttonY = Button(root, text = "Y", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("y"), font = fontson)
    buttonY.place(x = 420, y = 200);
    
    buttonLeftBr = Button(root, text = "(", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("("), font = fontson)
    buttonLeftBr.place(x = 360, y = 270);
    
    buttonRightBr = Button(root, text = ")", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press(")"), font = fontson)
    buttonRightBr.place(x = 420, y = 270);
    
    buttonPow = Button(root, text = "**", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("**"), font = fontson)
    buttonPow.place(x = 360, y = 340);
    
    buttonPi = Button(root, text = "pi", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("pi"), font = fontson)
    buttonPi.place(x = 420, y = 340);
    
    buttonSin = Button(root, text = "sin", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("sin("), font = fontson)
    buttonSin.place(x = 360, y = 410);
    
    buttonCos = Button(root, text = "cos", fg = "white", width = 2, border = 8, bg = 'blue', command = lambda: press("cos("), font = fontson)
    buttonCos.place(x = 420, y = 410);
    
frame1 = Frame(root); frame1.place(x=500, y=0, width=500, height=500)
figure = plt.Figure(figsize=(15,15), facecolor='yellow')
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=0,y=0,width=500,height=500)
ax = figure.add_subplot(1, 1, 1)
root.mainloop()