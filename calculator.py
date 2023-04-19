from tkinter import *
 
def add():
    a = float(first_entry.get())
    b = float(second_entry.get())
    c = a + b
    result_label2.config(text=str(c))

def subtract():
    a = float(first_entry.get())
    b = float(second_entry.get())
    c = a - b
    result_label2.config(text=str(c))

def multipy():
    a = float(first_entry.get())
    b = float(second_entry.get())
    c = a * b
    result_label2.config(text=str(c))

def divide():
    a = float(first_entry.get())
    b = float(second_entry.get())
    c = a / b
    c = round(c,4)
    result_label2.config(text=str(c))


window = Tk()
window.title("Shams calculator!")
window.geometry("400x400")

entry_frame1 = Frame(window,bg="gray")
entry_frame1.pack(expand=True,fill = "both")
entry_frame2 = Frame(window,bg="gray")
entry_frame2.pack(expand=True,fill = "both")
cal_frame = Frame(window,bg="gray")
cal_frame.pack(expand=True,fill = "both")
result_frame = Frame(window,bg="lavender")
result_frame.pack(expand=True,fill = "both")

Label(entry_frame1,text="Calculate!",bg="gray",foreground="lime",font=("",17)).place(x=155,y=3)
first_entry_label = Label(entry_frame1,text="First number:",bg="gray",font=("",15))
first_entry_label.place(x=20,y=48)
first_entry = Entry(entry_frame1)
first_entry.place(x=170,y=52)

first_entry_labe2 = Label(entry_frame2,text="Second number:",bg="gray",font=("",15))
first_entry_labe2.place(x=20,y=23)
second_entry = Entry(entry_frame2)
second_entry.place(x=170,y=27)

add_button = Button(cal_frame,text="Add(+)",bg="yellow",font=("",12),command=add)
add_button.place(x= 14,y=20)
subtract_button =Button(cal_frame,text="Subtract(-)",bg="yellow",font=("",12),command=subtract)
subtract_button.place(x= 100,y=20)
multiply_button = Button(cal_frame,text="Multipy(x)",bg="yellow",font=("",12),command=multipy)
multiply_button.place(x= 210,y=20)
divide_button = Button(cal_frame,text="Divide(/)",bg="yellow",font=("",12),command=divide)
divide_button.place(x=310,y=20)


result_label = Label(result_frame,text="Result:",bg="lavender",foreground="blue",font=("",15))
result_label.place(x=40,y=30)
result_label2 = Label(result_frame,text="",bg="lavender",foreground="black",font=("",14))
result_label2.place(x=150,y=30)





window.mainloop()