print('CALCULADORA DE JUROS\n---------------------------------')

c = float(input('Valor de entrada: R$'))
i = float(input('Taxa de Juros: (%)'))
porcen = i / 100
t = int(input('Tempo em meses: '))

perg = input('Simples ou Composto? (S/C) ').upper()
print('-----------------------------------------')
if perg == 'S':
    print('JUROS SIMPLES')
    print(f'Valor investido: \033[33mR${c}\033[0m')
    juros = c * (porcen * t)
    print(f'Juros simples acumulado: \033[32mR${juros:.2f}\033[0m')
    print(f'Montante: \033[31mR${c + juros:.2f}\033[0m')
elif perg == 'C':
    print('JUROS COMPOSTOS')
    print(f'Valor investido: \033[33mR${c}\033[0m')
    print(f'Montante: \033[31mR${c*((1+porcen)**t):.2f}\033[0m')
