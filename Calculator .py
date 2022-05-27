# *********************************************
# *********************************************
# *********************************************
# *********************************************
# **************Name:Omar Shaheen**************
# **************SW:Calculator******************
# **************Date:25 Dec 2021***************
# **************Version:1.0v*******************
# *********************************************

# import thinter as tk from python
import tkinter as tk
# make a string to store calculation into string
calculcation = ""

# make a function to add symbol to calculation and enter the parameters


def add_calculation(symbol):
    global calculcation
    # make concatenation between two string to write the equation
    calculcation = calculcation+str(symbol)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", calculcation)

# make a function to evaluate calculation and get the result


def evaluate_calculation():
    global calculcation
    # make a file to save parameters in the file
    myfile = open("Omar.txt", "a")
    myfile.write(calculcation)
    # Exception Handling for parameters
    try:
        calculcation = str(eval(calculcation))
        text_result.delete("1.0", "end")
        text_result.insert("1.0", calculcation)
        # save the result of calculation in the file
        myfile.write("=")
        myfile.write(calculcation)
        myfile.write("\n")
        # closing the file after the equation
        myfile.close()
    # make clear and write error if get a wrong equation
    except:
        clear()
        text_result.insert("1.0", "Error")

# make a function to clear a calculator


def clear():
    global calculcation
    calculcation = ""
    text_result.delete("1.0", "end")


# initlization for thinter
root = tk.Tk()
# to choose geometry of the calculator
root.geometry("315x315")
# to choose title for the calculator
root.title("CalCulator")
# to choose backgroud for the calculator
root.configure(bg="black")
# make screen to show the enitries and result to the user
text_result = tk.Text(root, height=2, width=16, font=("Arial", 26))
text_result.grid(columnspan=5)

# make button 1---------> number 1
Button1 = tk.Button(root, text='1', command=lambda: add_calculation(
    1), width=5, bg='red', fg='white', font=("Arial", 14))
Button1.grid(row=2, column=1)

# make button 2---------> number 2
Button2 = tk.Button(root, text='2', command=lambda: add_calculation(
    2), width=5, bg='red', fg='white', font=("Arial", 14))
Button2.grid(row=2, column=2)

# make button 3---------> number 3
Button3 = tk.Button(root, text='3', command=lambda: add_calculation(
    3), width=5, bg='red', fg='white', font=("Arial", 14))
Button3.grid(row=2, column=3)

# make button 4---------> number 4
Button4 = tk.Button(root, text='4', command=lambda: add_calculation(
    4), width=5, bg='red', fg='white', font=("Arial", 14))
Button4.grid(row=3, column=1)

# make button 5---------> number 5
Button5 = tk.Button(root, text='5', command=lambda: add_calculation(
    5), width=5, bg='red', fg='white', font=("Arial", 14))
Button5.grid(row=3, column=2)

# make button 6---------> number 6
Button6 = tk.Button(root, text='6', command=lambda: add_calculation(
    6), width=5, bg='red', fg='white', font=("Arial", 14))
Button6.grid(row=3, column=3)

# make button 7---------> number 7
Button7 = tk.Button(root, text='7', command=lambda: add_calculation(
    7), width=5, bg='red', fg='white', font=("Arial", 14))
Button7.grid(row=4, column=1)

# make button 8---------> number 8
Button8 = tk.Button(root, text='8', command=lambda: add_calculation(
    8), width=5, bg='red', fg='white', font=("Arial", 14))
Button8.grid(row=4, column=2)

# make button 9---------> number 9
Button9 = tk.Button(root, text='9', command=lambda: add_calculation(
    9), width=5, bg='red', fg='white', font=("Arial", 14))
Button9.grid(row=4, column=3)

# make button 0---------> number 0
Button0 = tk.Button(root, text='0', command=lambda: add_calculation(
    0), width=5, bg='red', fg='white', font=("Arial", 14))
Button0.grid(row=5, column=1)

# make button '+'---------> operation plus
Button_plus = tk.Button(root, text='+', command=lambda: add_calculation(
    '+'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_plus.grid(row=2, column=4)

# make button '-'---------> operation subtraction
Button_sub = tk.Button(root, text='-', command=lambda: add_calculation(
    '-'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_sub.grid(row=3, column=4)

# make button '*'---------> operation multplication
Button_mult = tk.Button(root, text='*', command=lambda: add_calculation(
    '*'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_mult.grid(row=4, column=4)

# make button '/'---------> operation Divsion
Button_Div = tk.Button(root, text='/', command=lambda: add_calculation(
    '/'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_Div.grid(row=5, column=4)

# make button '%'---------> operation modulus
Button_mod = tk.Button(root, text='%', command=lambda: add_calculation(
    '%'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_mod.grid(row=6, column=4)

# make button '**'---------> operation power
Button_pow = tk.Button(root, text='pow', command=lambda: add_calculation(
    '**'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_pow.grid(row=6, column=3)

# make button '**0.5'---------> operation square root
Button_sqrt = tk.Button(root, text='sqrt', command=lambda: add_calculation(
    '**0.5'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_sqrt.grid(row=5, column=3)

# make button '.'---------> Decimal point
Button_Decimal = tk.Button(root, text='.', command=lambda: add_calculation(
    '.'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_Decimal.grid(row=5, column=2)

# make button '('---------> open bracket
Button_Open = tk.Button(root, text='(', command=lambda: add_calculation(
    '('), width=5, bg='red', fg='white', font=("Arial", 14))
Button_Open.grid(row=6, column=1)

# make button ')'---------> close bracket
Button_close = tk.Button(root, text=')', command=lambda: add_calculation(
    ')'), width=5, bg='red', fg='white', font=("Arial", 14))
Button_close.grid(row=6, column=2)

# make button '='---------> equal
Button_equal = tk.Button(root, text='=', command=evaluate_calculation,
                         width=12, bg='red', fg='white', font=("Arial", 14),)
Button_equal.grid(row=7, column=1, columnspan=2)

# make button 'C'---------> clear operation
Button_clear = tk.Button(root, text='C', command=clear,
                         width=12, bg='red', fg='white', font=("Arial", 14),)
Button_clear.grid(row=7, column=3, columnspan=2)


root.mainloop()
