#!/usr/bin/env python2

import psycopg2

queries=["select title,hits from articleHits limit 3",
        "select name,sum(articleHits.hits) as num from authors, articleHits where authors.id = articleHits.author group by name order by num desc;",
        """select currentDate, round(errorCount*100.0/(okCount+errorCount),2)
           as errorprc
           from(
           select date(time) as currentDate,
           sum(case when status='200 OK' then 1 else 0 END) as okCount,
           sum(case when status='404 NOT FOUND' then 1 else 0 END) as errorCount
           from log group by date(time)
           ) as derived_table where errorCount*100/(okCount+errorCount)>1"""]

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
    return parsedData

def dataOutput(parsedData):
    print parsedData['title']
    for data in parsedData['data']:
        print '\t~ '+str(data[0])+' => '+str(data[1])+' hits'

def dataOutputError(parsedData):
    print parsedData['title']
    for data in parsedData['data']:
        print '\t~ '+str(data[0])+' => '+str(data[1])+' %'


# connection call to DB
dbConnect()
# fetches top articles
topArticles = {'title':"The Top 3 Articles are :", 'data':parseLog(queries[0])}

# fetches top authors
topAuthors = {'title':"Top Authors are :", 'data':parseLog(queries[1])}

# fetches error days
errorDays = {'title':"Days with more than 1 percent error are :", 'data':parseLog(queries[2])}

# Output
dataOutput(topArticles)
dataOutput(topAuthors)
dataOutputError(errorDays)
database.close()
