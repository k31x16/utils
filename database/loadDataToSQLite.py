import sqlite3
import csv
import glob
import os


class loadDataToSQLite:

    def __init__(self, path_input_files, path_database):
        self.path_input_files = path_input_files
        self.path_database = path_database

    def load_data(self):
        os.chdir(self.path_input_files)
        conn = sqlite3.connect(self.path_database)
        cursor = conn.cursor()
        csv_files = glob.glob('*.csv') # Get list files
        for file in csv_files:
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                print(file)
                create_table = f"CREATE TABLE IF NOT EXISTS {file.replace('.csv', '')} ({', '.join(header)})"
                cursor.execute(create_table)
                insert_query = f"INSERT INTO yandex VALUES ({', '.join(['?'] * len(header))})"
                cursor.executemany(insert_query, reader)
        conn.commit()
        conn.close()