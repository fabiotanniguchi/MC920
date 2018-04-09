#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 0
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s
import cv2
import numpy as np
import asyncio
from scipy import misc
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------------

async def Calculate_Stats(image):
    print("-----------------------------------")
    print("Largura:", image.shape[1])  # colunas
    print("Altura:", image.shape[0])  # linhas
    print("-----------------------------------")
    print("Intensidade mínima:", image.min())
    print("Intensidade máxima:", image.max())
    print("Intensidade média:", round(image.mean(), 2))
    print("-----------------------------------")

#-----------------------------------------------------------------------------------------

async def Plot_Histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.ylabel('frequência')
    plt.xlabel('níveis de cinza')
    plt.title('Histograma')

    #plt.show()

    plt.savefig("145980_1_histogram.png")

    plt.gcf().clear()

#-----------------------------------------------------------------------------------------

async def Negative(image):
    full_matrix = np.full(image.shape, 256)
    negative = full_matrix - image
    plt.imshow(negative, cmap="gray", vmin=0, vmax=255)
    plt.title('Negativo da imagem')

    #plt.show()

    plt.savefig("145980_2_negative.png")

    plt.gcf().clear()

#-----------------------------------------------------------------------------------------

async def Rescale_Intensity(image, min, max):
    factor = (max-min+1)/256
    limited_image = ( image * factor ) + min
    plt.imshow(limited_image, cmap="gray", vmin=0, vmax=255)
    plt.title('Imagem transformada')

    #plt.show()

    plt.savefig("145980_3_transformed.png")

    plt.gcf().clear()

# -----------------------------------------------------------------------------------------

# receiving the (image) file path
file_path = s.argv[1]
print("Lendo arquivo", file_path, "...")

# loading the PNG into a ndarray
image = misc.imread(file_path, True)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    Calculate_Stats(image),
    Plot_Histogram(image),
    Negative(image),
    Rescale_Intensity(image, 120, 180)
))
loop.close()
