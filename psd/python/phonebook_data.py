import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
list_of_users = [
    (2, 'ABC', 'XYZ', 93983913848),
    (3, 'QPE', 'DJENN', 99187798488)
]
cursor.executemany("INSERT INTO names(id, firstname, lastname, phonenumber) VALUES(?,?,?,?)", list_of_users)
id = input('enter user id: ')
fname = input('enter user first name : ')
lname = input('enter user last name : ')
phonenumber = input('enter user phone nmber: ')
cursor.execute("INSERT INTO names(id, firstname, lastname, phonenumber) VALUES(?,?,?,?)", (id, fname, lname, phonenumber))
conn.commit()
cursor.execute("select * From names;")
for user in cursor.fetchall():
    print(user)
conn.close()
