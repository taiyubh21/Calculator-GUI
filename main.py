# simple calculator app - gui using tkinter

# get everything from tkinter import
from tkinter import *


# function created for return value of number to textbox
def value_return(number):
    # insert value into text box
    # allows value not to be overwritten so can write big number using multiple number buttons
    # adds numbers to the end
    display.insert(END, number)


# separate function created to add decimal to create float
def decimal_insert(decimal):
    # adds decimal to numbers in the textbox display making it a float
    display.insert(END, decimal)
    # disable button after pressed so no more than one decimal is added
    button_decimal.configure(state=DISABLED)


# function created to clear textbox using A/C button
def clear_value():
    # deletes whatever is in the textbox
    display.delete(0, END)
    # return decimal button back to its normal state so can be pressed again and doesn't remain disabled
    button_decimal.configure(state=NORMAL)


# function created for addition operator
def addition():
    # save the first number entered as a float
    first_number = float(display.get())
    # use of global variable to be used in equals function
    global first_num
    # save the number into the global variable
    first_num = first_number
    # deletes whatever is in the textbox so user can enter second number
    display.delete(0, END)
    # return decimal button back to its normal state so can be pressed again and doesn't remain disabled
    button_decimal.configure(state=NORMAL)


# function created for equals operator
def equals():
    # save the second number entered as a float
    second_num = float(display.get())
    # deletes whatever is in the textbox so result can be output
    display.delete(0, END)
    # do addition operation on the numbers and insert into textbox
    result = first_num + second_num
    display.insert(0, str(result))


if __name__ == "__main__":
    # create gui
    window = Tk()

    # title of application
    window.title("Calculator Application")

    # creating display box
    display = Entry(window, width=30, borderwidth=5, font=("Arial", 15))
    # putting display box on screen using textbox
    display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # creating buttons
    # use value_return function and pass number through in the specific buttons
    button0 = Button(window, text="0", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(0))

    button1 = Button(window, text="1", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(1))
    button2 = Button(window, text="2", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(2))
    button3 = Button(window, text="3", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(3))

    button4 = Button(window, text="4", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(4))
    button5 = Button(window, text="5", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(5))
    button6 = Button(window, text="6", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(6))

    button7 = Button(window, text="7", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(7))
    button8 = Button(window, text="8", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(8))
    button9 = Button(window, text="9", padx=33, pady=22, font=("Arial", 15), command=lambda: value_return(9))

    # using decimal_insert function and passing '.' through
    button_decimal = Button(window, text=".", padx=35, pady=22, font=("Arial", 15), command=lambda: decimal_insert('.'))

    # button_clear calls clear_value function
    button_clear = Button(window, text="A/C", padx=68, pady=22, font=("Arial", 15), command=clear_value)
    # button_clear calls equals function
    button_equals = Button(window, text="=", padx=79, pady=22, font=("Arial", 15), command=equals)

    # button_clear calls addition function
    button_add = Button(window, text="+", padx=32, pady=22, font=("Arial", 15), command=addition)
    button_sub = Button(window, text="-", padx=34, pady=22, font=("Arial", 15))
    button_mul = Button(window, text="x", padx=33, pady=22, font=("Arial", 15))
    button_div = Button(window, text="÷", padx=32, pady=22, font=("Arial", 15))

    # displaying buttons appropriately
    button_clear.grid(row=1, column=0, columnspan=2)
    button_decimal.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)

    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)

    button0.grid(row=5, column=0)
    button_equals.grid(row=5, column=1, columnspan=2)

    button_add.grid(row=2, column=4)
    button_sub.grid(row=3, column=4)
    button_mul.grid(row=4, column=4)
    button_div.grid(row=5, column=4)

    # run gui
    window.mainloop()
