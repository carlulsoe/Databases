import mysql.connector
import random
'''
This creates the database elements for assignment 0 of databases.
'''


def drinksStore(mysqldb, store):
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT code from db19.beverage")
    codes = mycursor.fetchall()
    print(codes)
    sql = "INSERT INTO sells VALUES ('{}', {}, {})"
    for i in store:
        for j in codes:
            print(sql.format(i, j, random.randint(5, 50)))
            mycursor.execute(sql.format(i, j[0], random.randint(5, 50)))
            mysqldb.commit()


def insertStore(sqlDB, store):
    mycursor = sqlDB.cursor()
    sql = "INSERT INTO store VALUES ('{}', {}, {})"

    for s in store:
        mycursor.execute(sql.format(s, random.randint(1000, 9999), random.randint(100000, 999999)))
        mysqldb.commit()



def insertDrinks(sqlDB):
    mycursor = sqlDB.cursor()
    sql = "INSERT INTO beverage VALUES ({}, '{}', '{}')"
    size = ["small", "medium", "large", "grande"]

    i = 1
    while i < 20:

        drink = str(input("new drink:"))
        print(drink)
        for j in size:
            mycursor.execute(sql.format(i, drink, j))
            sqlDB.commit()
            i += 1

if __name__ == '__main__':
    store = ["Fakta", "Netto", "Føtex", "Kvikly", "Meny"]
    mysqldb = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="password",
                                      database="db19"
                                      )
    insertDrinks(mysqldb)
    insertStore(mysqldb, store)
    drinksStore(mysqldb, store)
