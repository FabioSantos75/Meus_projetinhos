from time import sleep

ganho = int(input('Quanto você ganho por mês? R$'))

tempo = int(input('Quantas horas você trabalho por mês? '))

hora = ganho / tempo
minuto = hora / 60

print(f'Quanho por hora: R${hora:.2f}')
print()
print('GANHO POR MINUTO:')
for i in range(ganho):
    ganho_acumulado = minuto * i
    print(f'R${ganho_acumulado:.2f}')
    print('----------------')
    sleep(60)
    
"""
Quanto uma pessoa está ganhando a cada minuto que passa
de acordo com o salário mensal e qtd de horas.
"""
