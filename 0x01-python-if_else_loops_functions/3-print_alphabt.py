#!/usr/bin/python3
alpha = "abcdefghijklmnopqrstuvwxyz"
for let in alpha:
    if let == 'q' or let == 'e':
        continue
    print(let.format(), end='')
