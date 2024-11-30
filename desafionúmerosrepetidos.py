# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:32:27 2024

@author: rodri
"""

n1 = int(input('Digite um número: '))
repete = False

while n1 != 0 and not repete:
    n2 = n1 % 10
    n1 = n1 // 10
    n3 = n1 % 10
    if n2 == n3:
        repete = True
if n1 == 0:
    print('Não existem dígitos que se repetem no número.')
else:
    print(f'Existe um número que se repete, o {n2}')
