# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:35:58 2024

@author: rodri
"""

n1 = int(input('Digite um número inteiro: '))
soma = 0
while n1 != 0:
    n2 = n1 % 10
    soma = soma + n2
    n1 = n1 // 10
print(soma)