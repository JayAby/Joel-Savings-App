# Creating the database

import sqlite3

db = sqlite3.connect('AddNewRec.db')
try:
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE addNew (
    sid INTEGER PRIMARY KEY AUTOINCREMENT,
    amountreceived DOUBLE,
    tithe DOUBLE,
    accommodation DOUBLE,
    fees DOUBLE,
    transport DOUBLE,
    bills DOUBLE,
    save DOUBLE,
    balance DOUBLE,
    date VARCHAR(12));''')

    db.commit()
    print('table(s) created successfully')
except:
    print('Error in table creation sql operation')
db.close()
