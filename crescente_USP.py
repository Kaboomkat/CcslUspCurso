# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:40:10 2024

@author: rodri
"""

n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))
n3 = int(input('Entre com o terceiro número: '))

if n1 < n2 < n3:
    print('crescente')
else:
    print('não está em ordem crescente')