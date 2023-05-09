import tkinter as tk
import sqlite3 as sql


try:
    connection = sql.connect("C:/databases/UIapp.db")
    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sql.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.close()
        print("Соединение с SQLite закрыто")
#
# window = tk.Tk()
# window.title("Окно")
#
#
#
# window.geometry("500x500")
# window.mainloop()
