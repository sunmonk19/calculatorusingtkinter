from tkinter import *

window =Tk()
window.title("calculator")

# frame for the buttons
frame = Frame(window, width=500, height = 500 , bg="black")
frame.pack(side=TOP )

#entry box in the frame
entybox = Entry(frame, width = 40)
entybox.grid(row=0, column=2)

def click(number):
    en = entybox.get()
    entybox.insert(END,number)



#buttons for calculator
#first row
button1 = Button(frame, text="1" , width=10, height=2 , command=lambda:click(1))
button1.grid(row=1, column=1 , padx=10 , pady=0)

button1 = Button(frame, text="2" , width=10, height=2 , command=lambda:click(2))
button1.grid(row=1, column=2 , padx=10 , pady=20)

button1 = Button(frame, text="3" , width=10, height=2 , command=lambda:click(3))
button1.grid(row=1, column=3 , padx=10 , pady=20)

# second row

button1 = Button(frame, text="4" , width=10, height=2 , command=lambda:click(4))
button1.grid(row=2, column=1 , padx=10 , pady=20)

button1 = Button(frame, text="5" , width=10, height=2 , command=lambda:click(5))
button1.grid(row=2, column=2 , padx=10 , pady=20)

button1 = Button(frame, text="6" , width=10, height=2 , command=lambda:click(6))
button1.grid(row=2, column=3 , padx=10 , pady=20)

# third row

button1 = Button(frame, text="7" , width=10, height=2 , command=lambda:click(7))
button1.grid(row=3, column=1 , padx=10 , pady=20)

button1 = Button(frame, text="8" , width=10, height=2 , command=lambda:click(8))
button1.grid(row=3, column=2 , padx=10 , pady=20)

button1 = Button(frame, text="9" , width=10, height=2 , command=lambda:click(9))
button1.grid(row=3, column=3 , padx=10 , pady=20)



window.mainloop()
