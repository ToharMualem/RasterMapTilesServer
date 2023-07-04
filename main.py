"""
Author: Tohar Mualem <toharm7@gmail.com>
Date: 4-07-2023
Purpose: main script, runs the flask application.
"""

import tile_serving_application
from tiling import tiling_obj


if __name__ == '__main__':
    serving_app = tile_serving_application.create_application(tiling_obj.file_name, r"/")
    serving_app.run_server()
