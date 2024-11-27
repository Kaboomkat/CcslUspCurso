temperatura = int(input('Qual a temperatura da água? '))

if temperatura >= 100:
    aguaFerve = True
    
else: 
    aguaFerve = False
    
if aguaFerve == True:
    print('A água está fervendo.')
    
else: 
    print('A água não está fervendo.')