import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
list_of_new_students = [
    (999, "ABC", "Java", 5),
    (991, "CDE", "Python", 3),
    (992, "FGH", "Python", 7),
    (993, "IJK", "Java", 4)
]
cursor.executemany("""
    INSERT INTO students(id, name, class, grade) VALUES(?,?,?,?)
""", list_of_new_students)
# conn.commit()
id_input = input("Enter id to search : ")
cursor.execute("SELECT * FROM students WHERE id = ?", [id_input])
rows = cursor.fetchall()
for row in rows:
    print(row)
# conn.close()

new_cursor = conn.cursor()
id_to_delete = input("Enter id to delete : ")
new_cursor.execute("DELETE FROM students where id = ?", [id_to_delete])
conn.commit()
conn.close()
# dropping the students table
# new_cursor.execute('DROP TABLE IF EXISTS students;')
