#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 4
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import imageio as io

import sys as s

#-----------------------------------------------------------------------------------------

def rotate_image(image, out_file_path, angle):
    return

#-----------------------------------------------------------------------------------------

def resize_using_scale_factor(image, out_file_path, scale_factor, interpolation_method):
    return

#-----------------------------------------------------------------------------------------

def resize_using_dimensions(image, out_file_path, x, y, interpolation_method):
    return

#-----------------------------------------------------------------------------------------

file_path = s.argv[1]
out_file_path = s.argv[2]
option = s.argv[3]
param1 = s.argv[4]


if option == 'd' | option == 'e':
    param2 = s.argv[5]
    if(option == 'd'):
        param3 = s.argv[6]

print("Lendo arquivo", file_path, "...")

image = io.imread(file_path, "PNG-PIL", as_gray=True)

if option == 'a':
    rotate_image(image, out_file_path, param1)
elif option == 'e':
    resize_using_scale_factor(image, out_file_path, param1, param2)
elif option == 'd':
    resize_using_dimensions(image, out_file_path, param1, param2, param3)
else:
    print()
    print("Escolha uma opção válida")
    print()
    print("'a' para rotação")
    print("'e' para redimensionamento por fator de escala")
    print("'d' para redimensionamento por novas medidas")
