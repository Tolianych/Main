'''
Created on Mar 17, 2014

@author: botyan
'''
import socket

host = "localhost"
port = 9091
port_trans = 9092

def execute():
    s9091 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s9091.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s9091.bind((host, port))
    s9091.listen(5)
    sock9091, addr9091 = s9091.accept()
    
    s9092 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s9092.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s9092.bind((host, port_trans))
    s9092.listen(5)
    sock9092, addr9092 = s9092.accept()
    
    while True:
        request = sock9091.recv(1024)
        response = send_home(request, sock9092)
        send_work(self, response, sock9091)

def send_home(self, request, sock9092):
    sock9092.send(request)
    response = sock9092.recv(1024)
    return response
    
def send_work(self, response, sock9091):
    sock9091.send(response)

if __name__ == "__main__":
    execute()
