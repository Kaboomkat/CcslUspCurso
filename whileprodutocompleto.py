# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:32:20 2024

@author: rodri

usuário define quantos números serão digitados
"""
tamanho = int(input('Digite o tamanho da sequência de números: '))

i = 0

produto = 1

while i < tamanho:
    valor = float(input('Digite um valor à ser mu5ltiplicado: '))
    produto = produto * valor
    i += 1
    
print(f'O produto dos valores digitados é: {produto}')