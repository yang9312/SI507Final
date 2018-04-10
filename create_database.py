import sqlite3
import csv
import json

# create a database
DBNAME = 'esteelauder.db'

def init_db(db_name):
	conn = sqlite3.connect(db_name)
	cur = conn.cursor()

	statement = "DROP TABLE IF EXISTS 'Type'"
	cur.execute(statement)
	conn.commit()

	statement = "DROP TABLE IF EXISTS 'Category'"
	cur.execute(statement)
	conn.commit()

	statement = "DROP TABLE IF EXISTS 'Product'"
	cur.execute(statement)
	conn.commit()

	statement = "DROP TABLE IF EXISTS 'Review'"
	cur.execute(statement)
	conn.commit()

	statement = '''CREATE TABLE 'Type' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'Name' TEXT
        );
        '''
	cur.execute(statement)
	conn.commit()

	statement = '''CREATE TABLE 'Category' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'Name' TEXT,
        'Suptype' INTEGER
        );
        '''
	cur.execute(statement)
	conn.commit()

	statement = '''CREATE TABLE 'Product' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'ProductId' INTEGER,
        'PrimaryName' TEXT,
        'SubName' TEXT,
        'StarRating' TEXT,
        'ReviewCount' INTEGER,
        'SuptypeId' INTEGER,
        'SubtypeId' INTEGER
        );
        '''
	cur.execute(statement)
	conn.commit()

	statement = '''CREATE TABLE 'Review' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'NickName' TEXT,
        'SkinType' TEXT,
        'Age' TEXT,
        'UsingYear' TEXT,
        'Rating' TEXT,
        'ProductID' INTEGER
        );
        '''
	cur.execute(statement)
	conn.commit()

	conn.close()


if __name__=="__main__":
	init_db(DBNAME)