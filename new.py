from PIL import Image
from numpy import array
import numpy as np
import key
import analysis
import random

img = Image.open('Lena.png')
ar = array(img)
height, width = ar.shape
keys = key.key_gen(height, width)


def shuffle(matrix):
    #   [[5, 9, 13, 6],
    #   [8, 1, 12, 4],
    #   [3, 2, 7, 15],
    #   [11, 0, 14, 10]]
    # [[0, 1, 2, 3],
    #    [4, 5, 6, 7],
    #    [8, 9, 10, 11],
    #    [12, 13, 14, 15]]
    shuffled = np.zeros((4, 4), dtype=int)
    shuffled[0, 0] = matrix[1, 1]
    shuffled[0, 1] = matrix[2, 1]
    shuffled[0, 2] = matrix[3, 1]
    shuffled[0, 3] = matrix[1, 2]
    shuffled[1, 0] = matrix[2, 0]
    shuffled[1, 1] = matrix[0, 1]
    shuffled[1, 2] = matrix[3, 0]
    shuffled[1, 3] = matrix[1, 0]
    shuffled[2, 0] = matrix[0, 3]
    shuffled[2, 1] = matrix[0, 2]
    shuffled[2, 2] = matrix[1, 3]
    shuffled[2, 3] = matrix[3, 3]
    shuffled[3, 0] = matrix[2, 3]
    shuffled[3, 1] = matrix[0, 0]
    shuffled[3, 2] = matrix[3, 2]
    shuffled[3, 3] = matrix[2, 2]
    return shuffled


s = np.copy(ar)


def shuffler(s):
    for i in range(509):
        for j in range(509):
            submatrix = s[i:i+4, j:j+4]
            changes = shuffle(submatrix)
            s[i:i+4, j:j+4] = changes
    return s


s = shuffler(s)


def hell_shuffle(s):
    s1 = np.zeros((0, 512), dtype=np.int8)
    s2 = np.zeros((0, 512), dtype=np.int8)
    shuffled = np.zeros((512, 512))
    for _ in range(0, 512):
        k = key.pixel_key(5000)
        s1 = np.append(s1, [k], axis=0)

    for _ in range(0, 512):
        k = key.pixel_key(5000)
        s2 = np.append(s2, [k], axis=0)
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            x = s1[i, j]
            y = s2[i, j]
            shuffled[i, j] = s[x, y]
            # keys[i, j] = (s1[i, j], s2[i, j])
    return shuffled
    # k2 = key.pixel_key(5000)
    # lk = np.copy(s)
    # print(k2)
    # return lk

# k1 = key.pixel_key(5000)
# k2 = key.pixel_key(5000)
# lk = open('./lk.txt', 'w')
# for i in k1:
#     for j in k2:
#         lk.write("{},{}\n".format(i, j))


def diffusion(s):
    shuffled = np.zeros((512, 0))
    k = key.pixel_key(512)
    for i in range(len(s)):
        x = k.index(i)
        c = s[:, [x]]
        shuffled = np.append(shuffled, c, axis=1)
    return shuffled


lk = hell_shuffle(s)
# print(lk)
lk = diffusion(lk)
k = Image.fromarray(lk.astype(np.uint8))
k.save('./pics/beforekeynew.png')


# Applying key
lk = key.keyxor(lk, keys)


# analysis
print("CC: ", analysis.correlation_coefficient(ar, lk))
k = Image.fromarray(lk.astype(np.uint8))
k.save('./pics/afterkeynew.png')

img2 = np.copy(ar)
x = random.randint(0, 254)
y = random.randint(0, 254)
img2[x][y] = random.randint(0, 254)
img2 = key.keyxor(img2, keys)
analysis.histogram(ar, lk)
npcr, uaci = analysis.NPCR_UACI_worker(ar, img2)
print("npcr: ", npcr, "%\tUaci: ", uaci, "%")
print("Entropy", analysis.entropy(lk))
