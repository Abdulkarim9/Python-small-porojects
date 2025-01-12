from tkinter import *


root = Tk()

root.title("Calculator")

entry = Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def number(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


def clear():
    entry.delete(0, END)


def delete():
    entry.delete(len(entry.get()) - 1, END)


def addition():
    global f_num
    global operation
    operation = "addition"
    first_number = entry.get()
    f_num = int(first_number)
    entry.delete(0, END)


def subtraction():
    global f_num
    global operation
    operation = "subtraction"
    first_number = entry.get()
    f_num = int(first_number)
    entry.delete(0, END)


def multiplication():
    global f_num
    global operation
    operation = "multiplication"
    first_number = entry.get()
    f_num = int(first_number)
    entry.delete(0, END)


def division():
    global f_num
    global operation
    operation = "division"
    first_number = entry.get()
    f_num = int(first_number)
    entry.delete(0, END)


def module():
    global f_num
    global operation
    operation = "module"
    first_number = entry.get()
    f_num = int(first_number)
    entry.delete(0, END)


def equal():
    global operation
    second_number = entry.get()
    entry.delete(0, END)
    if operation == "addition":
        entry.insert(0, f_num + int(second_number))
    elif operation == "subtraction":
        entry.insert(0, f_num - int(second_number))
    elif operation == "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif operation == "division":
        entry.insert(0, f_num / int(second_number))
    elif operation == "module":
        entry.insert(0, f_num % int(second_number))


button_clear = Button(root, text="Clear", bg="gray", fg="white", font=('Arial', 10), padx=23, pady=20, command=clear)
button_delete = Button(root, text="x", bg="gray", fg="white", font=('Arial', 10), padx=33, pady=20, command=delete)
button_percent = Button(root, text="%", bg="gray", fg="white", font=('Arial', 10), padx=32, pady=20, command=module)
button_division = Button(root, text="/", bg="orange", font=('Arial', 10), padx=35, pady=20, command=division)

button1 = Button(root, text="7", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(7))
button2 = Button(root, text="8", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(8))
button3 = Button(root, text="9", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(9))
button_multiplication = Button(root, text="*", bg="orange", font=('Arial', 10), padx=35, pady=20, command=multiplication)

button4 = Button(root, text="4", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(4))
button5 = Button(root, text="5", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(5))
button6 = Button(root, text="6", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(6))
button_subtraction = Button(root, text="-", bg="orange", font=('Arial', 10), padx=35, pady=20, command=subtraction)

button7 = Button(root, text="1", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(1))
button8 = Button(root, text="2", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(2))
button9 = Button(root, text="3", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(3))
button_addition = Button(root, text="+", bg="orange", font=('Arial', 10), padx=35, pady=20, command=addition)

button10 = Button(root, text="0", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command=lambda: number(0))
button11 = Button(root, text=".", bg="#333", fg="white", font=('Arial', 10), padx=35, pady=20, command="")
button_equal = Button(root, text="=",  bg="orange", font=('Arial', 10), padx=35, pady=20, command=equal)


button_clear.grid(row=1, column=0)
button_delete.grid(row=1, column=1)
button_percent.grid(row=1, column=2)
button_division.grid(row=1, column=3)

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
button_addition.grid(row=4, column=3)

button10.grid(row=5, column=0, columnspan=2, sticky=W+E)
button11.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()
