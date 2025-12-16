from db import get_connection


def add_product(name, price, quantity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )

    conn.commit()
    conn.close()


def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, price, quantity FROM products")
    products = cursor.fetchall()

    conn.close()
    return products
