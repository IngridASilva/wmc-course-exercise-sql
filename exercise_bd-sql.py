import sqlite3
students = sqlite3.connect('students_database.db')
cursor = students.cursor()

# 1)
# cursor.execute('CREATE TABLE students (id INT, name VARCHAR(100), age INT, course VARCHAR(100));')

# 2)
cursor.execute('INSERT INTO students(id, name, age, course) VALUES (1, "Ingrid", 24, "Economics")')
cursor.execute('INSERT INTO students(id, name, age, course) VALUES (2, "Jessica", 18, "Journalism")')
cursor.execute('INSERT INTO students(id, name, age, course) VALUES (3, "Elisa", 24, "Engineering")')
cursor.execute('INSERT INTO students(id, name, age, course) VALUES (4, "Thalissa", 28, "Biology")')
cursor.execute('INSERT INTO students(id, name, age, course) VALUES (5, "Brenda", 19, "Administration")')

students.commit()
students.close()

print("Database successfully updated!")