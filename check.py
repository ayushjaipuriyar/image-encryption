from PIL import Image
from numpy import array
import numpy as np
import key
import analysis
img = Image.open('Lena.png')

ar = array(img)
height, width = ar.shape
keys = key.key_gen(height, width)
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
def get_mini_square():
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


def shuffle_2d_array(array):
    flat_array = array.flatten()
    permuted_indices = np.random.permutation(flat_array.shape[0])
    flat_array = flat_array[permuted_indices]
    shuffled_array = flat_array.reshape(array.shape)
    return shuffled_array


# shuffled = shuffle_2d_array(shuffled)


def shuffle_image(image, window_size):
    rows, cols = image.shape

    copy_image = image.copy()

    for r in range(0, rows, window_size):
        for c in range(0, cols, window_size):
            window = image[r:r+window_size, c:c+window_size]

            permuted_indices = np.random.permutation(window_size**2)

            window = window.flatten()[permuted_indices].reshape(
                window_size, window_size)

            copy_image[r:r+window_size, c:c+window_size] = window

    return copy_image


# shuffled = shuffle_image(ar, 16)


def shuffle_arr(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(0, row):
        for j in range(0, col):
            arr[i][j] = ((row*row)+i+1) % 256
    for i in range(0, int(row/4)):
        for j in range(int(col/4)):
            arr[i][j] = (row*row + 1) % 256 - arr[i][j]
    for i in range(0, int(row/4)):
        for j in range(3*int(col/3), col):
            arr[i][j] = ((row*row)+1) % 256-arr[i][j]
    for i in range(3*(int(row/4)), row):
        for i in range(0, int(col/4)):
            arr[i][j] = (row*row+1) % 256 - arr[i][j]
    for i in range(int(row/4), 3*int(row/4)):
        for j in range(int(col/4), 3*int(col/4)):
            arr[i][j] = (row*row+1) % 256 - arr[i][j]

    temp = np.array(arr)

    for i in range(0, row):
        for j in range(0, col):
            rowindex = int((arr[i][j]-1) % row)
            colindex = int((arr[i][j]-1)/col)
            temp[i][j] = arr[rowindex][colindex]

    return temp


shuffled = shuffle_arr(ar)


# Applying key
shuffled = key.keyxor(shuffled, keys)


# analysis
print("CC: ", analysis.correlation_coefficient(ar, shuffled))
k = Image.fromarray(shuffled.astype(np.uint8))
k.save('./pics/final.png')

analysis.histogram(ar, shuffled)
npcr, uaci = analysis.NPCR_UACI_worker(ar)
print("npcr: ", npcr*100000, "%\tUaci: ", uaci*100000, "%")
print("Entropy", analysis.entropy(shuffled))
