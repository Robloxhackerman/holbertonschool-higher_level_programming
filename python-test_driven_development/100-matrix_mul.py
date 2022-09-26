#!/usr/bin/python3
"""Matrix resurrection"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    
    for PEPE1 in m_a:
        if not isinstance(PEPE1, list):
            raise TypeError("m_a must be a list of lists")
        for PEPE2 in PEPE1:
            if type(PEPE2) in (int, float):
                raise TypeError("m_a should contain only integers or floats")
        if len(PEPE1) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
    
    for PEPE3 in m_b:
        if not isinstance(PEPE2, list):
            raise TypeError("m_a must be a list of lists")
        for PEPE4 in PEPE3:
            if type(PEPE3) in (int, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(PEPE3) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    PEPON = [[0 for a in m_b[0]] for PEPE5 in m_a]
    for PEPE6 in range(len(m_a)):
        for PEPE7 in range(len(m_b[0])):
            for PEPE8 in range(len(m_b)):
                final[PEPE6][PEPE7] += m_a[PEPE6][PEPE8] * m_b[PEPE8][PEPE7]

    return PEPON
