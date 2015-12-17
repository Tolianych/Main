#   -*- coding: utf-8 -*-
'''
Created on Dec 17, 2015
@author: tolianych

'''
import requests
import Tkinter
import tkMessageBox
import json
import SendKeys

YANDEX_REQUEST = "https://dictionary.yandex.net/dicservice.json/lookup?ui=ru&srv=tr-text&sid=278611de.5699fa2a.f7fade92&text=%s&lang=en-ru&flags=5"


class Translator(object):

    def __init__(self, untranslated, request):
        self.untranslated = untranslated
        self.request = request

    def getWebResponse(self):
        resp = requests.get(self.request % self.untranslated)
        self.response = resp.content
#         print 'Response:', self.response

    def parseYaResponse(self):
        respToDict = json.loads(self.response)
        self.transList = respToDict['def'][0]['tr']
        self.transcription = respToDict['def'][0]['ts']

    def formatResult(self):
        formatedTranslations = ''
        for trans in self.transList:
            formatedTranslations += '    %s\n' % trans['text']
        return '%s\n%s\n%s' % (self.untranslated, self.transcription, formatedTranslations)

    def showPopup(self, text, title="Translated!"):
        window = Tkinter.Tk()
        window.wm_withdraw()
        window.geometry("1x1+" + str(window.winfo_screenwidth() / 2) + "+" + str(window.winfo_screenheight() / 2))
        tkMessageBox.showinfo(title, message=text)

    def main(self):
        self.getWebResponse()
        self.parseYaResponse()
        translation = self.formatResult()
        self.showPopup(translation)

if __name__ == '__main__':
    SendKeys.SendKeys('^C')
    root = Tkinter.Tk()
    root.withdraw()
    untranslated = root.clipboard_get()
    t = Translator(untranslated, YANDEX_REQUEST)
    t.main()
