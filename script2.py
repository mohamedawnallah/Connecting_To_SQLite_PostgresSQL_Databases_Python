import psycopg2 as pg2
from db_credentials import *
def create_table():
    conn = pg2.connect(f"dbname='database1' user={username} password={password} host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF  NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = pg2.connect(f"dbname='database1' user={username} password={password} host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price) )
    conn.commit()
    conn.close()


def view():
    conn = pg2.connect(f"dbname='database1' user={username} password={password} host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = pg2.connect(f"dbname='database1' user={username} password={password} host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()


def update(item,quantity,price,):
    conn = pg2.connect(f"dbname='database1' user={username} password={password} host='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()
create_table()
update('Apple',55,25)
print(view())
