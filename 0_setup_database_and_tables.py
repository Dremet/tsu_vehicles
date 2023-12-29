import sqlite3

""" CREATES SQLITE DATABASE AND CREATES TABLES """
con = sqlite3.connect("vehicles.db")
cur = con.cursor()

with open("sql/ddl.sql", "r") as ddl:
    cur.executescript(ddl.read())
