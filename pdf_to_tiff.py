"""
Author: Tohar Mualem <toharm7@gmail.com>
Date: 9-07-2023
Purpose: Uses Wand for creating a tiff image from a pdf with one page.
"""

from wand.image import Image
from os import path


def convert_pdf_to_tiff(file_path):
    pdf = Image(filename=file_path, resolution=300)
    file_name = path.splitext(path.basename(file_path))[0]
    pdf_images = pdf.convert("tiff")
    images_names = []
    i = 0
    for img in pdf_images.sequence:
        page_img = Image(img)
        suffix_str = "" if i == 0 else f"{i}"
        page_img.save(filename=f"{file_name}{suffix_str}.tiff")
        images_names.append(f"{file_name}{suffix_str}.tiff")
        i += 1

    return images_names


pdf_path = "103S.pdf"
if path.isfile(pdf_path):
    convert_pdf_to_tiff(pdf_path)
