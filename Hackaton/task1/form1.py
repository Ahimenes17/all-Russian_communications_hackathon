from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
from task1 import post


def first():
    first_task = Tk()
    first_task.title("Первое задание")
    first_task.geometry("350x155")

    label_token = Label(first_task, text="Токен ")
    label_token.place(x=10, y=10)

    label_dolgota = Label(first_task, text="Долгота ")
    label_dolgota.place(x=10, y=60)

    label_shirota = Label(first_task, text="Широта")
    label_shirota.place(x=120, y=60)

    label_radius = Label(first_task, text="Радиус охвата ")
    label_radius.place(x=230, y=60)

    value_token = StringVar()
    entry_token = Entry(first_task, width=15, textvariable=value_token)
    entry_token.place(x=10, y=30)

    value_dolgota = DoubleVar()
    entry_dolgota = Entry(first_task, width=15, textvariable=value_dolgota)
    entry_dolgota.place(x=10, y=80)

    value_shirota = DoubleVar()
    entry_shirota = Entry(first_task, width=15, textvariable=value_shirota)
    entry_shirota.place(x=120, y=80)

    value_radius = DoubleVar()
    entry_radyus = Entry(first_task, width=15, textvariable=value_radius)
    entry_radyus.place(x=230, y=80)

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
        padx=25,
        pady=5,
        command=get_data,
    )
    button_get_address.place(x=10, y=110)

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
        padx=23,
        pady=5,
        command=get_office,
    )
    button_get_office.place(x=120, y=110)
