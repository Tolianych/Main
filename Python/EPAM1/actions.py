'''
Created on Jan 14, 2015

@author: s.botyan
'''
import os
import pwd

def find_owner(path, name):
    return pwd.getpwuid(os.stat(os.path.join(path, name)).st_uid).pw_name

def change_owner(user, path, name, sudo_pas):
    command = "chown %s %s" % (user, os.path.join(path, name))
    os.popen("sudo -S %s"%(command), 'w').write(sudo_pas + '\n')
    
def change_owner_group(user, path, name, sudo_pas):
    command = "chown %s:%s %s" % (user, user, os.path.join(path, name))
    os.popen("sudo -S %s"%(command), 'w').write(sudo_pas + '\n')

def chmod(mode, path, name, sudo_pas):
    command = "chmod %s %s" % (mode, os.path.join(path, name))
    os.popen("sudo -S %s"%(command), 'w').write(sudo_pas + '\n')
    
def open_file(path, name):
    open(os.path.join(path, name), 'r')

def modify_file(path, name):
    f = open(os.path.join(path, name), 'a')
    f.write("new line\n")

def execute_file(path, name):
    execfile(os.path.join(path, name))

def setfacl(mode, path, name, sudo_pas):
    command = "setfacl -m %s " % mode + os.path.join(path, name)
    os.popen("sudo -S %s"%(command), 'w').write(sudo_pas + '\n')
    