#!/usr/bin/python3
print("0" + str(0), end='')
i = 0
while i < 100:
    if i < 10:
        message = ", 0".format() + str(i)
    else:
        message = ", ".format() + str(i)
    print(message, end='')
    i += 1
