# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:56:16 2024

@author: rodri
"""

mycard = int(input('Digite o número do seu cartão de crédito: '))
cardread = 1-
encontrei = False
while cardread != 0 and not encontrei:
    cardread = int(input('Digite o número do cartão de crédito: '))
    if cardread == mycard:
        encontrei = True
if encontrei:
    print('O cartão foi encontrado no sistema.')
else:
    print('O cartão não foi encontrado')