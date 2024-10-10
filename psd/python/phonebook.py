import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS names(
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        phonenumber TEXT NOT NULL
    );
""")

cursor.execute("""
    INSERT INTO names(id, firstname, lastname, phonenumber) VALUES
    (1, 'Ayush', 'Agarwal', 881818181);
""")
conn.commit()

cursor.execute('SELECT * FROM names;')
for row in cursor.fetchall():
    print(row)
conn.close()