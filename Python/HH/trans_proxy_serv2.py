'''
Created on Mar 18, 2014

@author: s.botyan
'''
import threading
import time
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        #print "%s wrote: " % self.client_address[0]
        print self.data
        result = self.send_home(self.data)
        self.request.send(result)
        
    def send_home(self, data):
        return 'Get this!'

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":

    HOST = 'localhost'
    PORT_WORK = 9095
    PORT_HOME = 9096

    server_WORK = ThreadedTCPServer((HOST, PORT_WORK), ThreadedTCPRequestHandler)
    server_HOME = ThreadedTCPServer((HOST, PORT_HOME), ThreadedTCPRequestHandler)

    server_WORK_thread = threading.Thread(target=server_WORK.serve_forever)
    server_HOME_thread = threading.Thread(target=server_HOME.serve_forever)

    server_WORK_thread.setDaemon(True)
    server_HOME_thread.setDaemon(True)

    server_WORK_thread.start()
    server_HOME_thread.start()

    while 1:
        time.sleep(1)