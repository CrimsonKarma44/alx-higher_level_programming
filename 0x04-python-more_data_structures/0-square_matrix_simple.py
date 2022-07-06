#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    listd = []
    for i in matrix:
        mapped = list(map(lambda x: x**2, i))
        listd.append(mapped)
    return (listd)
