import sqlite3

db = sqlite3.connect('AddNewRec.db')

viewquery = "SELECT * FROM addnew;"
removequery = "DELETE FROM addnew;"

cursor = db.cursor()
# cursor.execute(viewquery)

while True:
    record = cursor.fetchone()
    if record is None:
        break
    print(record)

# Uncomment the line below to delete all records
cursor.execute(removequery)

db.commit()  # Commit changes after deletion
db.close()
