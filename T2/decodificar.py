#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 2
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s
from scipy import misc

# this code has to be run with input parameters:
#
# python decodificar.py imagem.png plano_bits decodificada.png
#
# 1 - image path
# 2 - int number of the bits plan to be decoded
# 3 - result image path
#

#-----------------------------------------------------------------------------------------

# receiving the parameters
file_path = s.argv[1]
bits_plan = s.argv[2]
result_file_path = s.argv[3]

print("Carregando imagem em", file_path, "...")

# loading the PNG into a ndarray
image = misc.imread(file_path, False, "RGB")

flatten_ndarray = image.flatten()

flatten_ndarray = (flatten_ndarray & (1 << int(bits_plan))) >> int(bits_plan)

result_image = (image & (1 << int(bits_plan))) >> int(bits_plan)
result_image = result_image * 255

print("Escrevendo resultado em", result_file_path, "...")
misc.imsave(result_file_path, result_image)

print("Finalizado!")
