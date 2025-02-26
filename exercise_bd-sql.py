import sqlite3
students = sqlite3.connect('students_database.db')
cursor = students.cursor()

cursor.execute('CREATE TABLE students (id INT, name VARCHAR(100), age INT, course VARCHAR(100));')

students.commit()
students.close()

print("Banco de Dados atualizado com sucesso!")