# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:48:19 2024

@author: rodri
"""

n1 = int(input('Digite um número inteiro: '))
repete = False

while n1 != 0 and not repete:
    n2 = n1 % 10
    n1 = n1 // 10
    n3 = n1 % 10
    if n2 == n3:
        repete = True
if n1 == 0:
    print('não')
else:
    print('sim')