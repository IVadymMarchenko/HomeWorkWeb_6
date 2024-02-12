sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES Groups(id)
);
 """


sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS Groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(50)
);
"""


sql_create_teachers_table="""CREATE TABLE IF NOT EXISTS Teachers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);"""


sql_create_subjects_table="""CREATE TABLE IF NOT EXISTS Subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(50),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);"""


sql_create_grades_table="""CREATE TABLE IF NOT EXISTS Grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date_received DATE,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(id)
);"""