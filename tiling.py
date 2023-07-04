import os.path
import gdal2tiles


class Tiling:
    def __init__(self, file_path):
        self.path = file_path
        self.file_name = os.path.splitext(os.path.basename(self.path))[0]
        self.options = {'zoom': (1, 9), 'resume': True, 'profile': 'raster'}

        if not os.path.isfile(self.path):
            print(f"tiling.py couldn't find file in path: {self.path}")

    def tile_file(self, output_path):
        gdal2tiles.generate_tiles(self.path, output_path, **self.options)


path = r'103S.tiff'
tiling_obj = Tiling(path)
