#!/usr/bin/python3
i = 0
while i < 100:
    if i == 0:
        message = "0" + str(i)
    elif i < 10:
        message = ", 0".format() + str(i)
    else:
        message = ", ".format() + str(i)
    print(message, end='')
    i += 1
print()
