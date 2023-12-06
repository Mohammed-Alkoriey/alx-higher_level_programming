#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in range(0, len(matrix)):
        squ_mat = map(lambda num: num * num, matrix[i])
        row = list(squ_mat)
        new_mat.append(row)
    return new_mat
