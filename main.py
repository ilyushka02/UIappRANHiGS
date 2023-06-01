from tkinter import *
from tkinter import ttk
import datetime as dt
import sql3_scripts as sql
import pandas as pd

font = 'Times 12'
month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
days = [day+1 for day in range(0,31)]
years = [year for year in range(1970, dt.datetime.now().year + 1, 1)]
name_db = 'UIapp'
path_for_db = f'C:/databases/{name_db}.db'
people = []

def select_row():
    people = sql.select(path_for_db)
    da = pd.DataFrame(people)
    da[1] = pd.to_datetime(da[1], unit='s')
    da[1] = da[1].dt.strftime('%d.%m.%Y')
    people = list(da.itertuples(index=False, name=None))
    for i in tree.get_children():
        tree.delete(i)
    for person in people:
        tree.insert("", END, values=person)

def insert_row():
    user = name_var.get()
    email_str = email_var.get()
    d = day_var.get()
    if int(d) < 10:
        d = f'0{d}'
    m = month.index(month_var.get()) + 1
    if int(m) < 10:
        m = f'0{m}'
    y = year_var.get()
    date = f'{d}.{m}.{y}'
    sql.insert(path_for_db, user, date, email_str)

root = Tk()
root.title("UIapp")
root.geometry('800x400')

name_var = StringVar()
email_var = StringVar()
day_var = StringVar()
month_var = StringVar()
year_var = StringVar()

lbl = Label(root, text="Введите данные пользователя:", font='Times 14').place(x=0, y=0)

lbl1 = Label(root, text="Имя:", font=font).place(x=0, y=25)
name = Entry(root, textvariable=name_var, font=font, width=30).place(x=50, y=25)

lbl2 = Label(root, text="Дата рождения:", font=font).place(x=0, y=50)

day_box = ttk.Combobox(values=days, textvariable=day_var, width=5).place(x=120, y=50)
mounth_box = ttk.Combobox(values=month, textvariable=month_var, width=5).place(x=180, y=50)
year_box = ttk.Combobox(values=years, textvariable=year_var, width=5).place(x=240, y=50)

lbl3 = Label(root, text="Email:", font=font).place(x=0, y=75)
email = Entry(root, textvariable=email_var, font=font, width=30).place(x=50, y=75)

insert = Button(root, text ="Добавить запись", width=20, command=insert_row).place(x=300, y=25)
select = Button(root, text ="Загрузить данные из БД", width=20, command=select_row).place(x=460, y=25)

# определяем столбцы
columns = ("name", "dt_b", 'age', "email")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1, pady=120)

# определяем заголовки
tree.heading("name", text="Имя")
tree.heading("dt_b", text="Д.р")
tree.heading("age", text="Возраст")
tree.heading("email", text="Email")


root.mainloop()