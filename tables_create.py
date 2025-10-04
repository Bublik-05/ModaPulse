import psycopg2
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Пример одной таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    brand TEXT,
    category TEXT,
    catalog_price NUMERIC,
    cost_price NUMERIC
);
""")

print("✅ Таблицы успешно созданы (если их не было).")

conn.commit()
cur.close()
conn.close()
