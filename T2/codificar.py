#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 2
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s
import scipy as sp
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

textfile  = open(text_path, 'r')
text = ""
for line in textfile:
     text = text + line

# converting the text into binary
bin_text = bin(int.from_bytes(text.encode(), 'big'))

n = int(bin_text, 2)

# converting binary into a flat ndarray of bits
bits = sp.array([( n >> bit) & 1 for bit in range(len(bin_text) - 1, -1, -1)])

# resizing the array of bits into a ndarray with same shape of the image
# when the new shape is bigger than the last one scipy fills with zero
bits.resize(image.shape)

# preparing the ndarray to be used in a bitwise-or operation
bits = bits << int(bits_plan)

# finally inserting the message into the image using a bitwise operation
image = image | bits

# saving the image with the message
misc.imsave(result_file_path, image)
