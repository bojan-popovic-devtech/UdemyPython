import sqlite3

conn = sqlite3.connect("contacts.sqlite")

find_name = input("PLease enter name: ")
find_sql = "SELECT * FROM contacts WHERE name = ?"

find_cursor = conn.cursor()
find_cursor.execute(find_sql, (find_name,)) # When passing single tuple you need to pass 2 parameters, second empty

for row in find_cursor:
    print(row)

find_cursor.close()
conn.close()