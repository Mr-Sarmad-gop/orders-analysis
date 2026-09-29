import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
)
""")

# Sample data: 6 customers
customers = [
    ("Alice", "Lahore"),
    ("Bob", "Karachi"),
    ("Charlie", "Islamabad"),
    ("Diana", "Lahore"),
    ("Edward", "Karachi"),
    ("Fiona", "Peshawar")
]

# Sample data: 10 orders
orders = [
    (1, 6500.0), # Alice
    (1, 4200.0), # Alice
    (2, 7500.0), # Bob
    (2, 8000.0), # Bob
    (3, 3000.0), # Charlie
    (4, 9000.0), # Diana
    (4, 5500.0), # Diana
    (5, 2000.0), # Edward
    (5, 1500.0), # Edward
    (6, 4500.0)  # Fiona
]

cursor.executemany("INSERT INTO customers (name, city) VALUES (?, ?)", customers)
cursor.executemany("INSERT INTO orders (customer_id, amount) VALUES (?, ?)", orders)

conn.commit()
conn.close()

print("Database 'orders.db' created and populated successfully.")