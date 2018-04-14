#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 2
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s
from scipy import misc

# python codificar.py imagem_entrada.png texto_entrada.txt plano_bits imagem_saida.png
# python decodificar.py imagem_saida.png plano_bits texto_saida.txt

#-----------------------------------------------------------------------------------------

# receiving the parameters
file_path = s.argv[1]
bits_plan = s.argv[2]
result_file_path = s.argv[3]

print("Lendo arquivo", file_path, "...")

# loading the PNG into a ndarray
image = misc.imread(file_path, False, "RGB")

#n = int(bin_text, 2)
#other_text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

#print(other_text)
