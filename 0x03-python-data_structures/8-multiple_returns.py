#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    mult = length, first
    if len(sentence) == 0:
        first = None
    return mult
