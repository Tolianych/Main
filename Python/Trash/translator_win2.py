#   -*- coding: utf-8 -*-
'''
Created on Aug 3, 2015
@author: tolianych
For Windows only!
Translates selected text in translate.google.com directly by GET request and
returns result in popup window. In Linux could be setted
to system shortcut like 'python /home/user/translator.py' and assigned
shortcut should start with Ctrl (Ctrl+g for example).
'''
import requests
import Tkinter
import tkMessageBox
import SendKeys


SendKeys.SendKeys('^C')
root = Tkinter.Tk()
root.withdraw()
untranslated = root.clipboard_get()
print untranslated
getik = "https://translate.google.com/translate_a/single?client=t&sl=en&tl=ru&hl=ru&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&otf=1&srcrom=1&ssel=0&tsel=0&kc=1&tk=522934|790551&q=%s" % untranslated

r = requests.get(getik)
googleResponse = r.content
translated = ''


def findTranslations(wordTypeIndex):
    transStart = googleResponse.find('[', wordTypeIndex) + 1
    transEnd = googleResponse.find(']', wordTypeIndex)
    translationsString = googleResponse[transStart: transEnd].translate(None, '"')
    translations = translationsString.split(',')
    if not translations[0][0] == '[':
        return translations


def getTranslations(tp):
    wordTypeIndex = googleResponse.find(tp)
    if wordTypeIndex > 0:
        result = ''
        result += '%s:\n' % tp
        try:
            for translation in findTranslations(wordTypeIndex):
                result += '    %s\n' % translation
            return result
        except TypeError:
            pass

def getMainTranslation():
    transStart = googleResponse.find('[[["') + 4
    transEnd = googleResponse.find('"', transStart)
    return googleResponse[transStart: transEnd]

translated += '%s\n' % getMainTranslation()
for wordType in ['имя существительное', 'имя прилагательное', 'наречие']:
    trans = getTranslations(wordType)
    if trans:
        translated += trans

window = Tkinter.Tk()
window.wm_withdraw()
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title="Translated!", message="%s" % (translated))
