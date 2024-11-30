# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:39:21 2024

@author: rodri
"""

valor = 1 
decrescente = True
anterior = int(input('Digite o primeiro número de uma sequência decrescente '))
while valor != 0 and decrescente:
    valor = int(input('Digite o próximo número da sequência: '))
    if valor >= anterior:
        decrescente = False
    anterior = valor
if valor == 0:
    print('A sequência chegou ao fim, em ordem decrescente. :-)')
else:
    print('A sequência não é mais decrescente. :-(')