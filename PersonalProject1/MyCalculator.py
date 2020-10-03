# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:09:08 2020

@author: Admin
"""
import tkinter
from tkinter import *
from tkinter import messagebox

def proces():
    try:
        E4.delete(0, END)
        E4.insert(0, "")
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=int(number1)
        number2=int(number2)
        if operator=='+':
            answer=number1+number2
        elif operator=='-':
            answer=number1-number2
        elif operator=='*':
            answer=number1*number2
        elif operator=='/':
            answer=number1/number2
        Entry.insert(E4,0,answer)
        print(answer)
    except ValueError:
        messagebox.showwarnning("Warning","Please enter a value in integer")

def doIt():
    L1=Label(root, text="My Calculator").grid(row=0,column=1)
    L2=Label(root, text="Number 1").grid(row=1,column=0)
    L3=Label(root, text="Number 2").grid(row=2,column=0)
    L4=Label(root, text="Operation").grid(row=3,column=0)
    L5=Label(root, text="Answer").grid(row=4,column=0)
    E1=Entry(root, bd=3)
    E1.grid(row=1,column=1)
    E2=Entry(root, bd=3)
    E2.grid(row=2,column=1)
    E3=Entry(root, bd=3)
    E3.grid(row=3,column=1)
    E4=Entry(root, bd=3)
    E4.grid(row=4,column=1)
    
    B=Button(root,text="Submit").grid(row=5,column=1)
    B=Button(root, text ="Submit",command= proces).grid(row=5,column=1)


root = tkinter.Tk()
root.title("Basic Calculator")
#root.geometry("500x200")
root.update() 
label=tk.Label(root,text="before")
label.pack()
root.after(2000,doIt)   
root.mainloop()


