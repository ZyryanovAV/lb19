from tkinter import *

def fun_1(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab['text'] = ' '.join(s)


root = Tk()
but=Button(text="Преобразовать")
ent=Entry(root, width=20)
lab = Label(root, width=100, bg='black', fg='white', text="Жопа привет мир да я думаю")
but.bind('<Button-1>', fun_1)

ent.pack()
lab.pack()
but.pack()
root.geometry("450x250+300+300")
root.mainloop()