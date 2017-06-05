#!/usr/bin/env python2

import psycopg2

queries=["select title,hits from articleHits limit 3"]

def dbConnect():

    global database
    global dbCursor
    # error handling for connection to DB
    try:
        database = psycopg2.connect("dbname=news")
    except:
        print "Couldn't connect to DB"

    # initialized cursor to Db
    dbCursor = database.cursor()


def parseLog(query):
    dbCursor.execute(query)
    parsedData = dbCursor.fetchall()
    database.close()
    return parsedData

def dataOutput(parsedData):
    print parsedData['title']
    for data in parsedData['data']:
        print '\t'+str(data[0])+' => '+str(data[1])+' hits'


# connection call to DB
dbConnect()
query1 = dict()
query1['title']="The Top 3 Articles are :"
query1['data']=parseLog(queries[0])
dataOutput(query1)
