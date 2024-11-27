segundos_str = input('Por favor, entre com o número de segundos que deseja converter: ')

total_segs = int(segundos_str)

dia = total_segs // 86400
segs_restante_hora = total_segs % 86400
horas = segs_restante_hora // 3600
segs_restantes_minuto = segs_restante_hora % 3600
minutos = segs_restantes_minuto // 60
segs_restantes_final = segs_restantes_minuto % 60

print(f'{dia} dias, {horas} horas, {minutos} minutos e {segs_restantes_final} segundos.')
