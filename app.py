from tkinter import *
from turtle import bgcolor 

def window():
    root = Tk()
    root.title("Система для учета грузов")
    root.geometry('800x600')
    browse_btn=Button(root, width=20, height=4, bg='#ff0000', text="Войти")
    browse_btn.grid(column=2, row=1, padx=50)
    root.mainloop()

window()