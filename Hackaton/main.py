from tkinter import *
from tkinter import ttk
from Pst import post
from tkinter import messagebox
from pythonProject import form2

import json

main_form = Tk()
main_form.title("Главная форма")
main_form.geometry("500x150")


def first():
    first_task = Tk()
    first_task.title("Первое задание")
    first_task.geometry("500x150")

    label_radius = Label(first_task, text="Радиус охвата ")
    label_radius.place(x=370, y=10)

    label_dolgota = Label(first_task, text="Долгота ")
    label_dolgota.place(x=130, y=10)

    label_shirota = Label(first_task, text="Широта")
    label_shirota.place(x=250, y=10)

    label_token = Label(first_task, text="Токен ")
    label_token.place(x=10, y=10)

    value_radius = DoubleVar()
    entry_radyus = Entry(first_task, width=15, textvariable=value_radius)
    entry_radyus.place(x=370, y=50)

    value_dolgota = DoubleVar()
    entry_dolgota = Entry(first_task, width=15, textvariable=value_dolgota)
    entry_dolgota.place(x=130, y=50)

    value_shirota = DoubleVar()
    entry_shirota = Entry(first_task, width=15, textvariable=value_shirota)
    entry_shirota.place(x=250, y=50)

    value_token = StringVar()
    entry_token = Entry(first_task, width=15, textvariable=value_token)
    entry_token.place(x=10, y=50)

    def get_data():
        value_radius1 = float(entry_radyus.get())
        value_dolgota1 = float(entry_dolgota.get())
        value_shirota1 = float(entry_shirota.get())
        value_token1 = str(entry_token.get())
        with open("F:\projekt\Python\Hackaton\data.txt", "w") as file:
            json.dump(
                post.address_search(
                    token=value_token1,
                    radius=value_radius1,
                    longitude=value_dolgota1,
                    latitude=value_shirota1,
                ),
                file,
                indent=4,
            )
        messagebox.showinfo(
            title="Адреса",
            message="Адреса домов, находящихся в радиусе охвата, записаны в файл data.txt",
        )

    button_get_address = Button(
        first_task,
        text="Ввести",
        bg="black",
        fg="white",
        padx=20,
        pady=5,
        command=get_data,
    )
    button_get_address.place(x=100, y=80)

    def get_office():
        value_radius1 = float(entry_radyus.get())
        value_dolgota1 = float(entry_dolgota.get())
        value_shirota1 = float(entry_shirota.get())
        value_token1 = str(entry_token.get())
        messagebox.showinfo(
            title="Почтовые отделения",
            message=post.postal_office_find(
                value_token1,
                post.address_search(
                    value_token1, value_shirota1, value_dolgota1, value_radius1
                ),
            ),
        )

    button_get_office = Button(
        first_task,
        text="Найти почтовые отделения",
        bg="black",
        fg="white",
        padx=20,
        pady=5,
        command=get_office,
    )
    button_get_office.place(x=200, y=80)


def third():
    third_task = Tk()
    third_task.title("Третье задание")
    third_task.geometry("450x150")

    label_number_phone = Label(third_task, text="Телефон")
    label_number_phone.place(x=10, y=25)
    label_key = Label(third_task, text="Ключ")
    label_key.place(x=130, y=25)
    label_group = Label(third_task, text="Группа")
    label_group.place(x=250, y=25)

    value_number_phone = StringVar()
    entry_number_phone = Entry(third_task, width=15, textvariable=value_number_phone)
    entry_number_phone.place(x=10, y=50)

    value_key = StringVar()
    entry_key = Entry(third_task, width=15, textvariable=value_key)
    entry_key.place(x=130, y=50)

    value_group = StringVar()
    entry_group = Entry(third_task, width=26, textvariable=value_group)
    entry_group.place(x=250, y=50)

    def autorization():
        val_num_phone1 = str(entry_number_phone.get())
        val_key1 = str(entry_key.get())

    def get_group():
        pass

    button_get_key = Button(
        third_task,
        text="Авторизаваться",
        bg="black",
        fg="white",
        padx=45,
        pady=5,
        command=autorization,
    )
    button_get_key.place(x=25, y=80)

    button_get_group = Button(
        third_task,
        text="Получить сообщения",
        bg="black",
        fg="white",
        padx=15,
        pady=5,
        command=autorization,
    )
    button_get_group.place(x=250, y=80)


button1 = Button(
    main_form,
    text="Первое задание",
    bg="black",
    fg="white",
    padx=20,
    pady=5,
    command=first,
)
button1.place(x=30, y=50)

button2 = Button(
    main_form,
    text="Второе задание",
    bg="black",
    fg="white",
    padx=20,
    pady=5,
    command=form2.second,
)
button2.place(x=190, y=50)

button3 = Button(
    main_form,
    text="Третье задание",
    bg="black",
    fg="white",
    padx=20,
    pady=5,
    command=third,
)
button3.place(x=350, y=50)

main_form.mainloop()
