import psycopg2 
import pandas as pd

# --- параметры подключения ---
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fashion_store"
DB_USER = "postgres"
DB_PASSWORD = "ap112005"

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

with open("queries1.sql", "r", encoding="utf-8") as f:
    raw_sql = f.read()


queries = [q.strip() for q in raw_sql.split(';') if q.strip()]


for idx, query in enumerate(queries, start=1):
    print(f"\n===== Запрос {idx} =====")
    print(query)
    try:
        df = pd.read_sql_query(query, conn)
        print(df.head())  
    except Exception as e:
        print(f"Ошибка при выполнении запроса {idx}: {e}")

conn.close()
print("\nВсе запросы выполнены. Результаты сохранены в CSV.")




