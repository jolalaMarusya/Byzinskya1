import tkinter
from tkinter import messagebox

ca=0
count_o=0


window = tkinter.Tk()
window.title("Оконце")
window.geometry("750x310")

frame = tkinter.Frame(window) 

frame.pack()


var = tkinter.StringVar()

chi = tkinter.IntVar()
chi.set(0)


label = tkinter.Label(frame,
                      textvariable=var,
                      height= 1,
                      width = 10) 

label.pack() 


entry = tkinter.Entry(frame,
                      textvariable=var,
                      width = 80,
                      font= 50)

entry.pack()



b=tkinter.Button(window,text="Выйти",
                 background="magenta4",
                 foreground="snow",
                 bd = 5,
                 height = 2,
                 width = 8,
                 font=("comic sans ms", 16),
                 command=window.destroy)
b.pack(side=tkinter.RIGHT)

def counto():
    o = entry.get()
    O = entry.get()
    chio=o.count("о")
    chiO = O.count("О")
    chioo = chio + chiO
    messagebox.showinfo("Колво О",chioo)
        
def counta():
    a = entry.get()
    A = entry.get()
    chia=a.count("а")
    chiA = A.count("А")
    chiaa= chia + chiA
    messagebox.showinfo("Колво A",chiaa)

def aando():
    a = entry.get()
    A = entry.get()
    chia=a.count("а")
    chiA = A.count("А")
    chiaa= chia + chiA
    o = entry.get()
    O = entry.get()
    chio=o.count("о")
    chiO = O.count("О")
    chioo = chio + chiO
    chichi = chiaa + chioo
    messagebox.showinfo("Всего А и О",chichi)

bu=tkinter.Button(window,text="Посчитать О",
                  background="purple3",
                  foreground="snow",
                  bd = 5,
                  height = 2,
                  width = 12,
                  font=("comic sans ms", 16),
                  command=counto)
bu.pack()

buu=tkinter.Button(window, text = "Посчитать А",
                   background="purple3",
                   foreground="snow",
                   bd = 5,
                   height = 2,
                   width = 12,
                   font=("comic sans ms", 16),
                   command=counta)
buu.pack()

buuu=tkinter.Button(window, text = "Посчитать всё количество А и О",
                   background="purple3",
                   foreground="snow",
                    bd = 5,
                    height = 2,
                    width = 30,
                    font=("comic sans ms]", 18),
                   command=aando)
buuu.pack()
                        

window.mainloop()  
