import os
import socket
import threading
import socketserver


SERVER_HOST = 'localhost'
SERVER_PORT = 0 # tells the kernel to pickup a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkedClient():
    """A client to test forking server"""
    def __init__(self, ip, port):
        # Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        self.sock.connect((ip, port))

    def run(self):
        """Client playing with the server"""
        # Send the data to server
        current_process_id = os.getpid()
        print("PID ", current_process_id, "Sending echo message to the server : ", ECHO_MSG)
        sent_data_length = self.sock.send(bytearray(ECHO_MSG, 'utf-8'))
        print("Sent: ", sent_data_length, "characters. so far...")

        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print("PID ", current_process_id, " received: ", response[5:])

    def shutdown(self):
        """Cleanup the client socket"""
        self.sock.close()

class ForkingServerRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s: %s' % (current_process_id, data)
        print("Server sending response [current_process_id: data] = ", response)
        self.request.send(bytearray(response, 'utf-8'))
        return

class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer, ):
    """Nothing to add here. inherited everyting necessary from parents"""
    pass

def main(prog_for_server):
    while True:
        if prog_for_server == True:
            # Launch the server
            server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
            ip, port = server.server_address # Retrieve the port number
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.setDaemon(True) # don't hang on exit
            server_thread.start()
            print("Server loop running PID: ", os.getpid())
        else:
        # Launch the client(s)
        client1 = ForkedClient(ip, port)
        client1.run()

        # Clean them up
        server.shutdown()
        client1.shutdown()
        server.socket.close()

if __name__ == '__main__':
    main()