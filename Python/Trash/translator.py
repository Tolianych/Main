'''
Created on Apr 4, 2015

sudo pip install google_translate_api
sudo apt-get install python-tk
sudo apt-get install python-virtkey

@author: tolianych
'''
import google_translate_api as api
import Tkinter
import tkMessageBox
import virtkey

file_path = '/home/tolianych/Polygon/NewWords.txt'

v = virtkey.virtkey()
v.lock_mod(1<<2) # CTRL
v.press_keycode(54)
v.release_keycode(54)
v.unlock_mod(1<<2)

root = Tkinter.Tk()
root.withdraw()
untranslated = root.clipboard_get()

translator = api.TranslateService()
translated = translator.trans_sentence('en', 'ru', untranslated)

window = Tkinter.Tk()
window.wm_withdraw()
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title="Translator", message="%s" % (translated))

with open(file_path, 'a') as f:
    f.write(untranslated + '    ' + translated.encode('utf-8') + '\n')
