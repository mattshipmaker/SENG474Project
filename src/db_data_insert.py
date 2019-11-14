import sqlite3
from sqlite3 import Error
import csv
import db

def get_year_id(years, year):
    for (x,y) in years:
        if int(y) == int(year):
            return x

def get_country_id(countries, country):
    for(x,y) in countries:
        if y == country:
            return x

def md():

    con, cur = db.get_connection()

    cur.execute("SELECT * FROM year")
    y = cur.fetchall()

    cur.execute("SELECT * FROM country")
    c = cur.fetchall()

    yy = [2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]

    with open("../data/MalariaDeaths.csv", newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            country = row[0]
            yyy = zip(yy, row[1:])

            for q in yyy:
                year = q[0]
                data = q[1].split('[')[0].replace(' ','')

                year_id = get_year_id(y, year)
                country_id = get_country_id(c, country)

                if country_id is not None:
                    cur.execute(""" 
                    INSERT INTO malaria_deaths(country_id, year_id, deaths)
                    VALUES(?, ?, ?)
                    """,(country_id, year_id, data))
                    
    con.commit()

def imr():

    con, curs = db.get_connection()

    curs.execute("SELECT * FROM year")
    y = curs.fetchall()

    curs.execute("SELECT * FROM country")
    c = curs.fetchall()

    with open("../data/InfantMortalityRate.csv", newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            country = row[0]
            
            year = row[1]
            both = row[2]
            male = row[3]
            female = row[4]
            both_b = row[5]
            both_c = row[6]
            male_c = row[7]
            female_c = row[8]

            year_id = get_year_id(y, year)
            country_id = get_country_id(c, country)

            if(year_id == None or country_id == None):
                print(country, year, country_id, year_id)
            else:
                curs.execute("""INSERT INTO 
                infant_mortality_rate(country_id, year_id, both, male, female, both_b, both_c, male_c, female_c)
                VALUES(?,?,?,?,?,?,?,?,?)
                """, (country_id, year_id, both, male, female, both_b, both_c, male_c, female_c))
    con.commit()

def year():
    con = None
    try:
        con, curs = db.get_connection()

        years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
        i = 0
        for year in years:
            curs.execute("""
            INSERT INTO year(year_id, year) values(?,?)
            """, (i,year))
            i = i + 1

    except Error as e:
        print("failed to insert years: {}".format(e))
    finally:
        con.commit()
        con.close()

def country():
    rows = []
    with open("../data/countries.csv") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for r in row:
                rows.append(r.split("|")[1])

    con = None
    try:
        con, curs = db.get_connection()
        i = 0
        for r in rows:
            curs.execute("INSERT INTO country(country_id, name) VALUES(?,?) ", (i,r))
            curs.lastrowid
            i = i + 1
    except Error as e:
        print("failed to insert countries: {}".format(e))
    finally:
        con.commit()
        con.close()

def main():
    print("for reading csv -> insert into db")
    #country()
    #year()
    #imr()
    #md()

if __name__ == "__main__":
    main()