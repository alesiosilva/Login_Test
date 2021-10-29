# Database SQL

import sqlite3 as sql

conn = sql.connect('Users.db')
cursor = conn.cursor()

try: 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS UserLogins (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        Name TEXT NOT NULL, 
        Email TEXT NOT NULL, 
        User TEXT NOT NULL, 
        Password TEXT NOT NULL)'''
    )
    print('connected!')
except:
    print('error to connect on database!')

