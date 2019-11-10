import sqlite3

db_name = "../data/db.db"

def get_malaria_deaths():
    con, cur = get_connection()
    cur.execute("""SELECT * FROM malaria_deaths """)
    return cur.fetchall()

def get_imr():
    con, cur = get_connection()
    cur.execute("""SELECT * FROM infant_mortality_rate """)
    return cur.fetchall()

def get_countries():
    con, cur = get_connection()
    cur.execute("""SELECT * FROM COUNTRY """)
    return cur.fetchall()

def get_country(id):
    con, cur = get_connection()
    cur.execute("""SELECT name FROM country WHERE country_id = ? """,(id))
    return cur.fetchall()

def get_years():
    con, cur = get_connection()
    cur.execute("""SELECT * FROM YEAR """)
    return cur.fetchall()

def get_connection():
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    return con, cur

def main():
    print("database")

if __name__ == "__main__":
    main()