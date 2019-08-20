from tkinter import *

def sub_form():
    print("subform pressed")
    P = int(f_field.get())
    R = int(l_field.get())
    n=int(k_field.get())
    print(P,R,n)
    compound_interest=round(P*(1+(R/100))**n, 2)
    #
    print(compound_interest)
    label_full = Label(gui, text = "Your amount after compound interest is "+str(compound_interest))
    label_full.grid(row=5, column=1)

gui = Tk()

gui.configure(background="light green")
#
gui.title("Simple Form")
gui.geometry("250x250")

labelf = Label( gui, text = "Principal")
f_field = Entry(gui)
labelf.grid(row=1, column=1)
f_field.grid(row=1, column=2)

labell = Label( gui, text = "Rate ")
l_field = Entry(gui)
labell.grid(row=2, column=1)
l_field.grid(row=2, column=2)

labelk = Label( gui, text = "Time")
k_field = Entry(gui)
labelk.grid(row=3, column=1)
k_field.grid(row=3, column=2)
#


sub = Button(gui, text="Calculate", bg="blue", command=lambda: sub_form() )
sub.grid(row=4, column=1)

gui.mainloop()