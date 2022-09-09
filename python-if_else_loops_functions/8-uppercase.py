#!/usr/bin/python3
def uppercase(str):
   PEPEXTO = ""
   for PEPE1 in range(len(str)):
       if ord(str[PEPE1]) > 96 and ord(str[PEPE1]) < 123:
           PEPEXTO = PEPEXTO + chr(ord(str[PEPE1]) - 32)
           continue
       PEPEXTO = PEPEXTO + str[PEPE1]
   print("{}".format(PEPEXTO))
