#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuplita = (len(sentence), sentence[0:1],)
        return tuplita
    else:
        tuplita = (0, None,)
        return tuplita
