#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of "
if number < 0:
    lt = -(-number % 10)
elif number >= 0:
    lt = number % 10
if lt > 5:
    print(s + str(number) + " is " + str(lt) + " and is greater than 5")
elif lt == 0:
    print(s + str(number) + " is " + str(lt) + " and is 0")
else:
    print(s + str(number) + " is " + str(lt) + " and is less than 6 and not 0")
