import sqlite3

conn = sqlite3.connect('test1.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
all_records = cursor.fetchall()
if len(all_records) > 1:
   print("-----  %d RECORD FOUND  ------" % len(all_records))
   for row in all_records:
      print ("ID = ", row[0], end="  ")
      print ("NAME = ", row[1], end="  ")
      print ("ADDRESS = ", row[2], end="  ")
      print ("SALARY = ", row[3])
else:
   print("No Record Found!!!")

print ("Operation done successfully")
conn.close()