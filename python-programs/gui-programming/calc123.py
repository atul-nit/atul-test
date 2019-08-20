from tkinter import *
#
def Sign_up_for_SDLC():
#     print("subform pressed")
    first_name = f_field.get()
    last_name = l_field.get()
    Email_address= e_field.get()
    Phone_number=p_field.get()

# print("first_name:",first_name)
    f=first_name
    print(f)
    l=last_name
    print(l)
    e=Email_address
    print(e)
    p=Phone_number
    print(p)

    l1=[f,l,e,p]
    print(l1)
gui = Tk()

gui.configure(background="light green")

# #
gui.title("Sign up for SDLC")
gui.geometry("250x250")
#
labelf = Label( gui, text = "First name")
f_field = Entry(gui)
labelf.grid(row=1, column=1)
f_field.grid(row=1, column=2)
# #
labell = Label( gui, text = "last name")
l_field = Entry(gui)
labell.grid(row=2, column=1)
l_field.grid(row=2, column=2)

labele = Label( gui, text = "Email address")
e_field = Entry(gui)
labele.grid(row=3, column=1)
e_field.grid(row=3, column=2)

labelp = Label( gui, text = "Phone number")
p_field = Entry(gui)
labelp.grid(row=4, column=1)
p_field.grid(row=4, column=2)
# #
# #
# #
sub = Button(gui, text="submit", bg="blue", command=lambda: Sign_up_for_SDLC() )
sub.grid(row=5, column=1)

gui.mainloop()