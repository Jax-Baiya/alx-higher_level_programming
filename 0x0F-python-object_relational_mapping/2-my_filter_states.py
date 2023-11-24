#!/usr/bin/python3
'''
Contains a MySQLdb script that performs read operations on a database
It lists all states with a name starting with "N"
'''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db_location = 'localhost'
    port = 3306

    search = argv[4]
    db = MySQLdb.connect(host=db_location,
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=port)

    cursor = db.cursor()
    sql = """SELECT * FROM states
            WHERE BINARY name = '{}' ORDER BY id ASC""".format(search)

    cursor.execute(sql)
    data = cursor.fetchall()

    for row in data:
        print(row)

    db.close()
