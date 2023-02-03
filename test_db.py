from tinydb import TinyDB

db = TinyDB('testDB.json', indent=4)

print(db.tables())



