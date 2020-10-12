from tkinter import *


nodada = Tk()
nodada.title("GUI TASK")
nodada.geometry("800x400")
nodada.configure(background="yellow")


def addition():
    num1=int(first_entry.get())
    num2 = int(second_entry.get())
    answer = num1+num2
    answer_entry.configure(text=answer)

def clear():
    first_entry.delete(0,END)
    second_entry.delete(0,END)
    answer_entry.delete(0,END)


firstLabel = Label(nodada, text="First_Number", relief="solid", font="arial 18 bold")
first_entry = Entry(nodada, width=20)

firstLabel.grid(row=0, column=0)
first_entry.grid(row=0, column=1)

secondLabel = Label(nodada, text="Second_Number", relief="solid", font="arial 18 bold")
second_entry = Entry(nodada, width=20)

secondLabel.grid(row=1, column=0)
second_entry.grid(row=1, column=1)

answerLabel = Label(nodada, text="Result", relief="solid", font="arial 18 bold")
answer_entry= Label(nodada, width=30)

answerLabel.grid(row=2, column=0)
answer_entry.grid(row=2, column=1)



one_button = Button(nodada, text="Add", bg="red", command=addition)
one_button.grid(row=3, column=2)

clear_button = Button(nodada, text="Clear", bg="red", command=clear)
clear_button.grid(row=3,column=3)


nodada.mainloop()