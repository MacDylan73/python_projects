# importing tkinter module
from tkinter import *

# initializing variables
global num1
num1 = 0
global num2
num2 = 0
global operation
operation = ""
global solution
solution = 0
global operationlast
operationlast = True

# creating window
wn = Tk()
wn.title('Basic Calculator by Dylan Folscroft')
wn.geometry('300x450')
wn.configure(background='black')

# configuring rows to allow for scalability
Grid.rowconfigure(wn, 1, weight=2)
Grid.rowconfigure(wn, 2, weight=1)
Grid.rowconfigure(wn, 3, weight=1)
Grid.rowconfigure(wn, 4, weight=1)
Grid.rowconfigure(wn, 5, weight=1)
Grid.rowconfigure(wn, 6, weight=1)

Grid.columnconfigure(wn, 1, weight=1)
Grid.columnconfigure(wn, 2, weight=1)
Grid.columnconfigure(wn, 3, weight=1)
Grid.columnconfigure(wn, 4, weight=1)


# creating function for button press
# solution function


# clear button
def clear():
    global operationlast
    operationlast = True
    entry.delete(0, END)
    entry.insert(0, '0')


# number buttons
def one():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '1')
    else:
        entry.insert(len(entry.get()), '1')
    operationlast = False


def two():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '2')
    else:
        entry.insert(len(entry.get()), '2')
    operationlast = False


def three():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '3')
    else:
        entry.insert(len(entry.get()), '3')
    operationlast = False


def four():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '4')
    else:
        entry.insert(len(entry.get()), '4')
    operationlast = False


def five():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '5')
    else:
        entry.insert(len(entry.get()), '5')
    operationlast = False


def six():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '6')
    else:
        entry.insert(len(entry.get()), '6')
    operationlast = False


def seven():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '7')
    else:
        entry.insert(len(entry.get()), '7')
    operationlast = False


def eight():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '8')
    else:
        entry.insert(len(entry.get()), '8')
    operationlast = False


def nine():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '9')
    else:
        entry.insert(len(entry.get()), '9')
    operationlast = False


def zero():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '0')
    else:
        entry.insert(len(entry.get()), '0')
    operationlast = False


def decimal():
    global operationlast
    if operationlast is True:
        entry.delete(0, END)
        entry.insert(len(entry.get()), '.')
    else:
        entry.insert(len(entry.get()), '.')
    operationlast = False


# operation buttons
def addition():
    global num1
    global operation
    num1 = float(entry.get())
    operation = "+"
    entry.delete(0, END)
    entry.insert(0, "+")
    global operationlast
    operationlast = True


def subtraction():
    global num1
    global operation
    num1 = float(entry.get())
    operation = "-"
    entry.delete(0, END)
    entry.insert(0, "-")
    global operationlast
    operationlast = True


def multiplication():
    global num1
    global operation
    num1 = float(entry.get())
    operation = "*"
    entry.delete(0, END)
    entry.insert(0, "*")
    global operationlast
    operationlast = True


def division():
    global num1
    global operation
    num1 = float(entry.get())
    operation = "/"
    entry.delete(0, END)
    entry.insert(0, "/")
    global operationlast
    operationlast = True


# equals
def equals():
    global num2
    num2 = float(entry.get())
    entry.delete(0, END)
    global solution
    global operation
    if operation == "+":
        solution = num1 + num2
    elif operation == "-":
        solution = num1 - num2
    elif operation == "*":
        solution = num1 * num2
    elif operation == "/":
        solution = num1 / num2
    elif operation == "":
        solution = entry.get()
    operation = ''
    entry.insert(0, str(solution))
    global operationlast
    operationlast = False


# creating widgets for the calculator
entry = Entry(wn, borderwidth=3, bg='white', fg='black', justify='right', font=('Anton', 18))
entry.insert(0, '0')
clearbutton = Button(wn, text='C', font=('Anton', 12), padx=104.5, pady=10, bg='black', fg='white', command=clear)
divisionbutton = Button(wn, text='/', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=division)
sevenbutton = Button(wn, text='7', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=seven)
eightbutton = Button(wn, text='8', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=eight)
ninebutton = Button(wn, text='9', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=nine)
multlipicationbutton = Button(wn, font=('Anton', 12), text='*', padx=30, pady=10, bg='black', fg='white',
                              command=multiplication)
fourbutton = Button(wn, text='4', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=four)
fivebutton = Button(wn, text='5', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=five)
sixbutton = Button(wn, text='6', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=six)
subtractionbutton = Button(wn, text='-', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white',
                           command=subtraction)
onebutton = Button(wn, text='1', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=one)
twobutton = Button(wn, text='2', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=two)
threebutton = Button(wn, text='3', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=three)
additionbutton = Button(wn, text='+', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=addition)
zerobutton = Button(wn, text='0', font=('Anton', 12), padx=67.5, pady=10, bg='black', fg='white', command=zero)
decimalbutton = Button(wn, text='.', font=('Anton', 12), padx=31, pady=10, bg='black', fg='white', command=decimal)
equalsbutton = Button(wn, text='=', font=('Anton', 12), padx=30, pady=10, bg='black', fg='white', command=equals)

# placing the widgets on the screen
entry.grid(row=1, column=1, columnspan=4, pady=3, padx=5, sticky='nsew')
clearbutton.grid(row=2, column=1, columnspan=3, sticky='nsew')
divisionbutton.grid(row=2, column=4, sticky='nsew')
sevenbutton.grid(row=3, column=1, sticky='nsew')
eightbutton.grid(row=3, column=2, sticky='nsew')
ninebutton.grid(row=3, column=3, sticky='nsew')
multlipicationbutton.grid(row=3, column=4, sticky='nsew')
fourbutton.grid(row=4, column=1, sticky='nsew')
fivebutton.grid(row=4, column=2, sticky='nsew')
sixbutton.grid(row=4, column=3, sticky='nsew')
subtractionbutton.grid(row=4, column=4, sticky='nsew')
onebutton.grid(row=5, column=1, sticky='nsew')
twobutton.grid(row=5, column=2, sticky='nsew')
threebutton.grid(row=5, column=3, sticky='nsew')
additionbutton.grid(row=5, column=4, sticky='nsew')
zerobutton.grid(row=6, column=1, columnspan=2, sticky='nsew')
decimalbutton.grid(row=6, column=3, sticky='nsew')
equalsbutton.grid(row=6, column=4, sticky='nsew')

# keeping window open
wn.mainloop()
