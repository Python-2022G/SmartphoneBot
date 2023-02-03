from tinydb import TinyDB

db = TinyDB('db.json')


def get_tables():
    return db.tables()

def get_products(table_name: str) -> list[dict]:
    t = db.table(table_name)
    return t.all()

# print(get_products('Vivo'))