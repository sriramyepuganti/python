# python -m http.server to start a server
# python server.py run below code

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json


hostName = "localhost"
serverPort = 8080

json_string = json.dumps({'id':1})

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.set_headers()
        self.set_responses(json_string)
        return
    def set_headers(self, code=200, type="application/json"):
        self.send_response(code)
        self.send_header("Content-type", type )
        self.end_headers() 
    def set_responses(self,data):
        self.wfile.write(data.encode())


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
