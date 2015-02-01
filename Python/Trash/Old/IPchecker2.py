'''
Created on 04 march 2014

@author: Tolianych
'''
import urllib2, smtplib

req = urllib2.Request('http://192.168.1.1/userRpm/StatusRpm.htm')
req.add_header('Accept-Encoding','gzip,deflate,sdch')
passman=urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None,'http://192.168.1.1','Tolianych','starfish')
auth=urllib2.HTTPBasicAuthHandler(passman)
page = urllib2.build_opener(auth).open(req).read()

IPstart = page.find('wanPara = new Array(')
IPend = page.find('"255.255.255.255"')
IP = page[IPstart + 46 : IPend - 6]

url = 'http://2ip.ru/'

usock = urllib2.urlopen(url)
html_2ip = usock.read()
usock.close()

IP2start = html_2ip.find('<big id="d_clip_button">')
IP2end = html_2ip.find('</big>')
IP2 = html_2ip[IP2start + 24 : IP2end]

header = 'From: tormentor_bts@mail.ru\n'
header += 'To: tormentor_bts@mail.ru\n'
header += 'Subject: ' + IP + ' & ' + IP2 + '\n'

message = header + 'IP is ' + IP + ' & ' + IP2
server = smtplib.SMTP('smtp.mail.ru')
server.starttls()
server.login('tormentor_bts@mail.ru', 'starfish')
problems = server.sendmail('tormentor_bts@mail.ru', 'tormentor_bts@mail.ru', message)
server.quit()