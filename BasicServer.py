import BaseHTTPServer

# Run this if you want to just have one picture shown on the browser
# instead of multiple ones
#
# To show all files in a directory
# navigate to that directory in a terminal and use:
# python -m SimpleHTTPServer <PORT NUMBER> 

# handler to load one image
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        # choose an image to be opened!
        self.wfile.write(open('/home/linaro/Desktop/Pictures/my_image.png').read())

# /sbin/ifconfig to check your IP address
# Change 127.0.0.1 to actual ipaddress
IP_ADDRESS = '127.0.0.1'

# Port is just a port you can connect to 
# Make sure nothing else is using the port you've selected
PORT = 8081

httpd = BaseHTTPServer.HTTPServer((IP_ADDRESS, PORT),Handler)

print "serving @ port", PORT
httpd.serve_forever()
