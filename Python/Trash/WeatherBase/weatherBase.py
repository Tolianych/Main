# -*- coding: utf-8 -*-
import sqlite3 as lite
import matplotlib
import os
import urllib2
import zipfile


URL = 'http://pogoda.by/zip-avia/{0}/26851_{1}.zip'
YEARS = ('2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016')
MONTHS = xrange(1, 13)

selectMonth = "SELECT Date, T FROM Weather WHERE Date > '2011-01-01' AND Date LIKE '201_-02-__-15:00'"

class PogodaByParcer(object):

    def __init__(self):
        self.zipName = None
        self.csvName = None
        self.monthTempData = []

    def downloadZip(self, url):
        try:
            usock = urllib2.urlopen(url)
        except:
            print 'Exception occured while downloading %s' % url
            raise
        zipFileData = usock.read()
        self.zipName = os.path.basename(url)
        with open(self.zipName, 'wb') as f:
            f.write(zipFileData)
        usock.close()

    def unzipArchive(self):
        zipData = zipfile.ZipFile(self.zipName)
        self.csvName = zipData.namelist().pop()
        zipData.extract(self.csvName, path=None)
        os.unlink(self.zipName)

    def parceCsv(self):
        with open(self.csvName, 'r') as c:
            csv = c.readlines()
        os.unlink(self.csvName)
        for line in csv:
            dataLine = line.split(';')
            if dataLine[1] in ('03:00', '09:00', '15:00', '21:00'):
                dateString = '{}-{:02d}-{:02d}-{}'.format(self.csvName.split('-')[0][-4:],
                                                          int(self.csvName.split('-')[1][:-4]),
                                                          int(dataLine[0]),
                                                          dataLine[1])
                self.monthTempData.append((dateString,
                                           dataLine[2].lstrip('+'),  # Temperature
                                           dataLine[5],              # Weather phenomena
                                           dataLine[6],              # Cloudiness
                                           str(int(int(dataLine[9]) * 0.75006375541921)) if dataLine[9] else '1025'))  # Pressure (1 hPa = 0.75006375541921 mmHg)
        return self.monthTempData


class DbConnector(object):

    def __init__(self, dbName):
        self.con = None
        self.cur = None
        self.dbName = dbName

    def connect(self):
        try:
            self.con = lite.connect(self.dbName)
            self.cur = self.con.cursor()
            self.cur.execute('SELECT SQLITE_VERSION()')
            data = self.cur.fetchone()
            print "SQLite version: %s" % data
        except lite.Error, e:
            print "Error %s:" % e.args[0]

    def createTableWeather(self):
        self.cur.execute("CREATE TABLE Weather (Date TEXT, T INT, Phenomena TEXT, Cloudness INT, Pressure INT);")

    def fillRow(self, date, temp, phenomena, cloudness, pressure):
        sql = "INSERT INTO Weather VALUES ('{0}', {1}, '{2}', {3}, {4});".format(date, temp or '0', phenomena or 'N', cloudness or 'NULL', pressure)
        # print sql
        try:
            self.cur.execute(sql)
        except:
            print 'Error oqqured while trying to do "%s"' % sql
            raise

    def getRows(self):
        print 'start'
        self.cur.execute("SELECT * FROM Weather")
        rows = self.cur.fetchall()
        for row in rows:
            print row
        print 'Finish!'

    def __del__(self):
        if self.con:
            self.con.commit()
            self.con.close()

def getMonthData(url):
    parcer = PogodaByParcer()
    parcer.downloadZip(url)
    parcer.unzipArchive()
    return parcer.parceCsv()

def insertIntoDb(dbName, monthData):
    c = DbConnector(dbName)
    c.connect()
    c.createTableWeather()
    for dayWeather in monthData:
        c.fillRow(*dayWeather)

if __name__ == '__main__':
    # url = URL.format('2016', '2016-2')
    # monthData = getMonthData(url)
    # print monthData

    c = DbConnector('weather.db')
    c.connect()
    c.createTableWeather()
    for y in YEARS:
        print 'Starting to process year %s' % y
        for m in MONTHS:
            url = URL.format(y, '%s-%s' % (y, str(m)))
            monthData = getMonthData(url)
            for dayWeather in monthData:
                c.fillRow(*dayWeather)

    # c = DbConnector('weather.db')
    # c.connect()
    # c.getRows()


    # insertIntoDb('weather.db', monthData)
