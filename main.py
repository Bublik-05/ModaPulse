import psycopg2  # если MySQL — меняем на pymysql + строку подключения
import pandas as pd

# --- параметры подключения ---
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fashion_store"
DB_USER = "postgres"
DB_PASSWORD = "ap112005"

# --- подключение к БД ---
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# --- читаем все запросы из queries.sql ---
with open("queries.sql", "r", encoding="utf-8") as f:
    raw_sql = f.read()

# разбиваем по ';' (оставляем только непустые)
queries = [q.strip() for q in raw_sql.split(';') if q.strip()]

# --- выполняем каждый запрос ---
for idx, query in enumerate(queries, start=1):
    print(f"\n===== Запрос {idx} =====")
    print(query)
    try:
        df = pd.read_sql_query(query, conn)
        print(df.head())  # вывод первых строк
        # Сохраняем каждый результат в CSV
        df.to_csv(f"query_{idx}.csv", index=False)
    except Exception as e:
        print(f"Ошибка при выполнении запроса {idx}: {e}")

conn.close()
print("\nВсе запросы выполнены. Результаты сохранены в CSV.")
