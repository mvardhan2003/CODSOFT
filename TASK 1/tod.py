from tkinter import *

ro=Tk()
ro.geometry("400x400")
ro['bg']="orange"
m1=Label(ro,text="TO-DO LIST",bg="Gray",fg="Red",font=('time-new-roman',16)).grid(row=0,column=0)

g1=Entry()
# g1.insert(0,"Enter the task:")
g1.grid(row=1,column=0)
def myc():
    m2=Label(ro,text=g1.get()).grid(row=3,column=0)    

mb1=Button(ro,text="submit",padx=30,command=myc).grid(row=2,column=0)

ro.mainloop()