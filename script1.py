import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF  NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect('lite.db')
    curr = conn.cursor()
    curr.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    curr = conn.cursor()
    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect('lite.db')
    curr = conn.cursor()
    curr.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(item,quantity,price,):
    conn = sqlite3.connect('lite.db')
    curr = conn.cursor()
    curr.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

update('Fruits Glass',20,20)
delete("Water Glass")
print(view())