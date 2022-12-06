#!/usr/bin/python3
"""aaaaa"""
import MySQLdb
from sys import argv


"""aaaaa"""
if __name__ == "__main__":
    dataB = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
        )
    cursor = dataB.cursor()
    cursor.execute('''SELECT * FROM states WHERE name LIKE "{}"
            ORDER BY states.id ASC;'''.format(argv[4]))
    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
