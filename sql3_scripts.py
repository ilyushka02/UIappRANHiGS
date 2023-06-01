import sqlite3 as sql
import  datetime as dt

def select(path_for_db: str):
    try:
        sqlite_connection = sql.connect(path_for_db, timeout=20)
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT user_name, date_birthday, age, email from users_info"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()

    except sql.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

    return records

def insert(path_for_db: str, user_name, dt_b, email):
    dt_b = dt.datetime.strptime(dt_b, '%d.%m.%Y')
    sec = dt_b.timestamp()
    age = dt.datetime.now().year - dt_b.year

    try:
        sqlite_connection = sql.connect(path_for_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_query = f"""INSERT INTO users_info
                           (User_name, date_birthday, age, email)  VALUES  ('{user_name}', {sec}, {age}, '{email}')"""

        cursor.execute(sqlite_insert_query)

        sqlite_connection.commit()
        cursor.close()

    except sql.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

