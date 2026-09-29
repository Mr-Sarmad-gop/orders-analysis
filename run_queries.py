import sqlite3

def run_and_print(cursor, title, query):
    print(f"=== {title} ===")
    print(f"SQL:\n{query.strip()}\n")
    cursor.execute(query)
    rows = cursor.fetchall()
    
    col_names = [desc[0] for desc in cursor.description]
    print(" | ".join(col_names))
    print("-" * 45)
    
    for row in rows:
        print(" | ".join(str(val) for val in row))
    print("\n")

def main():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    # Query (a): INNER JOIN - customer name and order amount
    query_a = """
    SELECT c.name, o.amount
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id;
    """
    run_and_print(cursor, "Query (a): Customer Name and Order Amounts (INNER JOIN)", query_a)

    # Query (b): GROUP BY - total amount spent per customer sorted descending
    query_b = """
    SELECT c.name, SUM(o.amount) AS total_spent
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
    ORDER BY total_spent DESC;
    """
    run_and_print(cursor, "Query (b): Total Amount Spent per Customer (GROUP BY + SUM)", query_b)

    # Query (c): GROUP BY + HAVING - cities with average order amount > Rs. 5000
    query_c = """
    SELECT c.city, AVG(o.amount) AS avg_order_amount
    FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.city
    HAVING AVG(o.amount) > 5000;
    """
    run_and_print(cursor, "Query (c): Cities with Average Order > Rs. 5000 (GROUP BY + HAVING)", query_c)

    conn.close()

if __name__ == "__main__":
    main()