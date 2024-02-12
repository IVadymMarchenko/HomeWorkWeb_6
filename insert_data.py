import sqlite3
from faker import Faker
from random import randint, choice
from random import randint
fake = Faker('uk_UA')
group_id = [1,2,3]
name_group = ['математика','физика','биология']
name_group1=['groupA','groupB','groupC']

def generation_data(conn):
    try:
        cursor = conn.cursor()

        # Заполняем студентов
        for id in range(1, 31):
            student_name = fake.name()
            cursor.execute('INSERT INTO Students (name, group_id) VALUES (?, ?)', (student_name, choice(group_id)))

        # Заполняем группы
        for group in range(3):
            cursor.execute('INSERT INTO Groups (group_name) VALUES (?)', (name_group1[group],))

        # Заполняем учителей
        for teacher_id in range(50, 53):
            teacher_name = fake.name()
            cursor.execute('INSERT INTO Teachers (name) VALUES (?)', (teacher_name,))

        # Заполняем предметы
        for i, subject_name in enumerate(name_group):
            cursor.execute('INSERT INTO Subjects (subject_name, teacher_id) VALUES (?, ?)', (subject_name, i+1))

        #Заполняем оценки
        for student_id in range(1, 31):
            for subject_id in range(1, 4):
                grade = randint(2, 5)  # Генерируем случайную оценку от 2 до 5
                date_received = fake.date_between(start_date='-1y', end_date='today')
                cursor.execute("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                               (student_id, subject_id, grade, date_received))

        conn.commit()
        print('generation data ok')
    except sqlite3.Error as err:
        conn.rollback()
        print(err)












