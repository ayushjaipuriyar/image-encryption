import numpy as np
import itertools

# Define the matrix
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


def set_creator(matrix):
    # Create a dictionary to store the neighbors for each element
    neighbor_dict = {}

    # Loop through each element in the matrix
    for i in range(4):
        for j in range(4):
            # Initialize the set of neighbors
            neighbors = set()

            # Check the neighboring elements and add them to the set
            if i > 0 and j > 0:
                neighbors.add(matrix[i-1][j-1])
            if i > 0:
                neighbors.add(matrix[i-1][j])
            if i > 0 and j < 3:
                neighbors.add(matrix[i-1][j+1])
            if j > 0:
                neighbors.add(matrix[i][j-1])
            if j < 3:
                neighbors.add(matrix[i][j+1])
            if i < 3 and j > 0:
                neighbors.add(matrix[i+1][j-1])
            if i < 3:
                neighbors.add(matrix[i+1][j])
            if i < 3 and j < 3:
                neighbors.add(matrix[i+1][j+1])

            # Add the set of neighbors to the dictionary
            neighbor_dict[matrix[i][j]] = neighbors

    # Print the dictionary of neighbors
    return neighbor_dict


og_ne = set_creator(matrix)

value = 0
for key in og_ne:
    ins = og_ne[key].intersection(og_ne[key])
    value -= len(ins)

permutations = set(itertools.permutations(matrix.flatten()))

for i, perm in enumerate(permutations):
    print(f"Permutation {i+1}:")
    x = set_creator(np.array(perm).reshape(4, 4))
    z = 0
    for key in og_ne:
        ins = og_ne[key].intersection(x[key])
        z -= len(ins)
    value = min(value, z)
