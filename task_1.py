#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Напишите простейший калькулятор, состоящий из двух текстовых полей,
#куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат вычисления
#должен отображаться в метке. Если арифметическое действие выполнить невозможно
#(например, если были введены буквы, а не числа), то в метке должно появляться слово
#"ошибка".

from tkinter import *

def summa(self):
    try:
        s = float(ent_1.get())
        x = float(ent_2.get())
        res = s + x
        lab['text'] = ' '.join(str(res))
    except(ValueError):
        lab['text'] = "Ошибка"

def raznost(self):
    try:
        s = float(ent_1.get())
        x = float(ent_2.get())
        res = s - x
        lab['text'] = ' '.join(str(res))
    except(ValueError):
        lab['text'] = "Ошибка"

def proiz(self):
    try:
        s = float(ent_1.get())
        x = float(ent_2.get())
        res = s * x
        lab['text'] = ' '.join(str(res))
    except(ValueError):
            lab['text'] = "Ошибка"

def delen(self):
    try:
        s = float(ent_1.get())
        x = float(ent_2.get())
        res = s / x
        lab['text'] = ' '.join(str(res))
    except(ValueError):
                lab['text'] = "Ошибка"


root = Tk()
root.geometry("500x300+300+300")
root.title("Калькулятор")
but_1 = Button(text="+", width=20, height=1)
but_1['bg'] = '#555555'
but_1['activebackground'] = '#FFF523'
but_1['activeforeground'] = '#ffffff'
but_2 = Button(text="-", width=20, height=1)
but_3 = Button(text="*", width=20, height=1)
but_4 = Button(text="/", width=20, height=1)
ent_1 = Entry(root, width=20)
ent_2 = Entry(root, width=20)
lab = Label(root, width=20, bg='black', fg='white', text=" ")
but_1.bind('<Button-1>', summa)
but_2.bind('<Button-1>', raznost)
but_3.bind('<Button-1>', proiz)
but_4.bind('<Button-1>', delen)

ent_1.pack()
ent_2.pack()
but_1.pack()
but_2.pack()
but_3.pack()
but_4.pack()
lab.pack()
root.mainloop()