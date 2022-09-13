#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuplita = (len(sentence), sentence[1:2],)
        return tuplita
    else:
        tuplita = ("None", 0)
