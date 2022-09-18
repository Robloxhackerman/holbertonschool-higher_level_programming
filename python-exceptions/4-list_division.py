#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listita = []
    PEPE = 0
    for PEPE1 in range(0, list_length):
        try:
            PEPE = my_list_1[PEPE1] / my_list_2[PEPE1]
        except TypeError:
            PEPE = 0
            print("wrong type")
        except ZeroDivisionError:
            PEPE = 0
            print("division by 0")
        except IndexError:
            PEPE = 0
            print("out of range")
        finally:
            pass
        listita.append(PEPE)
    return listita
