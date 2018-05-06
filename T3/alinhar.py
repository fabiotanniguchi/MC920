#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 3
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s

import numpy as np

from scipy import misc

from skimage import filters
from skimage import segmentation
from skimage import transform

from matplotlib import cm
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------------

def alignHProj(image, out_file_path):
    max_amplitude = 0
    max_amplitude_angle = 0

    for x in range(-90, 90):
        rotated = transform.rotate(image, x, resize=True)
        
        sum_lines = np.sum(rotated, axis=1)
        amplitude = np.max(sum_lines)

        if (amplitude > max_amplitude):
            max_amplitude = amplitude
            max_amplitude_angle = x

    final_image = transform.rotate(image, max_amplitude_angle, resize=True)
    final_image_for_pyplot = abs(final_image - 1)

    plt.imsave(out_file_path, final_image_for_pyplot, cmap=cm.gray, vmin=0, vmax=1)

    return 0

#-----------------------------------------------------------------------------------------

def alignHoughTransf(image, out_file_path):
    return 0


#-----------------------------------------------------------------------------------------

# receiving the (image) file path
file_path = s.argv[1]
align_mode = s.argv[2]
out_file_path = s.argv[3]

print("Lendo arquivo", file_path, "...")

image = misc.imread(file_path, True)

threshold = filters.threshold_yen(image)
bin_image = image <= threshold
bin_image = segmentation.clear_border(bin_image)

plt.title("Imagem binária")
plt.imshow(bin_image, cmap="Greys",  interpolation="nearest")
plt.show()

if(align_mode == "1"):
    alignHProj(bin_image, out_file_path)
else:
    if(align_mode == "2"):
        alignHoughTransf(bin_image, out_file_path)
    else:
        print()
        print("Escolha uma opção válida")
        print()
        print("Modo 1 para Alinhamento por Projeção Horizontal")
        print("Modo 2 para Alinhamento por Transformada de Hough")
