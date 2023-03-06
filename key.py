import random
import numpy as np
import math


def key_gen(r, c, x=None):
    """ 
    Generate logistic chaotic map
    Argumets:
        r : row of the 2d map required
        c : col of the 2d map required
        x :  initial value of x in logistic function
    Returns:
        matrix of logictic chaotic map
     """
    R = 3.99
    random_float = random.uniform(0, 1)
    x = 0.4+(random_float/5)
    key = np.zeros((r, c))
    for i in range(0, r):
        for j in range(0, c):
            x = x*R*(1-x)
            key[i][j] = x*255

    return key


def pixel_key(r, x=None):
    """ 
    Generate logistic chaotic map
    Argumets:
        r : row of the 2d map required
        c : col of the 2d map required
        x :  initial value of x in logistic function
    Returns:
        matrix of logictic chaotic map
     """
    R = 3.99
    random_float = random.uniform(0, 1)
    x = 0.4+(random_float/5)
    generated_key = np.zeros(r)
    for i in range(0, r):
        x = x*R*(1-x)
        generated_key[i] = x*511
    generated_key = np.trunc(generated_key).astype(int)
    generated_key = generated_key[(generated_key <= 511)]
    keys = []
    for value in generated_key:
        if value not in keys:
            keys.append(value)
    keys_set = set(keys)
    vals = set(range(512))
    rest = vals.difference(keys_set)
    for i in rest:
        x = random.randint(0, len(keys))
        keys.insert(x, i)
    return keys


def keyxor(matrix, key):
    """
    Xor the image with the key
    Argumets:
        matrix : 2d numpy matrix , the image as a matrix
        key : the key generated from the chaotic function
    Returns:
        2d numpy array of the image after adding of the key
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j]) ^ int(key[i][j])

    return matrix
