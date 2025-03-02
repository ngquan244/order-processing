import sqlite3
import random

DB_PATH = "server/orders.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_code TEXT UNIQUE,
        price REAL
    )
    """)

    cursor.execute("DELETE FROM orders")

    products = [(f'P{str(i).zfill(4)}', round(random.uniform(10, 1000), 2)) for i in range(1, 1001)]
    cursor.executemany("INSERT INTO orders (product_code, price) VALUES (?, ?)", products)

    conn.commit()
    conn.close()
    print("Database đã khởi tạo thành công với 1000 sản phẩm!")

if __name__ == "__main__":
    init_db()
