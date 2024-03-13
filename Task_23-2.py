'''Напишите программу, которая считывает информацию из
таблицы book и печатает ее в виде таблицы, соответствующей
таблице из базы данных (заголовки и строки данных).'''

import psycopg2

conn = psycopg2.connect(
    dbname='XXXXX',
    user='YYYY',
    password='******',
    host='secret'
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Book")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

print('|'.join(columns))

for row in rows:
    print('|'.join(str(cell) for cell in row))

conn.close()