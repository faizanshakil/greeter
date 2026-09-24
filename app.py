from http.server import HTTPServer, BaseHTTPRequestHandler

class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = """
        <html>
        <head>
            <title>Greeter</title>
        </head>
        <body>
            <h1>Hello, Faizan!</h1>
            <p>Have a great day!</p>
            <p>Welcome to my greeter app.</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8080), GreeterHandler)

print("Greeter app is running on port 8080")

server.serve_forever()
