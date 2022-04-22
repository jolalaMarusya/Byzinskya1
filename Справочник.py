from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry('1920x1080')
root.title('Справочка')

var1= IntVar()
var1.set(0)
var2= IntVar()
var2.set(0)
answer1 = StringVar()

def canvas1():
    messagebox.showinfo("Кнопка","Текстик в окне")
def Kol(event):
    nadpis.configure(text=answer1)

label1 = Label(width=25,height=1,text = "Маленькая справочка по tkinter")
label1.pack()

label2 = Label(width=15,height=1,text = "1.Список")
label2.pack()

listbox1=Listbox(width=15,
                height=8)
listbox1.pack()

for i in ('Один','Два','Три','Четыре','Пять','Шесть','Семь','Восемь'):
    listbox1.insert(0,i)

#canvas= Canvas(width=700,height=500)
#canvas.pack()

#obj=PhotoImage(file="Ofo.png")

#id=canvas.create_image(50,50,anchor=NW,image=obj)

label3 = Label(width=15,height=1,text = "2.Переключатели")
label3.pack()

radiohead1=Radiobutton(root,text="Хоба?",value=1)
radiohead2=Radiobutton(root,text="Хобана?!",value=2)
radiohead1.pack()
radiohead2.pack()

label4 = Label(width=15,height=1,text = "3.Флажки")
label4.pack()

c1 = Checkbutton(root, text="Первый флажочек",
                 variable=var1,
                 onvalue=1, offvalue=0)
c1.pack()

c2 = Checkbutton(root, text="Второй флажочек",
                 variable=var2,
                 onvalue=1, offvalue=0)
c2.pack()

label5 = Label(width=15,height=1,text = "4.Кнопка")
label5.pack()

button1=Button(root,text='Проверка кнопки',command=canvas1)
button1.pack()

label6 = Label(width=15,height=1,text = "5.Надпись")
label6.pack()

label7 = Label(width=150,height=1,text = "Большая длинная надпись без запятых потому что нужен массивный текст а также без особого смысла и неизвестно влезет ли она спойлер: не влезла:)")
label7.pack()

label8 = Label(width=150,height=1,text = "6.Поле для ввода")
label8.pack()

entry1 = Entry(root,textvariable = answer1)
entry1.pack()

nadpis = Label(root, textvariable = answer1)
nadpis.pack()

root.mainloop()
