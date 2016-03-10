#   -*- coding: utf-8 -*-
'''
Created on Dec 17, 2015
@author: tolianych

'''
import requests
import time
import Tkinter
import tkMessageBox
import json
import virtkey

YANDEX_REQUEST = "https://dictionary.yandex.net/dicservice.json/lookup?ui=ru&srv=tr-text&sid=73bfeb1b.56a36fea.18f746bf&text=%s&lang=en-ru&flags=23"

#                   https://dictionary.yandex.net/dicservice.json/lookup?ui=ru&srv=tr-text&sid=3de82f55.56893e8d.27ba3f07&text=car&lang=en-en&flags=7


class Translator(object):

    def __init__(self, untranslated):
        self.untranslated = untranslated

    def getWebResponse(self):
        if ' ' in untranslated:
            self.isSentense = True
            resp = requests.post("https://translate.yandex.net/api/v1/tr.json/translate",
                                 headers={'content-type': 'application/x-www-form-urlencoded'},
                                 data={'id':'73bfeb1b.56a36fea.18f746bf-10-0', 'srv': 'tr-text', 'text': self.untranslated, 'lang': 'en-ru'})
        else:
            self.isSentense = False
            resp = requests.get(YANDEX_REQUEST % self.untranslated)
        self.response = resp.content
        print 'Response:', self.response

    def parseYaResponse(self):
        respToDict = json.loads(self.response)
        if not self.isSentense:
            try:
                self.transList = respToDict['def'][0]['tr']
                self.transcription = respToDict['def'][0]['ts']
            except IndexError:
                self.transList = [{'text': 'NOT TRANSLATED'}]
                self.transcription = ''
        else:
            self.transList = respToDict['text']
            print self.transList
            self.transcription = ''

    def formatResult(self):
        formatedTranslations = ''
        for trans in self.transList:
            if not self.isSentense:
                formatedTranslations += '    %s\n' % trans['text']
            else:
                formatedTranslations += '    %s\n' % trans
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
        with open('/home/tolianych/Translations.txt', 'a') as f:
            f.write('%s\n' % translation.encode('utf8'))

if __name__ == '__main__':
    v = virtkey.virtkey()
    time.sleep(0.1)  # Don't know why, but it helps.
    v.lock_mod(1<<2) # CTRL
    v.press_keycode(54)
    v.release_keycode(54)
    v.unlock_mod(1<<2)
    root = Tkinter.Tk()
    root.withdraw()
    untranslated = root.clipboard_get()
    t = Translator(untranslated)
    t.main()
