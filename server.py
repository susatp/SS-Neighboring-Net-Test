#!/usr/bin/env python3
"""
Simple HTTP server for La Bo Bo interactive page
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

# Use environment variable for port (Azure sets this automatically)
PORT = int(os.environ.get('PORT', 8000))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🎭 La Bo Bo Interactive Server")
        print(f"📡 Server running at: http://0.0.0.0:{PORT}")
        print(f"⏹️  Press Ctrl+C to stop the server")
        
        # Don't open browser automatically in production
        if os.environ.get('WEBSITE_SITE_NAME') is None:  # Only open browser locally
            print(f"🌐 Opening browser automatically...")
            webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped")
            httpd.shutdown()

if __name__ == "__main__":
    main()
