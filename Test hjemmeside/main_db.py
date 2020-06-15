from flask import g
import sqlite3

class MainData():

    def __init__(self):
        self.DATABASE = "database.db"

        self.create_db_tables()

    def _get_db(self):
        db = g.get('_database', None)
        if db == None:
            db = g._database = sqlite3.connect(self.DATABASE)
        return db

    def close_connection(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def register_user(self, user, pw, email):
        db = self._get_db()
        

    def _create_db_tables(self):
        db = self._get_db()
        c = db.cursor()
        try:
            c.execute("""CREATE TABLE users (
                id INTERGER PRIMATY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT
                password TEXT);""")
        except Exception as e:
            print(e)

        try:
            c.execute("""CREATE TABLE Energydrinks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                energy_drink TEXT,
                userid INTEGER,
                user_number_drinken INTEGER);""")
        except Exception as e:
            print(e)
        
        db.commit()
        return 'Database tables created'