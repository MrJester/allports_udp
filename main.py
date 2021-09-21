import threading
import socketserver


class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request[0].strip()
        self.socket = self.request[1]
        print("Received data from: {}:{}".format(self.client_address[0], self.client_address[1]))

        if self.data:
            self.socket.sendto(self.data.upper(), self.client_address)


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


sockets = []
socket_threads = []
server = '0.0.0.0'

for port_number in range(100, 150):
    try:
        sockets.append(ThreadedUDPServer((server, port_number), ClientHandler))
        print("Socket opened on port {}".format(port_number))
    except OSError:
        print("Error opening socket on {}, port is already in use.".format(port_number))
        pass

for TDC_server in sockets:
    socket_threads.append(threading.Thread(target=TDC_server.serve_forever))

for TDC_server_thread in socket_threads:
    TDC_server_thread.setDaemon(True)
    TDC_server_thread.start()

while True:
    continue