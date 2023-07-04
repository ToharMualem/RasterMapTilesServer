from flask import Flask
from views import TileRequestHandler


class TileServingApp:
    def __init__(self, name, static_url_path, host=r'localhost', port=8080):
        self.app = Flask(name, static_url_path)
        self.host = host
        self.port = port

    def add_url(self, url, view_function):
        self.app.add_url_rule(url, view_func=view_function)

    def run_server(self):
        self.app.run(self.host, self.port)

    def get_static_url_path(self):
        return self.app.static_url_path


def create_application(name, static_url_path, host=r'localhost', port=8080):
    serving_app = TileServingApp(name, static_url_path, host, port)
    serving_app.add_url(r'/tiles/<zoom>/<x>/<y>', TileRequestHandler.as_view("tile_api"))

    return serving_app


def run_app(serving_app):
    serving_app.run_server()
