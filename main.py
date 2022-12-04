# simple calculator app - gui using tkinter

# get everything from tkinter import
from tkinter import *

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
    button0 = Button(window, text="0", padx=33, pady=22, font=("Arial", 15))

    button1 = Button(window, text="1", padx=33, pady=22, font=("Arial", 15))
    button2 = Button(window, text="2", padx=33, pady=22, font=("Arial", 15))
    button3 = Button(window, text="3", padx=33, pady=22, font=("Arial", 15))

    button4 = Button(window, text="4", padx=33, pady=22, font=("Arial", 15))
    button5 = Button(window, text="5", padx=33, pady=22, font=("Arial", 15))
    button6 = Button(window, text="6", padx=33, pady=22, font=("Arial", 15))

    button7 = Button(window, text="7", padx=33, pady=22, font=("Arial", 15))
    button8 = Button(window, text="8", padx=33, pady=22, font=("Arial", 15))
    button9 = Button(window, text="9", padx=33, pady=22, font=("Arial", 15))

    button_decimal = Button(window, text=".", padx=35, pady=22, font=("Arial", 15))
    button_clear = Button(window, text="A/C", padx=68, pady=22, font=("Arial", 15))
    button_equals = Button(window, text="=", padx=79, pady=22, font=("Arial", 15))

    button_add = Button(window, text="+", padx=32, pady=22, font=("Arial", 15))
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
