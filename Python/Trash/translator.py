'''
Created on Apr 4, 2015

@author: tolianych

For Linux only!
Translates selected text in translate.google.com and
returns result in popup window. Should be setted 
to system shortcut (System-> Keyboard -> Shortcuts)
like 'python /home/user/translator.py' and assigned
shortcut should start with Ctrl (Ctrl+g for example).
'''
import google_translate_api as api
import Tkinter
import tkMessageBox
import virtkey

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
tkMessageBox.showinfo(title="Agent IP", message="%s" % (translated))
