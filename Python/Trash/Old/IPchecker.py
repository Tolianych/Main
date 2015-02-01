'''
Created on 04 march 2014

@author: Tolianych
'''
import urllib2, smtplib

url = 'http://2ip.ru/'

usock = urllib2.urlopen(url)
html = usock.read()
usock.close()

IPstart = html.find('<big id="d_clip_button">')
IPend = html.find('</big>')
IP = html[IPstart + 24 : IPend]

header = 'From: tormentor_bts@mail.ru\n'
header += 'To: tormentor_bts@mail.ru\n'
header += 'Subject: ' + IP + '\n'

message = header + 'IP is ' + IP
server = smtplib.SMTP('smtp.mail.ru')
server.starttls()
server.login('tormentor_bts@mail.ru', 'starfish')
problems = server.sendmail('tormentor_bts@mail.ru', 'tormentor_bts@mail.ru', message)
server.quit()
