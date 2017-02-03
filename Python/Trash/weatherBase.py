# -*- coding: utf-8 -*-
import os
import urllib2
import zipfile

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
                if dataLine[0] not in self.monthTempData.iterkeys():
                    self.monthTempData[dataLine[0]] = {}
                self.monthTempData[dataLine[0]][dataLine[1]] = dataLine[2].lstrip('+')
        return self.monthTempData

if __name__ == '__main__':
    parcer = PogodaByParcer()
    arch = parcer.downloadZip('http://pogoda.by/zip-avia/2016/26851_2016-2.zip')
    parcer.unzipArchive()
    print parcer.parceCsv()
