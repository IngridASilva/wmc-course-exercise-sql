import sqlite3
students = sqlite3.connect('students_database.db')
cursor = students.cursor()

# 1)
# cursor.execute('CREATE TABLE students (id INT, name VARCHAR(100), age INT, course VARCHAR(100));')

# 2)
# cursor.execute('INSERT INTO students(id, name, age, course) VALUES (1, "Ingrid", 24, "Economics")')
# cursor.execute('INSERT INTO students(id, name, age, course) VALUES (2, "Jessica", 18, "Journalism")')
# cursor.execute('INSERT INTO students(id, name, age, course) VALUES (3, "Elisa", 24, "Engineering")')
# cursor.execute('INSERT INTO students(id, name, age, course) VALUES (4, "Thalissa", 28, "Biology")')
# cursor.execute('INSERT INTO students(id, name, age, course) VALUES (5, "Brenda", 19, "Administration")')

# 3)
# a)
# all_records = cursor.execute('SELECT * FROM students')
# for students in all_records:
    # print(students)

# b)
# name_age_records = cursor.execute('SELECT name, age FROM students WHERE age > 20')
# for students in name_age_records:
    # print(students)

# c)
# course_records = cursor.execute('SELECT * FROM students WHERE course = "Engineering" ORDER BY name')
# for students in course_records:
    # print(students)

# d)
# count_records = cursor.execute('SELECT COUNT(*) FROM students')
# count_records = cursor.fetchone()[0]
    # print(f"Total de alunos: {count_records}")

# 4)
# a)
# cursor.execute('UPDATE students SET age = 27 WHERE id = 4')
# age_update_records = cursor.execute('SELECT age FROM students WHERE id = 4')
# for students in age_update_records:
    # print(students)

# b)
# cursor.execute('DELETE FROM students WHERE id = 5')
# id_delete_records = cursor.execute('SELECT * FROM students')
# for students in id_delete_records:
    # print(students)

students.commit()
students.close()

print("Database successfully updated!")