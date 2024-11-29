# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:25:12 2024

@author: rodri
"""
print('Digite uma sequência de valores terminada pelo número 0')

soma = 0
valor = 1
while valor != 0:
    valor = float(input('Digite um valor a ser somado: '))
    soma = soma + valor
    
print(f'A soma dos valores digitados é: {soma}')
