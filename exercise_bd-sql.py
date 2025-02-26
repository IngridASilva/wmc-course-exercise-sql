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
    # print(f"Total students: {count_records}")

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

# 5)
# cursor.execute('CREATE TABLE clients (id INT, name VARCHAR (100), age INT, balance FLOAT());')
# cursor.execute('INSERT INTO clients(id, name, age, balance) VALUES (1, "Ingrid", 24, 4000)')
# cursor.execute('INSERT INTO clients(id, name, age, balance) VALUES (2, "Henrique", 31, 10000)')
# cursor.execute('INSERT INTO clients(id, name, age, balance) VALUES (3, "Francisco", 80, 2000)')
# cursor.execute('INSERT INTO clients(id, name, age, balance) VALUES (4, "Maria Helena", 58, 1500)')
# cursor.execute('INSERT INTO clients(id, name, age, balance) VALUES (5, "Felipe", 35, 15000)')

# 6)
# a)
# name_age_clients_records = cursor.execute('SELECT name, age FROM clients WHERE age > 30')
# for clients in name_age_clients_records:
    # print(clients)

# b)
# average_balance_clients = cursor.execute('SELECT AVG(balance) AS average_balance FROM clients')
# average_balance_clients = cursor.fetchone()[0]
# print(f"Average balance: {average_balance_clients}")

# c)
# max_balance_clients = cursor.execute('SELECT name, balance FROM clients ORDER BY balance DESC LIMIT 1')
# max_balance_clients = cursor.fetchone()[0]
# print(f"Max balance: {max_balance_clients}")

# d)
# count_balance_clients = cursor.execute('SELECT COUNT(*) AS total_clientes FROM clients WHERE balance > 1000')
# count_balance_clients = cursor.fetchone()[0]
# print(f"Balance over 1000: {count_balance_clients}")

# 7)
# a)
# cursor.execute('UPDATE clients SET balance = 7000 WHERE id = 1')
# update_balance_clients = cursor.execute('SELECT * FROM clients')
# for clients in update_balance_clients:
    # print(clients)

# b)
# cursor.execute('DELETE FROM clients WHERE id = 5')
# delete_clients = cursor.execute('SELECT * FROM clients')
# for clients in delete_clients:
    # print(clients)

# 8)
# cursor.execute('CREATE TABLE shopping (id INT, client_id INT, product VARCHAR(100), value REAL);')

# cursor.execute('INSERT INTO shopping(id, client_id, product, value) VALUES (1,1,"Notebook",4500)')
# cursor.execute('INSERT INTO shopping(id, client_id, product, value) VALUES (2,2,"Piano",7000)')
# cursor.execute('INSERT INTO shopping(id, client_id, product, value) VALUES (3,3,"Cell phone",2000)')
# cursor.execute('INSERT INTO shopping(id, client_id, product, value) VALUES (4,1,"Cell phone",1900)')
# cursor.execute('INSERT INTO shopping(id, client_id, product, value) VALUES (5,4,"Computer",4500)')

# query_shopping = cursor.execute('SELECT clients.name, shopping.product, shopping.value FROM shopping JOIN clients ON shopping.client_id = clients.id')
# for shopping in query_shopping:
    #print(shopping)

students.commit()
students.close()

print("Database successfully updated!")