# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:54:14 2024

@author: rodri
"""
import math
from sys import exit

print('Você está tentando achar o valor das raízes de uma equação quadrática (a*x**2 + b*x + c == 0) não é?\n\nSou um programa de computador, e vou te ajudar!')
print()
print('Primeiro, você vai me informar quais que são os valores das constantes a, b e c.')
print()
a = float(input('Qual o valor da constante a? '))
if a == 0:
    exit('Equações de segundo grau não podem ter "a" = 0')
b = float(input('Qual o valor da constante b? '))
c = float(input('Qual o valor da constante c? '))

delta = b ** 2 - 4 * a * c

print()
print('Agora, eu vou fazer *MÁGICA* (matemática), e te informar o valor das raízes que resolvem a equação que você me forneceu!')
print()


if delta < 0:
    print('Δ<0, então não existem soluções reais para essa equação!')
    
elif delta > 0:
    x1 = ( - b + math.sqrt(delta))/ (a * 2) 
    x2 = ( - b - math.sqrt(delta))/ (a * 2) 
    print(f'As raízes dessa equação são {x1} e {x2}!')
    print()
    
else: 
    x3 = ( - b + math.sqrt(delta)/ a * 2 )
    print(f'Como Δ = 0, então o único resultado real dessa equação é {x3}!')
    print()

    



