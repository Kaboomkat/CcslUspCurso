# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:31:23 2024

@author: rodri
"""
import math

x1 = float(input('Informe a coordenada x do ponto 1: ')) 
y1 = float(input('Informe a coordenada y do ponto 1:'))
x2 = float(input('Informe a coordenada x do ponto 2: '))
y2 = float(input('Informe a coordenada y do ponto 2: '))

dist = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

distfinal = math.sqrt(dist)

if distfinal >= 10:
    print('longe')
else:
    print('perto')
