import sqlite3

# Open a database and create a table
conn = sqlite3.connect('test1.db')
print ("Opened database successfully")
create_table_query = '''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);'''
conn.execute(create_table_query)
# # conn.execute('''CREATE TABLE COMPANY
# #          (ID INT PRIMARY KEY     NOT NULL,
# #          NAME           TEXT    NOT NULL,
# #          AGE            INT     NOT NULL,
# #          ADDRESS        CHAR(50),
# #          SALARY         REAL);''')
# print ("Table created successfully")
conn.commit()

conn.close()