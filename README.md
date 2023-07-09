# RasterMapTilesServer
A map tiles serving application written in python.
# Installation and running
The project uses flask web framework to build the server and gdal2tiles to generate a folder with image tiles from a tiff image.
I also added a script for converting pdf to tiff image.
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
## Installing things for pdf converting to tiff
The script pdf_to_tiff.py uses wand which is python bindings library of MagickImage. For rasterizing the pdf file, MagickImage uses Ghostscript.
Install wand using pip:
```
pip install Wand
```
Install MagickImage from their website: https://imagemagick.org/script/download.php
and Install Ghostscript from their website: https://ghostscript.com/releases/gsdnld.html

# Running
In case which you have a pdf file, you need to convert the file to tiff image, because pdf file contains vector data and my server works on raster image.
For this situation I wrote a script called pdf_to_tiff.py, before running the script please install Wand using pip, MagickImage and GhostScript.
Before running change the variable pdf_path in the script to your file path.
It looks like this:
```
pdf_path = "{your_file_path}.pdf"
if path.isfile(pdf_path):
    convert_pdf_to_tiff(pdf_path)
```

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


