# Python 3 server example -> https://pythonbasics.org/webserver/
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        # check for get request
        url = urllib.parse.urlparse(self.path)
        if url.path == '/api':
            self.wfile.write(url.path.encode('utf-8'))
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(' Hello, world!'.encode('utf-8'))
            return

        url_query = dict(urllib.parse.parse_qsl(url.query))
        query = ''
        # if the existence of a key in a dict
        if 'query' in url_query:
            query = url_query['query']
        if query == '':
            json_data = json.dumps('{error: true,msg: "Error empty product name!"}')
            self.wfile.write(json_data.encode())
            return
        # return all products
        if query == 'products':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header("Content-type", "application/json")
            self.end_headers()
            products = ('[[1, "product_1", 12.5, "sticker_1.png"], '
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
                        '[12, "product_12", 12.5, "sticker_12.png"]]')
            # Send the JSON data as the response
            self.wfile.write(products.encode('utf-8'))
            # return 1 product -> /product?name=product_1
        elif query == 'product':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # dict -> new dictionary initialized with the name=value pairs
            url_query = dict(urllib.parse.parse_qsl(url.query))
            product_name = ''
            # if the existence of a key in a dict
            if 'productName' in url_query:
                product_name = url_query['productName']
            if product_name == '':
                json_data = json.dumps('{error: true,msg: "Error empty product name!"}')
                self.wfile.write(json_data.encode())
                return

            product = '[[1, "' + product_name + '", 12.5, "sticker_1.png"]]'
            # Send the JSON data as the response
            self.wfile.write(product.encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(' Hello, world!'.encode('utf-8'))

#
# if __name__ == "__main__":
#     hostName = "localhost"
#     serverPort = 8000
#
#     webServer = HTTPServer((hostName, serverPort), MyServer)
#     print("Server started http://%s:%s" % (hostName, serverPort))
#
#     try:
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass
#
#     webServer.server_close()
#     print("Server stopped.")
