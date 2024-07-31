from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import platform
import psutil

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        os_info = platform.platform()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent

        html = f"""
        <html>
            <body>
                <h1>System Information</h1>
                <p>Hostname: {hostname}</p>
                <p>IP Address: {ip_address}</p>
                <p>OS: {os_info}</p>
                <p>CPU Usage: {cpu_percent}%</p>
                <p>Memory Usage: {memory_percent}%</p>
            </body>
        </html>
        """

        self.wfile.write(html.encode())

def run_server():
    web_server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server started on port 8000")
    web_server.serve_forever()

if __name__ == "__main__":
    run_server()