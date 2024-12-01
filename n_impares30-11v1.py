# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:26:03 2024

@author: rodri
"""

n = int(input('Digite o valor de n: '))

n2 = 1

print('1')

while n2 < n * 2:
    n2 = n2 + 1
    if n2 % 2 != 0:
        print(n2)
        
    