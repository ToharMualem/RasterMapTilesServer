"""
Author: Tohar Mualem <toharm7@gmail.com>
Date: 4-07-2023
Purpose: A flask application for serving map tiles.
"""

from flask import Flask
from views import TileRequestHandler


class TileServingApp:
    """
    A wrapper of a flask application with functionality.
    """
    def __init__(self, name, static_url_path, host=r'localhost', port=8080):
        self.app = Flask(name, static_url_path)
        self.host = host
        self.port = port

    def add_url(self, url, view_function):
        """
        add url with a functionality, a wrapper of flask's add_url_rule.
        :param url: string of desired url.
        :param view_function: a function received from as_view function of class inherits View
        :return: void
        """
        self.app.add_url_rule(url, view_func=view_function)

    def run_server(self):
        """
        runs self.app server.
        :return: void
        """
        self.app.run(self.host, self.port)

    def get_static_url_path(self):
        return self.app.static_url_path


def create_application(name, static_url_path, host=r'localhost', port=8080):
    serving_app = TileServingApp(name, static_url_path, host, port)

    # add functionality to flask app here.
    serving_app.add_url(r'/tiles/<zoom>/<x>/<y>', TileRequestHandler.as_view("tile_api"))

    return serving_app


def run_app(serving_app):
    serving_app.run_server()
