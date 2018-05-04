#-----------------------------------------------------------------------------------------
# MC920 - TRABALHO 3
#
# FABIO TAKAHASHI TANNIGUCHI - RA 145980
#
#-----------------------------------------------------------------------------------------

import sys as s
from scipy import misc
import matplotlib as plt

#-----------------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------------

# receiving the (image) file path
file_path = s.argv[1]
align_mode = s.argv[2]
out_file_path = s.argv[3]

print("Lendo arquivo", file_path, "...")

# loading the PNG into a ndarray
image = misc.imread(file_path, True)

