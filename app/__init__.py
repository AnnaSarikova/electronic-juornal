from flask import Flask
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS ListOfStudents(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')
conn.commit()

from app import routes
