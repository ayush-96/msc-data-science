import sqlite3

with sqlite3.connect("company.db") as db:
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            class TEXT NOT NULL,
            grade INTEGER
        );
    """)
    cursor.execute("""
        INSERT INTO students(id, name, class, grade) VALUES
        (123, 'Mary', 'Python', 8)
    """)
    db.commit()
    cursor.execute("SELECT * FROM students;")
    print(cursor.fetchall())
    # db.close()

conn = sqlite3.connect('company.db')
new_cursor = conn.cursor()
newId = input("Enter ID : ")
name = input("Enter name : ")
newclass = input("Enter class : ")
newgrade = input("Enter grade : ")
new_cursor.execute("""
    INSERT INTO students VALUES(?,?,?,?)
""", (newId, name, newclass, newgrade))
conn.commit()
new_cursor.execute("SELECT * FROM students;")
for x in new_cursor.fetchall():
    print(x)
conn.close()
