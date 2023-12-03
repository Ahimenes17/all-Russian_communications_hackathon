from tkinter import *
from tkinter import ttk
from task1 import post
from tkinter import simpledialog
from task1 import form1
from task2 import form2
from task3 import form3
import json
import builtins


def gui_input(prompt):  # функция, заменяющая input()
    answer = simpledialog.askstring(title="Input", prompt=prompt)
    return answer


builtins.input = gui_input  # переопределение функции ввода


main_form = Tk()
main_form.title("Главная форма")
main_form.geometry("500x150")

button1 = Button(
    main_form,
    text="Первое задание",
    padx=20,
    pady=5,
    command=form1.first,
)
button1.place(x=30, y=50)

button2 = Button(
    main_form,
    text="Второе задание",
    padx=20,
    pady=5,
    command=form2.second,
)
button2.place(x=190, y=50)

button3 = Button(
    main_form,
    text="Третье задание",
    padx=20,
    pady=5,
    command=form3.third,
)
button3.place(x=350, y=50)

main_form.mainloop()
