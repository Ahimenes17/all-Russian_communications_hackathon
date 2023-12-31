from tkinter import *
from tkinter import ttk
from task1 import post
from tkinter import messagebox
from task2 import form2
from task1 import form1
import json

main_form = Tk()
main_form.title("Главная форма")
main_form.geometry("500x150")


def third():
    third_task = Tk()
    third_task.title("Третье задание")
    third_task.geometry("300x200")

    label_number_phone = Label(third_task, text="Телефон")
    label_number_phone.place(x=10, y=5)
    label_key = Label(third_task, text="Ключ")
    label_key.place(x=150, y=5)
    label_group = Label(third_task, text="Группа")
    label_group.place(x=10, y=100)

    value_number_phone = StringVar()
    entry_number_phone = Entry(third_task, width=20, textvariable=value_number_phone)
    entry_number_phone.place(x=10, y=25)

    value_key = StringVar()
    entry_key = Entry(third_task, width=20, textvariable=value_key)
    entry_key.place(x=150, y=25)

    value_group = StringVar()
    entry_group = Entry(third_task, width=24, textvariable=value_group)
    entry_group.place(x=10, y=120)

    def autorization():
        val_num_phone1 = str(entry_number_phone.get())
        val_key1 = str(entry_key.get())

    def get_group():
        pass

    button_get_key = Button(
        third_task,
        text="Авторизаваться",
        padx=15,
        pady=5,
        command=autorization,
    )
    button_get_key.place(x=10, y=50)

    button_get_group = Button(
        third_task,
        text="Получить сообщения",
        padx=10,
        pady=5,
        command=autorization,
    )
    button_get_group.place(x=10, y=150)


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
    command=third,
)
button3.place(x=350, y=50)

main_form.mainloop()
