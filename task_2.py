#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых соответствуют
#цветам радуги.При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в
#метку – название цвета.
#Коды цветов в шестнадцатеричной кодировке:  # ff0000 – красный, #ff7d00 – оранжевый,
# ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff –фиолетовый.

from tkinter import *

def vstavlyator_1(self):
    lab['text'] = "Красный"
    ent.delete(0, END)
    ent.insert(0, "#ff0000")

def vstavlyator_2(self):
    lab['text'] = "Оранжевый"
    ent.delete(0, END)
    ent.insert(0, "#ff7d00")

def vstavlyator_3(self):
    lab['text'] = "Желтый"
    ent.delete(0, END)
    ent.insert(0, "#ffff00")

def vstavlyator_4(self):
    lab['text'] = "Зеленый"
    ent.delete(0, END)
    ent.insert(0, "#00ff00")

def vstavlyator_5(self):
    lab['text'] = "Голубой"
    ent.delete(0, END)
    ent.insert(0, "#007dff")

def vstavlyator_6(self):
    lab['text'] = "Синий"
    ent.delete(0, END)
    ent.insert(0, "#0000ff")

def vstavlyator_7(self):
    lab['text'] = "Фиолетовый"
    ent.delete(0, END)
    ent.insert(0, "#7d00ff")

root = Tk()
root.geometry("650x450+300+300")
root.title("Радуга")
ent = Entry(root, width=20)
lab = Label(root, width=20, height=2, bg='black', fg='white')
but_1 = Button(width=15, height=3)
but_1['bg'] = '#ff0000'
but_2 = Button(width=15, height=3)
but_2['bg'] = '#ff7d00'
but_3 = Button(width=15, height=3)
but_3['bg'] = '#ffff00'
but_4 = Button(width=15, height=3)
but_4['bg'] = '#00ff00'
but_5 = Button(width=15, height=3)
but_5['bg'] = '#007dff'
but_6 = Button(width=15, height=3)
but_6['bg'] = '#0000ff'
but_7 = Button(width=15, height=3)
but_7['bg'] = '#7d00ff'
but_1.bind('<Button-1>', vstavlyator_1)
but_2.bind('<Button-1>', vstavlyator_2)
but_3.bind('<Button-1>', vstavlyator_3)
but_4.bind('<Button-1>', vstavlyator_4)
but_5.bind('<Button-1>', vstavlyator_5)
but_6.bind('<Button-1>', vstavlyator_6)
but_7.bind('<Button-1>', vstavlyator_7)

lab.pack()
ent.pack()
but_1.pack()
but_2.pack()
but_3.pack()
but_4.pack()
but_5.pack()
but_6.pack()
but_7.pack()
root.mainloop()


