#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for num1 in range(0, len(matrix)):
            for num2 in range(0, len(matrix[num1])):
                print("{:d} ".format(matrix[num1][num2]), end="")
