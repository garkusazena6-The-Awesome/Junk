import sqlite3
connection = sqlite3.connect('DB.sl3')
cursor = connection.cursor()
"""
cursor.execute('''CREATE TABLE IF NOT EXISTS first_table (name Text);''')
#cursor.execute("INSERT INTO first_table (name) VALUES ('Vanya');")
cursor.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
cursor.execute("UPDATE first_table SET name='Dmitro' WHERE name='Oleksiy';")
cursor.execute("UPDATE first_table SET name='Glib' WHERE rowid=4;")
cursor.execute("DELETE FROM first_table WHERE rowid=5;")
"""
cursor.execute("DROP TABLE first_table;")
connection.commit()
res=cursor.fetchall()
print(res)
connection.close()