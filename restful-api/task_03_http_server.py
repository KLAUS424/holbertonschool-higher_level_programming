#!/usr/bin/python3
"""
Simple API using Python's http.server module
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP request handler for simple API endpoints
    """
    def do_GET(self):
        """Handle GET requests"""
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # Route requests based on path
        if self.path == '/':
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode())
        elif self.path == '/data':
            # Serve JSON data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())
        elif self.path == '/status':
            # API status endpoint
            response = "OK"
            self.wfile.write(response.encode())
        elif self.path == '/info':
            # Additional endpoint from hints
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode())
        else:
            # Handle undefined endpoints
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            response = "Endpoint not found"
            self.wfile.write(response.encode())


def run_server():
    """Start the HTTP server"""
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Starting server on port 8000...")
    print("Visit http://localhost:8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
