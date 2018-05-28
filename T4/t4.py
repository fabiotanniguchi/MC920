#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 4
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import imageio as io
import math as m

from matplotlib import pyplot as plt

import numpy as np

import sys as s

#-----------------------------------------------------------------------------------------

# x' = x cos(theta) - y sin(theta)
# y' = x sin(theta) + y cos(theta)

#-----------------------------------------------------------------------------------------

def rotate(image_origin, angle):
    angle_radians = m.radians(angle)
    new_positions = np.zeros( (image_origin.shape[0], image_origin.shape[1], 2) )

    for (i, j), value in np.ndenumerate(image_origin):
        new_positions[i, j, 0] = max(min(round((i * m.cos(angle_radians)) - (j * m.sin(angle_radians))), image_origin.shape[0]-1), 0)
        new_positions[i, j, 1] = max(min(round((i * m.sin(angle_radians)) + (j * m.cos(angle_radians))), image_origin.shape[1]-1), 0)

    image_result = np.zeros(np.shape(image_origin))

    for (i, j), value in np.ndenumerate(image_origin):
        image_result[i, j] = image_origin[int(new_positions[i, j, 0]), int(new_positions[i, j, 1])]

    return image_result

#-----------------------------------------------------------------------------------------

def nearest_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    rotated_image = rotate(image, angle)

    plt.imshow(rotated_image, cmap="gray", vmin=0, vmax=255)
    plt.show()

#-----------------------------------------------------------------------------------------

def billinear_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    rotated_image = rotate(image, angle)

#-----------------------------------------------------------------------------------------

def bicubic_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    rotated_image = rotate(image, angle)

#-----------------------------------------------------------------------------------------

def lagrange_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    rotated_image = rotate(image, angle)

#-----------------------------------------------------------------------------------------

def resolve_execution_sfxy(image, out_file_path, method, angle, scale_factor_x, scale_factor_y):
    if method == "1":
        nearest_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y)
    elif method == "2":
        billinear_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y)
    elif method == "3":
        bicubic_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y)
    elif method == "4":
        lagrange_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y)
    else:
        print("Invalid method")
        exit(-1)

#-----------------------------------------------------------------------------------------

def resolve_execution_xy(image, out_file_path, method, angle, x, y):
    scale_factor_x = x/image.shape[1]
    scale_factor_y = y/image.shape[0]
    resolve_execution_sfxy(image, out_file_path, method, angle, scale_factor_x, scale_factor_y)

#-----------------------------------------------------------------------------------------

def resolve_execution_sf(image, out_file_path, method, angle, scale_factor):
    resolve_execution_sfxy(image, out_file_path, method, angle, scale_factor, scale_factor)

#-----------------------------------------------------------------------------------------

file_path = s.argv[1]
out_file_path = s.argv[2]
method = s.argv[3]
angle = float(s.argv[4])
scale_factor = -1.0
x = -1.0
y = -1.0

if len(s.argv) == 6:
    scale_factor = float(s.argv[5])
    print("Using scale factor", scale_factor)
elif len(s.argv) == 7:
    x = float(s.argv[5])
    y = float(s.argv[6])
    print("Using dimensions", x, " and ",y)
else:
    print("Cannot resolve execution using this combination of parameters")
    exit(-1)

print("Loading file", file_path, "...")

image = io.imread(file_path, "PNG-PIL", as_gray=True)

if float(x) > float(0.0) and float(y) > float(0.0):
    resolve_execution_xy(image, out_file_path, method, angle, x, y)
else:
    resolve_execution_sf(image, out_file_path, method, angle, scale_factor)
