#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for num1 in matrix:
            for num2 in num1:
                if num2 == num1[(len(num1) - 1)]:
                    print("{:d}".format(num2), end="")
                else:
                    print("{:d} ".format(num2), end="")
            print("")
