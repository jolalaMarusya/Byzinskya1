from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('1600x900')
root.title('Тест по программированию')

def canvas1():
    answer1 = entry1.get()
    if answer1 == "Картинка":
        messagebox.showinfo("Ответ","ВЕРНО")
    else:
        messagebox.showinfo("Ответ","Давай по новой, Миша")
def a():
    answer1 = entry1.get()
    if answer1 == "Картинка":
        messagebox.showinfo("Ответ на первый вопрос","ВЕРНО")
    else:
        messagebox.showinfo("Ответ на первый вопрос","Давай по новой, Миша")
    if var.get() == 3:
        messagebox.showinfo("Ответ на второй вопрос","ВЕРНО")
    else:
        messagebox.showinfo("Ответ на второй вопрос","Давай по новой, Миша")

    if var2.get() == 6:
        messagebox.showinfo("Ответ на третий вопрос","ВЕРНО")
    else:
        messagebox.showinfo("Ответ на третий вопрос","Давай по новой, Миша")
    if var3.get() == 10:
        messagebox.showinfo("Ответ на четвёртый вопрос","ВЕРНО")
    else:
        messagebox.showinfo("Ответ на четвёртый вопрос","Давай по новой, Миша")
    if var4.get() == 16:
        messagebox.showinfo("Ответ на пятый вопрос","ВЕРНО")
    else:
        messagebox.showinfo("Ответ на пятый вопрос","Давай по новой, Миша")    


answer1 = StringVar()
var = IntVar()
var.set(0)
var2 = IntVar()
var2.set(0)
var3 = IntVar()
var3.set(0)
var4 = IntVar()
var4.set(0)


lab1 = Label(root,text="                                      Вопрос 1. За что отвечает эта команда?(слово)")
lab1.pack()

canvas=Canvas(root,width=500,height=200)
canvas.place(relx=.2,rely=.0)

obj=PhotoImage(file="1.PNG")
id=canvas.create_image(50,50,anchor=NW,image=obj)

entry1=Entry(root,textvariable=answer1)
entry1.place(relx=.465,rely=.200)

lab2 = Label(root,text="Вопрос 2. Как создать окно с оповещением?")
lab2.place(relx=.415,rely=.225)

r11 = Radiobutton(root,text="createwindow",value=1,variable=var)
r11.place(relx=.415,rely=.245)
r12 = Radiobutton(root,text="massegebox",value=2,variable=var)
r12.place(relx=.415,rely=.265)
r13 = Radiobutton(root,text="messagebox",value=3,variable=var)
r13.place(relx=.415,rely=.285)
r14 = Radiobutton(root,text="createmessage",value=4,variable=var)
r14.place(relx=.415,rely=.305)

lab3 = Label(root,text="Вопрос 3. Кто создал Python?")
lab3.place(relx=.415,rely=.330)

r21 = Radiobutton(root,text="Billy Herrington",value=5,variable=var2)
r21.place(relx=.415,rely=.345)
r22 = Radiobutton(root,text="Guido van Rossum",value=6,variable=var2)
r22.place(relx=.415,rely=.365)
r23 = Radiobutton(root,text="Dennis Ritchie",value=7,variable=var2)
r23.place(relx=.415,rely=.385)
r24 = Radiobutton(root,text="Markus Persson",value=8,variable=var2)
r24.place(relx=.415,rely=.405)

lab4 = Label(root,text="Вопрос 4. В какой популярной игре все скрипты написаны на Python?")
lab4.place(relx=.415,rely=.430)


r31 = Radiobutton(root,text="CS:GO",value=9,variable=var3)
r31.place(relx=.415,rely=.450)
r32 = Radiobutton(root,text="Mount and Blade",value=10,variable=var3)
r32.place(relx=.415,rely=.470)
r33 = Radiobutton(root,text="Warcraft 2",value=11,variable=var3)
r33.place(relx=.415,rely=.490)
r34 = Radiobutton(root,text="Massegebox",value=12,variable=var3)
r34.place(relx=.415,rely=.510)


lab5 = Label(root,text="Вопрос 5. Какая программа из ниже перечисленных написана на Python?")
lab5.place(relx=.415,rely=.530)


r41 = Radiobutton(root,text="TBoI",value=13,variable=var4)
r41.place(relx=.415,rely=.550)
r42 = Radiobutton(root,text="Discord",value=14,variable=var4)
r42.place(relx=.415,rely=.570)
r43 = Radiobutton(root,text="RaidCall",value=15,variable=var4)
r43.place(relx=.415,rely=.590)
r44 = Radiobutton(root,text="Blender",value=16,variable=var4)
r44.place(relx=.415,rely=.610)





button1=Button(root,text='Проверка всех решений',command=a)
button1.place(relx=.420,rely=.640)

root.mainloop()
