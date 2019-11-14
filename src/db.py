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
    return cur.fetchone()

def get_country_data(id):
    con, cur = get_connection()
    cur.execute(""" 
    SELECT c.name, y.year, imr.both, imr.male, imr.female, imr.both_b, imr.both_c, imr.male_c, imr.female_c 
    FROM country c 
    JOIN infant_mortality_rate imr ON imr.country_id = c.country_id 
    JOIN year y on y.year_id = imr.year_id
    WHERE c.country_id = ?;
    """, (id))
    return cur.fetchall()

def get_country_data_by_year(id, year):
    con, cur = get_connection()
    cur.execute(""" 
    SELECT imr.both, imr.male, imr.female, imr.both_b, imr.both_c, imr.male_c, imr.female_c 
    FROM country c 
    JOIN infant_mortality_rate imr ON imr.country_id = c.country_id 
    JOIN year y on y.year_id = imr.year_id
    WHERE c.country_id = ? AND y.year = ?;
    """, (id, year))
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