#!/usr/bin/python3
"""aaaa"""
import MySQLdb
from sys import argv


"""aaaa"""
if __name__ == "__main__":
    dataB = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = dataB.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    result = cursor.fetchall()

    for row in result:
        print(row)