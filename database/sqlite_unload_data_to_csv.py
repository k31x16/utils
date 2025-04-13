import sqlite3
import csv
import os


def export_all_tables_to_csv(db_path, output_folder='csv_output'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    os.makedirs(output_folder, exist_ok=True)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        output_file = os.path.join(output_folder, f"{table_name}.csv")
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(column_names)  # Записываем заголовки
            writer.writerows(rows)  # Записываем данные
        print(f"Table {table_name} export in {output_file}")
    conn.close()

database_path = 'myDB.db'
export_all_tables_to_csv(database_path)