import sqlite3
from sqlite3 import Error

def full_delete(dbname):
    con = sqlite3.connect(dbname)
    curs = con.cursor()

    try:
        curs.execute("""
        DROP TABLE country
        """)

        curs.execute("""
        DROP TABLE year
        """)

        curs.execute("""
        DROP TABLE infant_mortality_rate
        """)

    except Error as e:
        print("failed to delete: {e}".format(e))


def init(dbname):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()

    try:
    ## create country 
        curs.execute("""
        CREATE TABLE IF NOT EXISTS country(
            country_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name STRING NOT NULL
        );
        """)

    ## create year table
        curs.execute("""
        CREATE TABLE IF NOT EXISTS year(
            year_id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER NOT NULL
        );
        """)

        curs.execute("""
        CREATE TABLE IF NOT EXISTS infant_mortality_rate( 
            imr_id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_id INTEGER NOT NULL, 
            year_id INTEGER NOT NULL,
            both REAL NOT NULL, 
            male REAL NOT NULL, 
            female REAL NOT NULL,
            both_b REAL NOT NULL, 
            both_c REAL NOT NULL,
            male_b REAL NOT NULL, 
            female_b REAL NOT NULL,
            FOREIGN KEY(country_id) REFERENCES country(country_id),
            FOREIGN KEY(year_id) REFERENCES year(year_id));
        """)

        print("Sucess")

    except Error as e:
        print("failed to init db tables: {}".format(e))


def main():
    print("SQLite3 database initialization")
    
    init("/home/matt/Documents/School/SENG474/SENG474Project/data/db.db")
    
    #full_delete("/home/matt/Documents/School/SENG474/SENG474Project/data/db.db")

if __name__ == '__main__':
    main()