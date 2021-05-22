#!/usr/bin/env python3
# -*- config: utf-8 -*-

# виджеты Radiobatton и Checkbutton поддерживают большинство свойств
# оформления внешнего вида, которые есть у других элементов графического интерфейса.
# При этом у Radiobutton есть особое свойство indicatoron . По-умолчанию он равен
# единице, в этом случае радиокнопка выглядит как нормальная радиокнопка. Однако если
# присвоить этой опции ноль, то виджет Radiobutton становится похожим на обычную кнопку
# по внешнему виду. Но не по смыслу.

from tkinter import *


def phone():
    a = var.get()
    if a == 0:
        label['text'] = '8 768754367'
    elif a == 1:
        label['text'] = '+7 908565421'
    elif a == 2:
        label['text'] = '+7 121565212'


root = Tk()

f = Frame()
f.pack(side=LEFT)

var = IntVar()
var.set(-1)
Radiobutton(f, text="Вася", width=10, height=3,
            indicatoron=0, variable=var,
            value=0, command=phone).pack()
Radiobutton(f, text="Петя", width=10, height=3, indicatoron=0, variable=var,value=1, command=phone).pack()
Radiobutton(f, text="Маша", width=10, height=3, indicatoron=0, variable=var, value=2, command=phone).pack()

label = Label(bg="white", width=25)
label.pack(side=LEFT, fill=Y)

root.mainloop()
