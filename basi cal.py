from tkinter import *

ra = Tk()
ra.title("Bsic Caliculator:")
e = Entry(width=56, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=25)


def gea(n):
    e.insert(END, n)


def gead():
    x = e.get()
    global y
    global math
    math = "add"
    y = int(x)
    e.delete(0, END)


def gesu():
    x = e.get()
    global y
    global math
    math = "su"
    y = int(x)
    e.delete(0, END)


def gemu():
    x = e.get()
    global y
    global math
    math = "mu"
    y = int(x)
    e.delete(0, END)


def gedi():
    x = e.get()
    global y
    global math
    math = "di"
    y = int(x)
    e.delete(0, END)


def geac():
    e.delete(0, END)


def geaq():
    z = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, str(y + int(z)))
    elif math == "su":
        e.insert(0, str(y - int(z)))
    elif math == "mu":
        e.insert(0, str(y * int(z)))
    else:
        e.insert(0, str(y / int(z)))


b9 = Button(ra, text="9", padx=49, pady=25, command=lambda: gea(9)).grid(row=1, column=2)
b8 = Button(ra, text="8", padx=49, pady=25, command=lambda: gea(8)).grid(row=1, column=1)
b7 = Button(ra, text="7", padx=49, pady=25, command=lambda: gea(7)).grid(row=1, column=0)
b6 = Button(ra, text="6", padx=49, pady=25, command=lambda: gea(6)).grid(row=2, column=2)
b5 = Button(ra, text="5", padx=49, pady=25, command=lambda: gea(5)).grid(row=2, column=1)
b4 = Button(ra, text="4", padx=49, pady=25, command=lambda: gea(4)).grid(row=2, column=0)
b3 = Button(ra, text="3", padx=49, pady=25, command=lambda: gea(3)).grid(row=3, column=2)
b2 = Button(ra, text="2", padx=49, pady=25, command=lambda: gea(2)).grid(row=3, column=1)
b1 = Button(ra, text="1", padx=49, pady=25, command=lambda: gea(1)).grid(row=3, column=0)
b0 = Button(ra, text="0", padx=49, pady=25, command=lambda: gea(0)).grid(row=4, column=0)
b_add = Button(ra, text="+", padx=49, pady=25, command=gead).grid(row=4, column=1)
b_minu = Button(ra, text="-", padx=49, pady=25, command=gesu).grid(row=4, column=2)
b_multi = Button(ra, text="*", padx=49, pady=25, command=gemu).grid(row=5, column=2)
b_divi = Button(ra, text="/", padx=49, pady=25, command=gedi).grid(row=5, column=0)
b_eq = Button(ra, text="=", padx=49, pady=25, command=geaq).grid(row=5, column=1)
b_clear = Button(ra, text="Clear", padx=170, pady=25, command=geac).grid(row=6, column=0, columnspan=3)

ra.mainloop()
