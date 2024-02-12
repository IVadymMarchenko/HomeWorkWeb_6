import sqlite3
from insert_data import generation_data
import great_table
from great_table import *

# Имя файла базы данных SQLite
DB_FILE = 'my_database.db'

# Подключаемся к БД а если её нет то создаем
def create_data(DB_FILE):
    with sqlite3.connect(DB_FILE) as conn:
        return conn

def create_tables(conn, creat_table_sql):
    try:
        c = conn.cursor()
        c.execute(creat_table_sql)
        conn.commit()
    except Exception as err:
        conn.rollback()
        print(err)

def main():
    conn = create_data(DB_FILE)
    # Создаем наши таблицы
    create_tables(conn, great_table.sql_create_students_table)
    create_tables(conn, great_table.sql_create_groups_table)
    create_tables(conn, great_table.sql_create_teachers_table)
    create_tables(conn, great_table.sql_create_subjects_table)
    create_tables(conn, great_table.sql_create_grades_table)
    #Заполнение таблиц данными
    generation_data(conn)
    print('OK')



if __name__=='__main__':
    #Запустив этот скрипт он создаст базу данных в папке проэкта и наполнит её данными!
    #Дальше нужно перейти в папку SQL-enquiries и
    main()



