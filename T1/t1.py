#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 1
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s
import cv2
import numpy as np
import scipy
import pylab
from scipy import misc
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------------

def Draw_Borders(image):
    shapeMask = cv2.inRange(image, 0, 127)
    #plt.imshow(shapeMask, cmap="gray", vmin=0, vmax=255)
    #plt.show()
    #plt.gcf().clear()

    # find the contours in the mask
    (im2, cnts, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # create a blank image and fill it with the contours
    imageWithBorders = np.zeros(image.shape, dtype=np.uint8)
    imageWithBorders.fill(255)
    cv2.drawContours(imageWithBorders, cnts, -1, 128, 2)
    plt.imshow(imageWithBorders, cmap="gray", vmin=0, vmax=255)
    plt.title('Contornos dos objetos detectados')
    plt.savefig("2_borders_145980.png")
    plt.gcf().clear()

    return (cnts, imageWithBorders)

#-----------------------------------------------------------------------------------------

def Name_Contours_And_Show_Stats(imageWithBorders, cnts):

    # loop over the contours
    i = 0
    small_objects = []
    medium_objects = []
    big_objects = []
    print("Número de regiões: ", np.size(cnts, 0))
    for c in cnts:
        # centroid calc
        M = cv2.moments(c)
        cX = int((M["m10"] / (M["m00"] + 1)))
        cY = int((M["m01"] / (M["m00"] + 1)))

        shape = str(i)

        cv2.putText(imageWithBorders, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, 0, 2, cv2.LINE_AA)

        perimeter = cv2.arcLength(c,True)
        area = cv2.contourArea(c)

        print("região: ", i, " | perímetro: ", round(perimeter, 1), " | área: ", round(area, 1))

        # organizing contours in categories
        if(area < 1500):
            small_objects.append(c)
        else:
            if (area < 3000):
                medium_objects.append(c)
            else:
                big_objects.append(c)

        i += 1

    # showing the objects with labels
    plt.imshow(imageWithBorders, cmap="gray", vmin=0, vmax=255)
    #plt.show()
    plt.title('Objetos encontrados e seus respectivos números')
    plt.savefig("3_object_names_145980.png")
    plt.gcf().clear()

    # drawing histogram
    x = scipy.arange(3)
    y = scipy.array([len(small_objects), len(medium_objects), len(big_objects)])
    f = pylab.figure()
    ax = f.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, y, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(["Objetos pequenos", "Objetos médios", "Objetos grandes"])
    f.savefig("4_histogram_145980.png")

# -----------------------------------------------------------------------------------------

# receiving the (image) file path
file_path = s.argv[1]
print("Lendo arquivo", file_path, "...")

# loading the PNG into a ndarray
image = misc.imread(file_path, True)

plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title('Imagem transformada para escala de cinza')
#plt.show()
plt.savefig("1_grayscale_145980.png")
plt.gcf().clear()

(contours, imageWithBorders) = Draw_Borders(image)

Name_Contours_And_Show_Stats(imageWithBorders, contours)
