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
    entybox.delete(0,END)
    entybox.insert(0 , str(en) + str(number))



#buttons for calculator
#first row
button1 = Button(frame, text="1" , width=10, height=2 , command=lambda:click(1))
button1.grid(row=1, column=1 , padx=10 , pady=0)

button2 = Button(frame, text="2" , width=10, height=2 , command=lambda:click(2))
button2.grid(row=1, column=2 , padx=10 , pady=20)

button3 = Button(frame, text="3" , width=10, height=2 , command=lambda:click(3))
button3.grid(row=1, column=3 , padx=10 , pady=20)

# second row

button4 = Button(frame, text="4" , width=10, height=2 , command=lambda:click(4))
button4.grid(row=2, column=1 , padx=10 , pady=20)

button5 = Button(frame, text="5" , width=10, height=2 , command=lambda:click(5))
button5.grid(row=2, column=2 , padx=10 , pady=20)

button6 = Button(frame, text="6" , width=10, height=2 , command=lambda:click(6))
button6.grid(row=2, column=3 , padx=10 , pady=20)

# third row

button7= Button(frame, text="7" , width=10, height=2 , command=lambda:click(7))
button7.grid(row=3, column=1 , padx=10 , pady=20)

button8 = Button(frame, text="8" , width=10, height=2 , command=lambda:click(8))
button8.grid(row=3, column=2 , padx=10 , pady=20)

button9 = Button(frame, text="9" , width=10, height=2 , command=lambda:click(9))
button9.grid(row=3, column=3 , padx=10 , pady=20)

button0 = Button(frame, text="0" , width=10 , height=2, command =lambda:click(0))
button0.grid(row=4 , column=1, padx=10 ,pady=20)

#operator buttons 

def add():
    number1 = entybox.get()
    global i
    global math
    math = "addition"
    i =int(number1)
    entybox.delete(0,END)
 
buttonadd = Button(frame, text="+", width=10, height=2 ,command= add)
buttonadd.grid(row=5 , column=1, padx=10 ,pady=20)

def sub():
    number1 = entybox.get()
    global i
    global math
    math = "subtraction"
    i =int(number1)
    entybox.delete(0,END)

buttonsub = Button(frame, text="-", width=10, height=2 ,command=sub)
buttonsub.grid(row=5 , column=2, padx=10 ,pady=20)

def mul():
    number1 = entybox.get()
    global i
    global math
    math = "multiply"
    i =int(number1)
    entybox.delete(0,END)

buttonmul = Button(frame, text="*", width=10, height=2 ,command=mul)
buttonmul.grid(row=4 , column=3, padx=10 ,pady=20)

def div():
    number1 = entybox.get()
    global i
    global math
    math = "divsion"
    i =int(number1)
    entybox.delete(0,END)

buttondiv = Button(frame, text="/", width=10, height=2 ,command=div)
buttondiv.grid(row=4 , column=2, padx=10 ,pady=20)

#ok and clear buttons

def ok():
    number2 = entybox.get()
    entybox.delete(0,END)
    if math == "addition":
        entybox.insert(0, i + int(number2))
    elif math == "subtraction":
        entybox.insert(0, i - int(number2))
    elif math == "multiply":
        entybox.insert(0, i * int(number2))
    elif math == "divsion":
        entybox.insert(0, i / int(number2))
    

buttonok = Button(frame, text="ok", width=10, height=2 ,command= ok)
buttonok.grid(row=5 , column=3, padx=10 ,pady=20)

def clear():
    entybox.delete(0,END)

buttonclear = Button(frame, text="clear", width=10, height=2 ,command= clear)
buttonclear.grid(row=6 , column=1, padx=10 ,pady=20)



window.mainloop()
