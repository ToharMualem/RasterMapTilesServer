# RasterMapTilesServer
A map tiles serving application written in python.
# Installation and running
The project uses flask web framework to build the server and gdal2tiles to generate a folder with image tiles from a tiff image.
## Install flask
Installing flask can be done by pip:
```
pip install flask
```
## Install gdal2tiles
For cutting the image into tiles folder I used gdal2tiles, you can find it's repo here: https://github.com/tehamalab/gdal2tiles.
gdal2tiles uses GDAL - a translator library for raster and vector geospacial data, install GDAL here: https://gdal.org/download.html.
After installing GDAL, pip install gdal2tiles:
```
pip install gdal2tiles
```
# Running
Before running the webserver we need to generate our data, tiling.py does that.
write your tiff image path in the script, save and run the script with your python.
It looks like this:
```
path = r'{your_file_path}.tiff'
tiling_obj = Tiling(path)
tiling_obj.generate_tiles_folder(f"{tiling_obj.file_name}_Tiles")
```

After your tiles folder is ready, run the server simply by running main.py with python.
the html script called maptiles.html is an openlayers client, it requests localhost:8080 for tiles, you can change it in case which your server isn't local.


