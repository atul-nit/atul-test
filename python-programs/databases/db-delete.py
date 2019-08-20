import sqlite3

conn = sqlite3.connect('test1.db')
print ("Opened database successfully")

del_query = '''DELETE FROM COMPANY WHERE ID=1'''
conn.execute(del_query)
conn.commit()
conn.close()