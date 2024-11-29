# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:37:41 2024

@author: rodri
"""

import math
from sys import exit

a = float(input('Qual o valor da constante a? '))
if a == 0:
    exit('Equações de segundo grau não podem ter "a" = 0')
b = float(input('Qual o valor da constante b? '))
c = float(input('Qual o valor da constante c? '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
    
elif delta == 0:
    x3 = ( - b + math.sqrt(delta)/ a * 2 )
    print(f'a raiz desta equação é {x3}')
    
else: 
    x1 = ( - b - math.sqrt(delta))/ (a * 2) 
    x2 = ( - b + math.sqrt(delta))/ (a * 2) 
    print(f'as raízes da equação são {x1} e {x2}')
    