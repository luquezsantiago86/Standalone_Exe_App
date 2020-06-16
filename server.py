from waitress import serve

from app1 import app

server = app.server

serve(server, port=8049)
