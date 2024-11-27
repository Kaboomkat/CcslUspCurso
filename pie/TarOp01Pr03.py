NumInt = int(input('Digite um número inteiro: '))
Dezena = NumInt%100
Resto = Dezena//10
print(f'O dígito das dezenas é {int(Resto)}')