#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 3
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import imageio as io

import sys as s

import numpy as np

from scipy import misc
from scipy import ndimage

from skimage import feature
from skimage import filters
from skimage import segmentation
from skimage import transform

import statistics

import warnings

#-----------------------------------------------------------------------------------------

def alignHProj(image, out_file_path):
    max_amplitude = 0
    max_amplitude_angle = 0

    for x in range(-90, 90):
        rotated = misc.imrotate(image, x)
        
        sum_lines = np.sum(rotated, axis=1)
        amplitude = np.max(sum_lines)

        if (amplitude > max_amplitude):
            max_amplitude = amplitude
            max_amplitude_angle = x

    final_image = abs(image - 1)
    final_image = misc.imrotate(final_image, max_amplitude_angle, interp="bicubic")

    print()
    print("Salvando arquivo", out_file_path, "...")
    io.imwrite(out_file_path, final_image, "PNG-PIL", compress_level=0, optimize=False)

    return 0

#-----------------------------------------------------------------------------------------

def alignHoughTransf(image, out_file_path):

    blur = filters.gaussian(image, 3)
    edges = feature.canny(blur)
    hough_lines = transform.probabilistic_hough_line(edges)

    slopes = [(y2 - y1) / (x2 - x1) if (x2 - x1) else 0 for (x1, y1), (x2, y2) in hough_lines]

    rad_angles = [np.arctan(x) for x in slopes]
    deg_angles = [np.degrees(x) for x in rad_angles]

    rotation_number = statistics.median(deg_angles)

    final_image = abs(image - 1)
    final_image = misc.imrotate(final_image, rotation_number, interp="bicubic")

    print()
    print("Salvando arquivo", out_file_path, "...")
    io.imwrite(out_file_path, final_image, "PNG-PIL", compress_level=0, optimize=False)

    return 0

#-----------------------------------------------------------------------------------------

# receiving the (image) file path
file_path = s.argv[1]
align_mode = s.argv[2]
out_file_path = s.argv[3]

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    print("Lendo arquivo", file_path, "...")

    image = io.imread(file_path, "PNG-PIL", as_gray=True)

    threshold = filters.threshold_yen(image)

    bin_image = np.zeros(image.shape, dtype="bool")
    bin_image = image <= threshold
    bin_image = segmentation.clear_border(bin_image)

    if(align_mode == "1"):
        alignHProj(bin_image, out_file_path)
    elif(align_mode == "2"):
        alignHoughTransf(bin_image, out_file_path)
    else:
        print()
        print("Escolha uma opção válida")
        print()
        print("Modo 1 para Alinhamento por Projeção Horizontal")
        print("Modo 2 para Alinhamento por Transformada de Hough")

print()
print("FIM")
