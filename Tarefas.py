def menu():
    lista = ['1 - Nova Tarefa', '2 - Ver Tarefas', '3 - Concluir Tarefa', '4 - Fechar']
    for i in lista:
        print(i)

def salvar_tarefas():
    with open('tarefas.txt', 'w') as file:
        for tarefa in tarefas:
            file.write(f'{tarefa[0]};{tarefa[1]};{tarefa[2]}\n')

def carregar_tarefas():
    try:
        with open('tarefas.txt', 'r') as file:
            for linha in file:
                dia, hora, nome = linha.strip().split(';')
                tarefas.append([dia, hora, nome])
    except (FileNotFoundError, ValueError):
        print('Nenhuma tarefa encontrada. Um novo arquivo será criado ao adicionar uma tarefa.')


tarefas = []
carregar_tarefas()
print('-'*25)
menu()
print('-'*25)
print('TAREFAS:')
for i in tarefas:
    print(f'{i[0]} | {i[1]} -- {i[2]}')

print('-' * 25)
while True:

    try:
        opcoes = int(input('Opção: '))
    except (ValueError, TypeError, KeyboardInterrupt):
        print('Por favor, insira um número válido.')
        continue
    if opcoes == 1:
        dia = input('Dia: ')
        while True:
            lista = [dia]
            hora = input('Hora: ')
            lista.append(hora)
            nome = input('Tarefa: ')
            lista.append(nome)
            tarefas.append(lista)
            perg = input('Mais? (S/N) ').strip().upper()
            print('-' * 25)
            if perg != 'S':
                salvar_tarefas()
                break
    elif opcoes == 2:
        print('TAREFAS:')
        for i in tarefas:
            print(f'{i[0]} | {i[1]} -- {i[2]}')
        print('-' * 25)

    elif opcoes == 3:
        concluir = input('Tarefa a ser concluída (Hora ou Nome): ')
        for tarefa in tarefas:
            if concluir in tarefa:
                tarefas.remove(tarefa)
                print(f'Tarefa "{concluir}" concluída.')
                salvar_tarefas()
                break
        else:
            print('Tarefa não encontrada.')
        print('-' * 25)
    elif opcoes == 4:
        print('Programa Finalizado')
        break
    else:
        print('Número inválido.')
