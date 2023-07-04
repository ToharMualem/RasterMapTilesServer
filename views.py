"""
Author: Tohar Mualem <toharm7@gmail.com>
Date: 4-07-2023
Purpose: An API script for tile_serving_application.py
"""

import os.path
from flask import send_file
from flask import Response
from flask.views import MethodView
from tiling import tiling_obj

FILE_NAME = tiling_obj.file_name


class TileRequestHandler(MethodView):
    """ handles requests for tile image,these requests end in <zoom>/<x>/<y>"""
    def get(self, zoom, x, y):
        file_path = self.generate_tile_path(zoom, x, y)
        print(file_path)
        if file_path == "":
            return Response(status=204)

        return send_file(file_path)

    def post(self, zoom, x, y):
        file_path = self.generate_tile_path(zoom, x, y)
        if file_path == "":
            return Response(status=204)

        return send_file(file_path)

    @staticmethod
    def generate_tile_path(zoom, x, y):
        """
        finds the file_path of the requested tile image.
        :param zoom: zoom level - an integer.
        :param x: x coordinate - an integer.
        :param y: y coordinate - an integer.
        :return: a file_path, in case that tile image doesn't exist - returns empty string.
        """
        folder_name = f"{FILE_NAME}_Tiles"
        file_path = f"{folder_name}/{zoom}/{x}/{y}.png"
        if os.path.isfile(file_path):
            return file_path
        else:
            return ""
