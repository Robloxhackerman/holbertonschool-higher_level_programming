#!/usr/bin/python3
"""Python Module"""
import MySQLdb
from sys import argv


"""SQL Query"""
if __name__ == "__main__":
    dataB = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
        )

    cursor = dataB.cursor()
    cursor.execute("SELECT cit.name FROM cities cit \
        LEFT JOIN states st ON cit.st_id = s.id \
        WHERE s.name = %s \
        ORDER BY c.id", (argv[4], ))
    result = cursor.fetchall()
    for i, record in enumerate(result):
        if i > 0:
            print(', ', end='')
        print(str(record[0]), end='')
    print()
    cursor.close()
    dataB.close()
