# -----------------------------------------------------------------------------------------
# MC920 - TRABALHO 4
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
# -----------------------------------------------------------------------------------------

import imageio as io

import math as m

from matplotlib import pyplot as plt

import numpy as np

import sys as s


# -----------------------------------------------------------------------------------------


def rotate(image_origin, angle, out_file_path):
    angle_radians = m.radians(angle * (-1))
    new_positions = np.zeros( (image_origin.shape[0], image_origin.shape[1], 2) )

    for (i, j), value in np.ndenumerate(image_origin):
        new_positions[i, j, 0] = max(min(round((i * m.cos(angle_radians)) - (j * m.sin(angle_radians))), image_origin.shape[0]-1), 0)
        new_positions[i, j, 1] = max(min(round((i * m.sin(angle_radians)) + (j * m.cos(angle_radians))), image_origin.shape[1]-1), 0)

    image_result = np.zeros(np.shape(image_origin))

    for (i, j), value in np.ndenumerate(image_origin):
        image_result[i, j] = image_origin[int(new_positions[i, j, 0]), int(new_positions[i, j, 1])]

    save_output_image(out_file_path, image_result)


# -----------------------------------------------------------------------------------------


def nearest_pixel(i, j, image, scale_factor_x, scale_factor_y):
    if m.isclose(float(scale_factor_x), float(1.0)) & m.isclose(float(scale_factor_y), float(1.0)):
        return image[i,j]
    else:
        old_i = max(min(i / scale_factor_x, image.shape[0]),0)
        old_j = max(min(j / scale_factor_y, image.shape[1]),0)

        diff1 = s.maxsize
        if 0 <= round(old_i) < image.shape[0] and 0 <= round(old_j) < image.shape[1]:
            diff1_x = abs(i - round(old_i))
            diff1_y = abs(j - round(old_j))
            diff1 = m.sqrt(m.pow(diff1_x, 2) + m.pow(diff1_y, 2))

        diff2 = s.maxsize
        if 0 <= round(old_i + 1) < image.shape[0] and 0 <= round(old_j) < image.shape[1]:
            diff2_x = abs(i - round(old_i + 1))
            diff2_y = abs(j - round(old_j))
            diff2 = m.sqrt(m.pow(diff2_x, 2) + m.pow(diff2_y, 2))

        diff3 = s.maxsize
        if 0 <= round(old_i) < image.shape[0] and 0 <= round(old_j + 1) < image.shape[1]:
            diff3_x = abs(i - round(old_i))
            diff3_y = abs(j - round(old_j + 1))
            diff3 = m.sqrt(m.pow(diff3_x, 2) + m.pow(diff3_y, 2))

        diff4 = s.maxsize
        if 0 <= round(old_i + 1) < image.shape[0] and 0 <= round(old_j + 1) < image.shape[1]:
            diff4_x = abs(i - round(old_i + 1))
            diff4_y = abs(j - round(old_j + 1))
            diff4 = m.sqrt(m.pow(diff4_x, 2) + m.pow(diff4_y, 2))

        minimum = min( (diff1, diff2, diff3, diff4) )

        if diff1 == diff2 == diff3 == diff4 == s.maxsize:
            return 0
        if diff1 == minimum:
            return image[round(old_i), round(old_j)]
        if diff2 == minimum:
            return image[round(old_i + 1), round(old_j)]
        if diff3 == minimum:
            return image[round(old_i), round(old_j + 1)]
        return image[round(old_i + 1), round(old_j + 1)]


# -----------------------------------------------------------------------------------------


def nearest_interpolation(image, out_file_path, scale_factor_x, scale_factor_y):
    #plt.imshow(rotated_image, cmap="gray", vmin=0, vmax=255)
    #plt.show()

    dim_x = round(image.shape[0] * scale_factor_x)
    dim_y = round(image.shape[1] * scale_factor_y)

    result_image = np.zeros( (dim_x, dim_y) )

    for (i, j), value in np.ndenumerate(result_image):
        result_image[i,j] = nearest_pixel(i, j, image, scale_factor_x, scale_factor_y)

    #plt.imshow(result_image, cmap="gray", vmin=0, vmax=255)
    #plt.show()

    save_output_image(out_file_path, result_image)


# -----------------------------------------------------------------------------------------


def bilinear_interpolation(image, out_file_path, scale_factor_x, scale_factor_y):
    dim_x = round(image.shape[0] * scale_factor_x)
    dim_y = round(image.shape[1] * scale_factor_y)

    result_image = np.zeros((dim_x, dim_y))

    for (i, j), value in np.ndenumerate(result_image):
        if m.isclose(float(scale_factor_x), float(1.0)) & m.isclose(float(scale_factor_y), float(1.0)):
            result_image[i,j] = image[i,j]
        else:
            old_i = max(min(i / scale_factor_x, image.shape[0]), 0)
            old_j = max(min(j / scale_factor_y, image.shape[1]), 0)

            weighted_sum = 0
            weight_sum = 0

            for a in range(0, 1):
                for b in range(0,1):
                    if 0 <= round(old_i + a) < image.shape[0] and 0 <= round(old_j + b) < image.shape[1]:
                        diff1_x = abs(i - round(old_i + a))
                        diff1_y = abs(j - round(old_j + b))
                        diff1 = m.sqrt(m.pow(diff1_x, 2) + m.pow(diff1_y, 2))
                        weighted_sum = weighted_sum + diff1 * image[round(old_i + a), round(old_j + b)]
                        weight_sum = weight_sum + diff1

            if weight_sum > 0:
                weighted_sum = weighted_sum / weight_sum
                result_image[i,j] = weighted_sum

    save_output_image(out_file_path, result_image)

# -----------------------------------------------------------------------------------------


def calc_r(s):
    v1 = m.pow(calc_p(s + 2), 3)
    v2 = m.pow(calc_p(s + 1), 3)
    v3 = m.pow(calc_p(s), 3)
    v4 = m.pow(calc_p(s - 1), 3)

    return (1 / 6) * (v1 - 4 * v2 + 6 * v3 - 4 * v4)


# -----------------------------------------------------------------------------------------


def calc_p(t):
    if t > 0:
        return t
    return 0


# -----------------------------------------------------------------------------------------


def bicubic_interpolation(image, out_file_path, scale_factor_x, scale_factor_y):
    dim_x = round(image.shape[0] * scale_factor_x)
    dim_y = round(image.shape[1] * scale_factor_y)

    result_image = np.zeros((dim_x, dim_y))

    for (i, j), value in np.ndenumerate(result_image):
        if m.isclose(float(scale_factor_x), float(1.0)) & m.isclose(float(scale_factor_y), float(1.0)):
            result_image[i,j] = image[i,j]
        else:
            x = int(i / scale_factor_x)
            y = int(j / scale_factor_y)
            dx = (i / scale_factor_x) - x
            dy = (j / scale_factor_y) - y

            sum_value = 0

            for a in range(-1, 3):
                for b in range(-1, 3):
                    normalized_x = min(x + a, image.shape[0] - 1)
                    normalized_y = min(y + b, image.shape[1] - 1)
                    sum_value = sum_value + image[normalized_x, normalized_y] * calc_r(a - dx) * calc_r(dy - b)

            result_image[i, j] = sum_value

    save_output_image(out_file_path, result_image)


# -----------------------------------------------------------------------------------------


def lagrange_function(dx, x, y, n, image):
    first_part = 0
    second_part = 0
    third_part = 0
    fourth_part = 0

    if 0 <= (x-1) < image.shape[0] and 0 <= (y+n-2) < image.shape[1]:
        first_part = (-1) * dx * (dx-2) * image[x-1, y+n-2]

    if 0 <= (x) < image.shape[0] and 0 <= (y+n-2) < image.shape[1]:
        second_part = (dx+1) * (dx-1) * (dx-2) * image[x, y+n-2]

    if 0 <= (x+1) < image.shape[0] and 0 <= (y+n-2) < image.shape[1]:
        third_part = (-1) * dx * (dx+1) * (dx-2) * image[x+1, y+n-2]

    if 0 <= (x+2) < image.shape[0] and 0 <= (y+n-2) < image.shape[1]:
        fourth_part = dx * (dx+1) * (dx-1) * image[x+2, y+n-2]

    return (first_part/6) + (second_part/2) + (third_part/2) + (fourth_part/6)


# -----------------------------------------------------------------------------------------


def lagrange_interpolation_piece(i, j, scale_factor_x, scale_factor_y, rotated_image):
    x = int(i / scale_factor_x)
    y = int(j / scale_factor_y)
    dx = (i / scale_factor_x) - x
    dy = (j / scale_factor_y) - y

    ls = np.zeros((4))
    for a in range(-1, 3):
        ls[a + 1] = lagrange_function(dx, x, y, a, rotated_image)

    first_part = (-1) * dy * (dy - 1) * (dy - 2) * ls[0]
    second_part = (dy + 1) * (dy - 1) * (dy - 2) * ls[1]
    third_part = (-1) * dy * (dy + 1) * (dy - 2) * ls[2]
    fourth_part = dy * (dy + 1) * (dy - 1) * ls[3]

    return (first_part / 6) + (second_part / 2) + (third_part / 2) + (fourth_part / 6)


# -----------------------------------------------------------------------------------------


def lagrange_interpolation(image, out_file_path, scale_factor_x, scale_factor_y):
    dim_x = round(image.shape[0] * scale_factor_x)
    dim_y = round(image.shape[1] * scale_factor_y)

    result_image = np.zeros((dim_x, dim_y))

    if m.isclose(float(scale_factor_x), float(1.0)) & m.isclose(float(scale_factor_y), float(1.0)):
        result_image = image
    else:
        for (i, j), value in np.ndenumerate(result_image):
            x = int(i / scale_factor_x)
            y = int(j / scale_factor_y)
            dx = (i / scale_factor_x) - x
            dy = (j / scale_factor_y) - y

            ls = np.zeros((4))
            for a in range(-1, 3):
                ls[a+1] = lagrange_function(dx, x, y, a, image)

            first_part = (-1) * dy * (dy-1) * (dy-2) * ls[0]
            second_part = (dy+1) * (dy-1) * (dy-2) * ls[1]
            third_part = (-1) * dy * (dy+1) * (dy-2) * ls[2]
            fourth_part = dy * (dy+1) * (dy-1) * ls[3]

            result_image[i,j] = (first_part/6) + (second_part/2) + (third_part/2) + (fourth_part/6)

    save_output_image(out_file_path, result_image)


# -----------------------------------------------------------------------------------------


def save_output_image(out_file_path, result_image):
    print()
    print("Saving file", out_file_path, "...")
    plt.imsave(out_file_path, result_image, cmap="gray", vmin=0, vmax=255)
    print("Saved!")
    print()
    print("END")
    print()
    print()


# -----------------------------------------------------------------------------------------


def resolve_execution_sfxy(image, out_file_path, method, scale_factor_x, scale_factor_y):
    if method == "1":
        nearest_interpolation(image, out_file_path, scale_factor_x, scale_factor_y)
    elif method == "2":
        bilinear_interpolation(image, out_file_path, scale_factor_x, scale_factor_y)
    elif method == "3":
        bicubic_interpolation(image, out_file_path, scale_factor_x, scale_factor_y)
    elif method == "4":
        lagrange_interpolation(image, out_file_path, scale_factor_x, scale_factor_y)
    else:
        print("Invalid method")
        exit(-1)


# -----------------------------------------------------------------------------------------


def resolve_execution_xy(image, out_file_path, method, x, y):
    scale_factor_x = x/image.shape[1]
    scale_factor_y = y/image.shape[0]
    resolve_execution_sfxy(image, out_file_path, method, scale_factor_x, scale_factor_y)


# -----------------------------------------------------------------------------------------


def resolve_execution_sf(image, out_file_path, method, scale_factor):
    resolve_execution_sfxy(image, out_file_path, method, scale_factor, scale_factor)


# -----------------------------------------------------------------------------------------


file_path = s.argv[1]
out_file_path = s.argv[2]
method = s.argv[3]

angle = 0.0
scale_factor = -1.0
x = -1.0
y = -1.0

if method == '0':
    angle = float(s.argv[4])
else:
    print()
    if len(s.argv) == 5:
        scale_factor = float(s.argv[4])
        print("Using scale factor", scale_factor)
        print()
    elif len(s.argv) == 6:
        x = float(s.argv[4])
        y = float(s.argv[5])
        print("Using dimensions", x, "and",y)
    else:
        print("Cannot resolve execution using this combination of parameters")
        exit(-1)

print("Loading file", file_path, "...")

image = io.imread(file_path, "PNG-PIL", as_gray=True)

if method == '0':
    rotate(image, angle, out_file_path)
else:
    if float(x) > float(0.0) and float(y) > float(0.0):
        resolve_execution_xy(image, out_file_path, method, x, y)
    else:
        resolve_execution_sf(image, out_file_path, method, scale_factor)
