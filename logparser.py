#!/usr/bin/env python2


import psycopg2

def dbConnect():
    #error handling for connection to DB
    try:
        database = psycopg2.connect("dbname=news")
    else:
        "Couldn't connect to DB"

    #initialized cursor to Db
    dbCursor = database.cursor()


def parseLog(query):
    dbCursor.execute(query)
    parsedData = dbCursor.fetchall()
    database.close()
    return parsedData

#connection call to DB
dbConnect()
