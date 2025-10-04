import psycopg2
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE DATABASE fashion_store;")
print("✅ База данных 'fashion_store' создана (если её не было).")

cur.close()
conn.close()
