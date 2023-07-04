import os.path

from flask import send_file
from flask import Response
from flask.views import MethodView
from tiling import tiling_obj

FILE_NAME = tiling_obj.file_name


class TileRequestHandler(MethodView):
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
        folder_name = f"{FILE_NAME}_Tiles"
        file_path = f"{folder_name}/{zoom}/{x}/{y}.png"
        if os.path.isfile(file_path):
            return file_path
        else:
            return ""
