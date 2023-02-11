
import numpy as np
import random

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


# Differential Attakcs NPCR & UACI

def NPCR(img1, img2):
    """ 
    Calculate the NPCR value
    Arguments:
        img1 = Encrypted image 1
        img2 = Encrypted image 2 with one pixel changed 
    Returns:
        NPCR value
     """
    height, width = img1.shape
    sum = 0
    for i in range(h):
        for j in range(w):
            if img1[x, y] != img2[x, y]:
                sum+1
    res = ((sum)/(w*h))*100
    return res


def NPCR_worker(img1):
    img2 = np.copy(img1)
    img2[random.randint(0, 254)][random.randint(0, 254)]


def uaci(img1, img2):
    height, width = img1.shape
    value = 0
    for y in range(height):
        for x in range(width):
            value += (abs(int(img1[x, y])-int(img2[x, y])))
    value = value*100/(width*height*255)
    return value
