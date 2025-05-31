import mysql.connector
import sqlite3
import psycopg2
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
user_data = {
    'name': "John",
    'age': 32,
    'phone': 568567898,
}
# cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, phone INTEGER, UNIQUE(phone))')

cursor.execute('INSERT INTO users (name, age, phone) VALUES (?, ?, ?)', (
    user_data['name'], user_data['age'], user_data['phone'])
               )
conn.commit()
# some = cursor.execute('SELECT * FROM users WHERE age > ?', (30,)).fetchall()
# conn.commit()
# conn.close()
#
#
# class MySql:
#     conn = mysql.connector.connect(host='localhost', user='root', password='some', database='your_db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users')
#     conn.commit()
#     conn.close()
#
#
# class PostgresSql:
#     conn = psycopg2.connect(host='localhost', user='root', password='some', database='your_db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users')
#     conn.commit()
#     conn.close()


# class SqlAlchemy:
engine = create_engine('sqlite:///example.db')
conn = engine.connect()

metadata = MetaData()
patient = Table('patient', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                )
metadata.create_all(engine)
print([row for row in conn.execute(patient.select())])
