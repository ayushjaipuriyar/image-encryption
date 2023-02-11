from PIL import Image
import random
from numpy import array
import numpy as np
import key
import analysis
img = Image.open('Lena.png')

ar = array(img)
shuffled = np.zeros((512, 512), dtype=int)


def shuffler(matrix, n):
    for i in range(4):
        matrix[i][0], matrix[i][3] = matrix[i][3], matrix[i][0]
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    matrix = [list(reversed(row)) for row in zip(*matrix)]
    return matrix


def compile(matrix, i, j):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            shuffled[i+m][j+n] = matrix[m][n]


# New is the 4x4 matrix needed for further processing
new = np.zeros((4, 4), dtype=int)
i, j = 0, 0
count = 0
while i < len(ar):
    while j < len(ar[i]):
        p, q = 0, 0
        for m in range(i, i+4):
            q = 0
            for n in range(j, j+4):
                new[p][q] = ar[m][n]
                q += 1
            p += 1
        # shuffled_img3 = Image.fromarray(new.astype(np.uint4))
        new = shuffler(new, count)
        compile(new, i, j)
        j += 4
        count += 1
    i += 4
    j = 0


keys = key.key_gen(len(ar), len(ar[0]))
# print(key)

shuffled = key.keyxor(shuffled, keys)
print("CC: ", analysis.correlation_coefficient(ar, shuffled))
k = Image.fromarray(shuffled.astype(np.uint8))
k.save('./pics/final.png')

# loc1 = './Lena.png'
# loc2 = 'pics/final.png'

analysis.histogram(ar, shuffled)
npcr, uaci = analysis.NPCR_UACI_worker(ar)
print("npcr: ", npcr, "%\tUaci: ", uaci)
print(analysis.entropy(ar))
# print(uaci(ar, shuffled))
# print("BCR:", analysis.bit_correct_ratio(ar, shuffled))
