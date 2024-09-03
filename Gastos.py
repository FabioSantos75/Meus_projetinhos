print('\033[1mORÇAMENTO PESSOAL\033[0m')
entrada = 637.24+5
print(f'Entrada: \033[34mR${entrada}\033[0m')
dados = []
soma = de = la = va = 0

"""
de: despesas - que se repete todos os mesês
la: lazer - diversão gasto sem compromisso
va: variados - não é lazer e nem despesas
"""

def salvar_tarefas():
    try:
        with open('gastos.txt', 'w') as file:
            for k in dados:
                file.write(f'{k[0]};{k[1]};{k[2]}\n')
    except Exception as e:
        print(f'Erro ao salvar os dados: {e}')


def carregar_tarefas():
    try:
        with open('gastos.txt', 'r') as file:
            for linha in file:
                try:
                    nome, cat, valor = linha.strip().split(';')
                    valor = float(valor)
                    dados.append([nome, cat, valor])
                    global soma, de, la, va
                    soma += valor
                    if cat == 'de':
                        de += valor
                    elif cat == 'la':
                        la += valor
                    elif cat == 'va':
                        va += valor
                except ValueError:
                    print(f'Erro ao converter os dados na linha: {linha.strip()}')
    except FileNotFoundError:
        print('Nenhum arquivo encontrado. Um novo arquivo será criado ao adicionar uma tarefa.')
    except Exception as e:
        print(f'Erro ao carregar os dados: {e}')


def menu():
    print('\033[1mMENU PRINCIPAL\033[0m')
    lista = ['1 - Novo gasto', '2 - Tabela', '3 - Relatório', '4 - Excluir item', '5 - Sair']
    for i in lista:
        print(i)


print('-' * 25)
carregar_tarefas()  # Carrega as tarefas ao iniciar o programa
menu()
print('-' * 25)
while True:
    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
    if opcao == 1:
        while True:
            try:
                listas = []
                nome = input('Nome: ').strip()
                if not nome:
                    raise ValueError("Nome não pode ser vazio.")
                listas.append(nome)
                cat = input('Categoria (de, la, va): ').strip().lower()
                if cat not in ['de', 'la', 'va']:
                    raise ValueError("Categoria inválida. Use 'de', 'la' ou 'va'.")
                listas.append(cat)
                valor = float(input('Valor: R$'))
                listas.append(valor)
                soma += valor
                if cat == 'de':
                    de += valor
                elif cat == 'la':
                    la += valor
                elif cat == 'va':
                    va += valor
                dados.append(listas)
                perg = input('Mais? [s/n] ').strip().upper()
                print('-' * 25)
                if perg == 'N':
                    salvar_tarefas()
                    break
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
    elif opcao == 2:
        print('-' * 25)
        print('TABELA')
        print('\033[1m\033[94mGASTO           CATEGORIA    VALOR     \033[0m')
        print('-' * 40)
        for i in dados:
            print(f'\033[94m{i[0]:<17} {i[1]:<10} {i[2]:<10.2f}\033[0m')
        print()
        if soma < entrada:
            print(f'Total: \033[34mR${soma:.2f}\033[0m\n')
        else:
            print(f'Total: \033[31mR${soma:.2f}\033[0m\n')
    elif opcao == 3:
        print('-' * 25)
        print('\033[36mRELATÓRIO\033[0m')
        if soma < entrada:
            print(f'Total Gasto: \033[34mR${soma:.2f}\033[0m')
        else:
            print(f'Total Gasto: \033[31mR${soma:.2f}\033[0m')
        print(f'\033[90m{(soma / entrada) * 100:.2f}%\033[0m')
        saldo = entrada - soma
        if saldo > 0:
            print(f'Saldo: \033[34mR${saldo:.2f}\033[0m\n')
        else:
            print(f'Saldo: \033[31mR${saldo:.2f}\033[0m\n')
            print(f'\033[31mVocê gastou R${soma - entrada} mais dinheiro do que ganhou!\033[0m\n')
        print(f'\033[34mDespesas:    R${de} | {(de / entrada) * 100:6.1f}%\033[0m')
        print(f'\033[34mVariáveis:   R${va} | {(va / entrada) * 100:6.1f}%\033[0m')
        print(f'\033[34mLazer:       R${la} | {(la / entrada) * 100:6.1f}%\033[0m\n')
        print(f'\033[90mNº de Gastos: {len(dados)}\nMédia: R${soma/len(dados):.2f}\033[0m')
        print(f'\033[90mPor semana: R${soma / 4:.2f}\nPor dia: R${soma / 30:.2f}\033[0m\n')
    elif opcao == 4:
        concluir = input('Gasto a ser excluído (Nome): ').strip()
        found = False
        for p in dados:
            if concluir in p:
                dados.remove(p)
                print(f'Gasto "{concluir}" excluído.')
                salvar_tarefas()
                found = True
                break
        if not found:
            print(f'Gasto "{concluir}" não encontrado.')
    elif opcao == 5:
        print('PROGRAMA FINALIZADO!')
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção do menu.")
