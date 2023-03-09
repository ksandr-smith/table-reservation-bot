import sqlite3


DB_NAME = "db.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


def close_db():
    connection.close()
