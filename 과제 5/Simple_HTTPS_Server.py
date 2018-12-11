import http.server
import ssl

# PEM PASSWORD : 1234

httpd = http.server.HTTPServer(('localhost', 4443), http.server.BaseHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', keyfile='key.pem')
httpd.serve_forever()
print("Fail to start server or server stopped to run!")