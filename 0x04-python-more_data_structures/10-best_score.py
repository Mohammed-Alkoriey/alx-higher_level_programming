#!/usr/bin/python3

def best_score(a_dictionary):
    best = 0
    best_key = ""
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > best:
                best = value
                best_key = key
            else:
                continue
        return best_key
    else:
        return None
