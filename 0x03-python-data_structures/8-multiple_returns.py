#!/usr/bin/python3

def multiple_returns(sentence):
    leng = len(sentence)
    if leng > 0:
        first_char = sentence[0]
        return leng, first_char
    else:
        return None
