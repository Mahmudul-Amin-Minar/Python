import sqlite3

def create_table():
    # create connection to the database file if there is no file then it will create one
    conn = sqlite3.connect("lite.db")

    # create cursor for that connection
    curr = conn.cursor()

    # sql query to create a table named store if table is not exist
    curr.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # commit those changes
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()

    # using ? mark placeholder to insert data
    curr.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price)) 
    conn.commit()
    conn.close()

# insert_data("Coffe cups", 10, 5)

def view():
    conn = sqlite3.connect("lite.db")
    
    curr = conn.cursor()
    curr.execute("SELECT * FROM store")

    # fetch all the data from the database file
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    
    curr = conn.cursor()

    # query selection for which item to delete
    curr.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    curr.close()


def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    
    curr = conn.cursor()
    # query selection for which item to update
    curr.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    curr.close()

update(11,6,'Coffe cups')

# delete("wine GLass")
print(view())
