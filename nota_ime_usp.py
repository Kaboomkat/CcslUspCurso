# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:47:48 2024

@author: rodri
"""

nota = float(input('Dê entrada da sua nota no sistema: '))
if nota >= 3.0 and nota <= 5.0:
    nota = True
    print('Parabéns! Você passou')
else:
    nota = False
    print('Você falhou.')