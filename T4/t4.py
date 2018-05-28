#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 4
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import imageio as io

import sys as s

import scipy as sp

#-----------------------------------------------------------------------------------------

def nearest_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    return

#-----------------------------------------------------------------------------------------

def billinear_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    return

#-----------------------------------------------------------------------------------------

def bicubic_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    return

#-----------------------------------------------------------------------------------------

def lagrange_interpolation(image, out_file_path, angle, scale_factor_x, scale_factor_y):
    return

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
angle = s.argv[4]
scale_factor = -1.0
x = -1.0
y = -1.0

if len(s.argv) == 6:
    scale_factor = s.argv[5]
elif len(s.argv) == 7:
    x = s.argv[5]
    y = s.argv[6]
else:
    print("Cannot resolve execution using this combination of parameters")
    exit(-1)

print("Lendo arquivo", file_path, "...")

image = io.imread(file_path, "PNG-PIL", as_gray=True)

if float(x) > float(0.0) and float(y) > float(0.0):
    resolve_execution_xy(image, out_file_path, method, angle, x, y)
else:
    resolve_execution_sf(image, out_file_path, method, angle, scale_factor)
