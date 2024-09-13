import time
from datetime import datetime

def obter_input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, insira um número válido.")

def obter_input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                raise ValueError("O valor deve ser um número positivo.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, insira um número inteiro positivo.")


hora_atual = datetime.now()
print('CONTAGEM DE GANHO POR TEMPO:')
print('Digite: "0" se você não sabe o valor que ganho por hora.')


hora = obter_input_float('Ganho por hora: ')


if hora == 0:
    salario = obter_input_float('Salário: R$')
    horas_trabalhadas = obter_input_int('Horas trabalhadas no mês: ')
    hora = salario / horas_trabalhadas


minuto = hora / 60
print(f'Ganho por hora: R${hora:.2f}')
print('_'*25)
print(f'Início da contagem: {hora_atual.strftime("%H:%M")}')


minuto_acumulado = 0
while True:
    try:
        time.sleep(60)  # Aguarda 60 segundos (1 minuto)
        minuto_acumulado += minuto
        print(f'Ganho acumulado: R${minuto_acumulado:.2f}')
    except KeyboardInterrupt:
        print("\nContagem interrompida pelo usuário.")
        break





