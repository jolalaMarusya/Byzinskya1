from tkinter import *
import winsound

root = Tk()
root.geometry('1000x350')
root.title('Самоучитель')

def Zvuk():
 winsound.Beep(2000, 1000)

def Lev(event):
 nadpis.configure(text='Левая кнопка')
def Prav(event):
 nadpis.configure(text='Правая кнопка')
def Koleso(event):
    nadpis.configure(text='Колёсико мыши')
def new_window(event):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title('Второе окно')
    but2 = Button(window, text='Привет, товарищи ученики!')
    but2.pack()

def new_w_color(event) :
    window = Toplevel(root)
    window.geometry('400x400')
    window.title('Второе окно')
    but2 = Button(window, text='Меняй цвет на Красный')
    but2.bind('<Button->',new_c_red)
    butt3 = Button(window, text='Меняй цвет на Голубой')
    butt3.bind('<Button->',new_c_blue)
    butt3.pack()
    but2.pack()

def new_c_red(event):
    root["bg"] = "crimson"

def new_c_blue(event):
    root["bg"] = "blue"

def new_c_text(event):
    lab["fg"] = "maroon"


def new_wi(event):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title('Хобана')
    window.pack(fill=BOTH,expand=True)
    window.ver = BooleanVar()
    cb = Checkbutton(window,text="Убери галочку",
                     variable=window.var,command=window.onClick)
    cb.select()
    cb.place(x=50,y=50)
    

def onClick(window):
    if window.var.get() == True:
        window.master.title("Мурик")
    else:
        window.master.title("")

    
    

    
    


lab = Label(root,
            text="Уважаемые учащиеся. Вашему вниманию предлагается самоучитель по Python. Разработчик: Дмитрий Гульшин и Данила Епишкин. Связь с автором vk.com/bobola.")
lab.pack()

bexit=Button(root,text="Выйти",
             background="magenta4",
             foreground="snow",
             bd = 5,
             height = 2,
             width = 10,
             font=("comic sans ms",16),
             command=root.destroy)
bexit.pack(side=RIGHT)


button = Button(root,
                text='Звук!',
                background="magenta4",
                 foreground="snow",
                 bd = 5,
                 height = 2,
                 width = 10,
                 font=("comic sans ms",16),
                command=Zvuk)
button.pack() 

knopka = Button(root, text = 'Нажмите любую кнопку мыши')
nadpis = Label(root, text = 'Пока ничего не нажато')
knopka.pack()
nadpis.pack()
knopka.bind('<Button-1>', Lev)
knopka.bind('<Button-3>', Prav)
knopka.bind('<Button-2>',Koleso)


but = Button(root, text='Создать новое окно')
but.bind('<Button->', new_window)

but.pack()

butcolor= Button(root,text="Поменяй свой цвет!")
butcolor.bind('<Button->',new_w_color)
butcolor.pack()

buttctext = Button(root,text="Поменяй цвет текста нашего обращения!")
buttctext.bind('<Button->',new_c_text)
buttctext.pack()

ButtHu = Button(root,text="Абоба")
ButtHu.bind('<Button->',new_wi)
ButtHu.pack()

root.mainloop()
