# Python 3 server example -> https://pythonbasics.org/webserver/
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import json
import urllib.parse

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):

    # check for get request
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        # return all products
        if url.path == '/products':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(
                '[[1, "product_1", 12.5, "sticker_1.png"], '
                '[2, "product_2", 12.5, "sticker_2.png"], '
                '[3, "product_3", 12.5, "sticker_3.png"], '
                '[4, "product_4", 12.5, "sticker_4.png"], '
                '[5, "product_5", 12.5, "sticker_5.png"], '
                '[6, "product_6", 12.5, "sticker_6.png"], '
                '[7, "product_7", 12.5, "sticker_7.png"], '
                '[8, "product_8", 12.5, "sticker_8.png"], '
                '[9, "product_9", 12.5, "sticker_9.png"], '
                '[10, "product_10", 12.5, "sticker_10.png"], '
                '[11, "product_11", 12.5, "sticker_11.png"], '
                '[12, "product_12", 12.5, "sticker_12.png"]]',
                'utf-8'))
            # return 1 product -> /product?name=product_1
        elif url.path == '/product':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes('[[1, "product_1", 12.5, "sticker_1.png"]]', 'utf-8'))
        else:
            self.path = '/index.html'
            file_to_open = open('index.html').read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
