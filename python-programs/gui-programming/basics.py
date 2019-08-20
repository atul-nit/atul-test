from tkinter import *

def sub_form():
    print("subform pressed")
    first_name = f_field.get()
    last_name = l_field.get()
    full_name = first_name + " " + last_name
    print(full_name)
    label_full = Label(gui, text = "Your full name is "+full_name)
    label_full.grid(row=4, column=1)

gui = Tk()

gui.configure(background="light green")
# # #
gui.title("Simple Form")
gui.geometry("250x250")
# #
labelf = Label( gui, text = "First name")
f_field = Entry(gui)
labelf.grid(row=1, column=1)
f_field.grid(row=1, column=2)
# # #
labell = Label( gui, text = "last name")
l_field = Entry(gui)

labell.grid(row=2, column=1)
l_field.grid(row=2, column=2)
# # #
# # #
# # #
sub = Button(gui, text="submit", bg="blue", command=lambda: sub_form() )
sub.configure(background="red", fg="blue")
sub.grid(row=3, column=1)

gui.mainloop()