# -*- coding: utf-8 -*-
import sqlite3 as lite
import os
import urllib2
import zipfile


URL = 'http://pogoda.by/zip-avia/{0}/26851_{1}.zip'

class PogodaByParcer(object):

    def __init__(self):
        self.zipName = None
        self.csvName = None
        self.monthTempData = {}

    def downloadZip(self, url):
        usock = urllib2.urlopen(url)
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
                dateString = '{}-{:02d}-{:02d}'.format(self.csvName.split('-')[0][-4:],
                                                       int(self.csvName.split('-')[1][:-4]),
                                                       int(dataLine[0]))
                if dateString not in self.monthTempData.iterkeys():
                    self.monthTempData[dateString] = {}
                self.monthTempData[dateString][dataLine[1]] = dataLine[2].lstrip('+')
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
        self.cur.execute("CREATE TABLE Weather (Date TEXT, N INT, M INT, D INT, E INT)")

    def fillRow(self, date, nightTemp, morningTemp, dayTemp, eveningTemp):
        self.cur.execute("INSERT INTO Weather VALUES ({0}, {1}, {2}, {3}, {4});".format(date, nightTemp, morningTemp, dayTemp, eveningTemp))

    def __del__(self):
        if self.con:
            self.con.close()

def getMonthData(url):
    parcer = PogodaByParcer()
    parcer.downloadZip(url)
    parcer.unzipArchive()
    return parcer.parceCsv()

if __name__ == '__main__':
    url = URL.format('2016', '2016-2')
    monthData = getMonthData(url)
    print monthData
    # c = DbConnector('weather.db')
    # c.connect()
