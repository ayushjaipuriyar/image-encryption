import itertools
import numpy as np
# Define the possible values for the matrix elements
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Generate all possible permutations of the values
permutations = itertools.permutations(values)

# Iterate over the permutations and check if each one is a valid matrix
for perm in permutations:
    matrix = np.reshape(perm, (4, 4))
    valid_matrix = True
    for i in range(4):
        for j in range(4):
            # Check if any adjacent element (excluding diagonals) has the same value
            neighbors = []
            if i > 0:
                neighbors.append(matrix[i-1][j])
            if i < 3:
                neighbors.append(matrix[i+1][j])
            if j > 0:
                neighbors.append(matrix[i][j-1])
            if j < 3:
                neighbors.append(matrix[i][j+1])
            if len(set(neighbors)) != len(neighbors):
                valid_matrix = False
                break
        if not valid_matrix:
            break
    if valid_matrix:
        print(matrix)
