#!/usr/bin/env python2


import psycopg2

def parseLog(query):
    database = psycopg2.connect("dbname=news")
    dbCursor = database.cursor()
    dbCursor.execute(query)
    parsedData = dbCursor.fetchall()
    database.close()
    return parsedData
