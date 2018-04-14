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
text_path = s.argv[2]
bits_plan = s.argv[3]
result_file_path = s.argv[4]

print("Lendo arquivo", file_path, "...")

# loading the PNG into a ndarray
image = misc.imread(file_path, False, "RGB")

misc.imsave(result_file_path, image)

textfile  = open(text_path, 'r')
text = ""
for line in textfile:
     text = text + line

# ISTO FUNCIONA!!! EEEEEE
bin_text = bin(int.from_bytes(text.encode(), 'big'))

print(len(bin_text))

#print(bin_text)

n = int(bin_text, 2)
#other_text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

#print(other_text)

bits = [( n >> bit) & 1 for bit in range(len(bin_text) - 1, -1, -1)]

print(len(bits))
