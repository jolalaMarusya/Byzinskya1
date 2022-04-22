from tkinter import *
from random import randint

root = Tk()
root.geometry("550x350")
root.title("Чёт нечёт")

var=IntVar()
var.set(0)

b= " "

def abc ():
    a = randint(0,1000)
    if var.get() == 1 and a%2==0:
        lbl = Label (root,text="Верно")
        lbl.pack()
    elif var.get() == 1 and a % 2 !=0:
        lbl=Label (root,text="Неверно")
        lbl.pack()
    elif var.get() == 2 and a%2==0:
        lbl=Label (root,text="Неверно")
        lbl.pack()
    elif var.get()==2 and a % 2 != 0:
        lbl=Label (root,text="Верно")
        lbl.pack()

lab1=Label(root,text="Чёт или нечёт?")
lab1.pack()
lab2=Label(root,text="Компьютер загадал число")
lab2.pack()
lab3=Label(root,text="Какое оно - чётное или нечётное?")
lab3.pack()

r1=Radiobutton(root,text="Чётное",value=1,variable=var)
r2=Radiobutton(root,text="Нечётное",value=2,variable=var)
r1.pack()
r2.pack()

btn=Button(root,text="Проверить ответ",command=abc)
btn.pack()

root.mainloop()
