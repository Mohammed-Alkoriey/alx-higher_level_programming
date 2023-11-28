#!/usr/bin/python3
print("0" + str(0), end = '')
i = 1
while i < 100:
    if i < 10:
        print(", 0".format() + str(i),end = '')
    else:
        print(", ".format() + str(i),end = '')
    i += 1
