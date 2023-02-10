from PIL import Image
import random
from numpy import array
import numpy as np
img = Image.open('Lena.png')

ar = array(img)
shuffled = np.zeros((512, 512), dtype=int)


def key_gen(r, c):
    R = 3.99
    random_float = random.uniform(0, 1)
    x = 0.4+(random_float/5)
    key = np.zeros((r, c))
    for i in range(0, r):
        for j in range(0, c):
            x = x*R*(1-x)
            key[i][j] = x*255

    return key


def shuffler(matrix, n):
    for i in range(16):
        matrix[i][0], matrix[i][3] = matrix[i][3], matrix[i][0]
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    print(n % 16)
    matrix = [list(reversed(row)) for row in zip(*matrix)]
    return matrix


def compile(matrix, i, j):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            shuffled[i+m][j+n] = matrix[m][n]


# New is the 16x16 matrix needed for further processing
new = np.zeros((16, 16), dtype=int)
i, j = 0, 0
count = 0
while i < len(ar):
    while j < len(ar[i]):
        p, q = 0, 0
        for m in range(i, i+16):
            q = 0
            for n in range(j, j+16):
                new[p][q] = ar[m][n]
                q += 1
            p += 1
        # shuffled_img3 = Image.fromarray(new.astype(np.uint16))
        new = shuffler(new, count)
        compile(new, i, j)
        j += 16
        count += 1
    i += 16
    j = 0


key = key_gen(len(ar), len(ar[0]))
for i in range(len(ar)):
    for j in range(len(ar[i])):
        shuffled[i][j] = int(shuffled[i][j]) ^ int(key[i][j])
print(correlation_coefficient(ar, shuffled))
k = Image.fromarray(shuffled.astype(np.uint8))
k.save('./pics/final.png')

loc1 = './Lena.png'
loc2 = 'pics/final.png'


def sumofpixelval(height, width, img1, img2):
    matrix = np.empty((width, height))
    for y in range(width):
        for x in range(height):
            if img1[x, y] == img2[x, y]:
                matrix[x, y] = 0
            else:
                matrix[x, y] = 1
    psum = 0
    for y in range(width):
        for x in range(height):
            psum = matrix[x, y]+psum
    return psum


def npcr(img1, img2):
    height, width = img1.shape
    npcrv = ((sumofpixelval(height, width, img1, img2)/(height*width))*100)
    return npcrv


print(npcr(ar, shuffled))


def uaci(img1, img2):
    height, width = img1.shape
    value = 0
    for y in range(height):
        for x in range(width):
            value += (abs(int(img1[x, y])-int(img2[x, y])))
    value = value*100/(width*height*255)
    return value


print(uaci(ar, shuffled))


def correlation_coefficient(img1, img2):
    # Ensure that the images have the same shape
    assert img1.shape == img2.shape, "The images have different shapes"

    # Calculate the mean of the image
    mean1 = np.mean(img1)
    mean2 = np.mean(img2)

    # Calculate the standard deviation of the images
    std1 = np.std(img1)
    std2 = np.std(img2)

    # Subtract the mean from each pixel and divide by the standard deviation
    normalized_img1 = (img1 - mean1) / std1
    normalized_img2 = (img2 - mean2) / std2

    # Calculate the sum of the product of the corresponding pixels
    sum_of_products = np.sum(normalized_img1 * normalized_img2)

    # Calculate the correlation coefficient
    return sum_of_products / (img1.size - 1)
