from http.server import HTTPServer, BaseHTTPRequestHandler

from stocker import Stocker

mystocker = Stocker()

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            #self.path = '/index.html'
            #file_to_open = open(self.path[1:]).read()
            text = '<html><body><p>'
            text += 'AMAZON'
            text += '</p></body></html>'
            file_to_open = text
            self.send_response(200)

        elif 'secret' in self.path:
            self.path = '/secret/index.html'
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)

        elif 'calc' in self.path:
            try:
                result = str(eval(self.path.split('?')[-1]))
            except:
                result = 'ERROR'
            text = '<html><body><p>'
            text += result
            text += '</p></body></html>'
            file_to_open = text
            self.send_response(200)

        elif 'stocker' in self.path:
            try:
                result =  str(mystocker(self.path))
            except:
                result = 'ERROR'
            text = '<html><body><p>'
            text += result
            text += '</p></body></html>'
            file_to_open = text
            self.send_response(200)

        """
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = 'File no found'
            self.send_response(404)
        """
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


host = 'localhost'
port = 8080

httpd = HTTPServer((host, port), Serv)
httpd.serve_forever()
