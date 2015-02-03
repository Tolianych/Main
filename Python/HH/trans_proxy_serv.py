'''
Created on Mar 17, 2014

@author: botyan
'''
import threading
import socket

host = "localhost"
port_work = 9098
port_home = 9099

class pipe_home(threading.Thread):
    def run(self):
        s9092 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s9092.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s9092.bind((host, port_home))
        s9092.listen(1)
        sock9092, addr9092 = s9092.accept()
    
    def send_home(self, request):
        self.sock9092.send(request)
        self.response = self.sock9092.recv(1024)
        return self.response
        
class pipe_work(threading.Thread):
    def run(self):
        s9091 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s9091.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s9091.bind((host, port_work))
        s9091.listen(1)
        sock9091, addr9091 = s9091.accept()
    
    def send_work(self, response):
        self.sock9091.send(response)
        
def main():
    pipe_to_home = pipe_home()
    pipe_to_home.start()
    pipe_to_work = pipe_work()
    pipe_to_work.start()
    
    while True:
        request = pipe_to_work.recv(1024)
        response = pipe_to_home.send_home(request)
        pipe_to_work.send_work(response)

if __name__ == "__main__":
    main()