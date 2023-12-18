#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    count = 0

    while count < list_length:
        try:
            result = my_list_1[count] / my_list_2[count]
            count += 1
        except ZeroDivisionError:
            result = 0
            count += 1
            print("division by 0")
        except IndexError:
            result = 0
            count += 1
            print("out of range")
        except TypeError:
            result = 0
            count += 1
            print("wrong type")
        finally:
            results.append(result)
    return results
