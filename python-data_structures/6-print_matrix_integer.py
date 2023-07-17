#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix)
    size2 = len(matrix[0])
    if size2 == 0:
        print()
    else:
        for i in range(size):
            for j in range(size2):
                if j + 1 == size2:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=' ')
