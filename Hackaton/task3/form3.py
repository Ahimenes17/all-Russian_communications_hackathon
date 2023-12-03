from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from task3.main import TG
import asyncio

def third():
    third_task = Tk()
    third_task.title("Третье задание")
    third_task.geometry("300x200")

    label_api_id = Label(third_task, text="api_id")
    label_api_id.place(x=10, y=5)
    value_api_id = StringVar(third_task)
    entry_api_id = Entry(third_task, width=20, textvariable=value_api_id)
    entry_api_id.place(x=10, y=25)

    label_api_hash = Label(third_task, text="api_hash")
    label_api_hash.place(x=150, y=5)
    value_api_hash = StringVar(third_task)
    entry_api_hash = Entry(third_task, width=20, textvariable=value_api_hash)
    entry_api_hash.place(x=150, y=25)

    async def autorisation():
        # global tg
        # tg = TG(value_api_id.get(), value_api_hash.get())
        if tg: print('done')

    button_get_key = Button(
        third_task,
        text="Авторизаваться",
        padx=15,
        pady=5,
        command=lambda: asyncio.run(autorisation()),
    )
    button_get_key.place(x=10, y=50)

    label_group = Label(third_task, text="Группа")
    label_group.place(x=10, y=100)
    value_group = StringVar(third_task)
    entry_group = Entry(third_task, width=24, textvariable=value_group)
    entry_group.place(x=10, y=120)

    async def get_group():
        if not (value_group.get() and value_api_id.get() and value_api_hash.get()):
            messagebox.showerror(title='Ошибка', message='Заполните все поля ввода')
        else:
            global tg
            tg = TG(value_api_id.get(), value_api_hash.get())
            r = await tg.run(entry_group.get())
            if r[:10].find('Ошибка') < 0:
                with open("./group_msg.txt", "w") as file:
                    file.write(r)
                messagebox.showinfo(
                    title="Выполнено",
                    message="Последние 100 сообщений выведены в файл group_msg.txt",
                )
            else:
                messagebox.showerror(
                    title="Произошла ошибка",
                    message=r
                )

    button_get_group = Button(
        third_task,
        text="Получить сообщения",
        padx=10,
        pady=5,
        command=lambda: asyncio.run(get_group()),
    )
    button_get_group.place(x=10, y=150)
