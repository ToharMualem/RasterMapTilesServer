# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tile_serving_application
from tiling import tiling_obj

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serving_app = tile_serving_application.create_application(tiling_obj.file_name, r"/")
    serving_app.run_server()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
