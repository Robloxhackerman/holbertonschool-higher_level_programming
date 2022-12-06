#!/usr/bin/python3
"""Python Module"""
import MySQLdb
from sys import argv


"""SQL Query"""
if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Error")

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities \
                    JOIN states ON  cities.state_id = states.id WHERE \
                    BINARY states.name = %s""", (argv[4],))
    cont = cursor.fetchall()

    for i in cont:
        for j in i:
            if i == cont[0]:
                print(j, end='')
            else:
                print(f", {j}", end='')
    print()
    cursor.close()
    db.close()
