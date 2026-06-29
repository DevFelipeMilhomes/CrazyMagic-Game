import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS dados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            time INTEGER NOT NULL,
            date TEXT NOT NULL
            )
        ''')

    def save(self, ranking_dict: dict):
        self.connection.execute('INSERT INTO dados (name,time,date) VALUES (:name, :time, :date)', ranking_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY time ASC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()

    def drop_table(self):
        self.connection.execute('DROP TABLE dados')