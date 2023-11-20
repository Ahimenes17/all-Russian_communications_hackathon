from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from task2.second_file import VK

def second():
    second_task = Tk()
    second_task.title("Второе задание")
    second_task.geometry("400x200")

    label1 = Label(second_task, text="Токен авторизации", fg="blue", cursor="hand2")
    label1.bind('<Button-1>', lambda e: messagebox.showinfo("Как получить токен", "Для получения токена пользователя перейдите по ссылке https://vkhost.github.io/\nНа странице находится инструкция как получить токен\nСреди кнопок вверху страницы нажмите на любую, авторизуйтесь в ВК и скопируйте токен в буфер обмена\nПолученную строку вставьте в поле ниже"))
    label1.place(x=10, y=10)

    value_token = StringVar(second_task)
    entry_token = Entry(second_task, width=20, textvariable=value_token)
    entry_token.place(x=10, y=30)

    label_group = Label(second_task, text="Группа ")
    label_group.place(x=10, y=100)

    label_user = Label(second_task, text="ID Пользователя ")
    label_user.place(x=160, y=100)

    value_group = StringVar(second_task)
    entry_group = Entry(second_task, width=20, textvariable=value_group, state='disabled')
    entry_group.place(x=10, y=125)

    value_user = StringVar(second_task)
    entry_user = Entry(second_task, width=20, textvariable=value_user, state='disabled')
    entry_user.place(x=160, y=125)

    get_mode = BooleanVar(second_task)
    get_mode.set(True)
    get_mode_users = Radiobutton(second_task, text="users.get", variable=get_mode, value=True, state='disabled')
    get_mode_exec = Radiobutton(second_task, text="execute", variable=get_mode, value=False, state='disabled')

    get_mode_users.place(x=300, y=105)
    get_mode_exec.place(x=300, y=125)

    raw = BooleanVar(second_task)
    raw_check = Checkbutton(second_task, text='Выводить JSON', variable=raw, offvalue=0, onvalue=1)
    raw_check.place(x=160, y=20)

    def login():
        entry_group['state'] = 'disabled'
        entry_user['state'] = 'disabled'
        button_get_user['state'] = 'disabled'
        button_get_group['state'] = 'disabled'
        get_mode_users['state'] = 'disabled'
        get_mode_exec['state'] = 'disabled'
        global vk
        try:
            print(str(entry_token.get()))
            vk = VK(token=str(entry_token.get()))
            entry_group['state'] = 'normal'
            entry_user['state'] = 'normal'
            button_get_user['state'] = 'normal'
            button_get_group['state'] = 'normal'
            get_mode_users['state'] = 'normal'
            get_mode_exec['state'] = 'normal'
        except Exception as e:
            if (str(e) == '[5] User authorization failed: no access_token passed.') or (str(e) == '[5] User authorization failed: invalid access_token (4).'):
                msg = messagebox.showinfo('Авторизация провалилась', 'Авторизация провалилась\nПроверьте корректность введенного токена и попробуйте еще раз')

    button_login = Button(
        second_task,
        text="Авторизоваться",
        padx=20,
        pady=5,
        command=login,
    )
    button_login.place(x=10, y=60)

    def get_group():
        group_id = str(entry_group.get())
        print(raw.get())
        r = vk.get_group_info(group_id, raw.get())
        messagebox.showinfo('Результат выполнения', r)

    def get_user():
        user_id = str(entry_user.get())
        if get_mode:
            r = vk.get_user_info(user_id, raw.get())
        else:
            r = vk.get_user_info_exec(user_id, raw.get())
        messagebox.showinfo('Результат выполнения', r)

    button_get_group = Button(
        second_task,
        text="Получить инфо",
        padx=20,
        pady=5,
        command=get_group,
        state='disabled'
    )
    button_get_group.place(x=10, y=160)

    button_get_user = Button(
        second_task,
        text="Получить инфо",
        padx=20,
        pady=5,
        command=get_user,
        state='disabled'
    )
    button_get_user.place(x=160, y=160)





