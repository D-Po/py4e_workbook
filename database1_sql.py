# 12.07.2021
# py4e
# Section 15.4 Creating a database table
# The code to create a database file and a table named Tracks with
# two columns in the database is as follows:

# SQL

import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()
