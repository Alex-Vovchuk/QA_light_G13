import sqlite3

import pytest


@pytest.fixture(scope='session')
def get_connection():
    file_path = 'C:\\Users\\papka\\Documents\\workspace\\QA_light_G13\\src\\'
    conn = sqlite3.connect(file_path + 'example.db')
    yield conn
    conn.close()


@pytest.fixture
def delete_user(get_connection):
    def _inner_function(phone_number):
        conn = get_connection
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE phone = ?', (phone_number,))
        conn.commit()
    return _inner_function
