'''
Created on Mar 17, 2014

@author: botyan
'''
import socket

host_home = "localhost"
port_trans = 9091
host_serv = "192.168.1.5"
port_serv = 9092

def execute():
    s_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_serv.connect((host_serv, port_serv))
    
    s_trans = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_trans.connect((host_home, port_trans))
    
    while True:
        request = s_serv.recv(1024)
        response = send_trans(request, s_trans)
        send_trans(response, s_serv)

def send_trans(request, s_trans):
    s_trans.send(request)
    response = s_trans.recv(1024)
    return response

if __name__ == "__main__":
    execute()
