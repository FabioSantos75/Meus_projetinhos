print("Minha Urna Eletrônica")
print('-'*30)
Joaozinho = Maria = Fabio = Branco = 0
Esther = Nicole = Julio = 0
nomes = []

while True:
    while True:
        eleitor = str(input('Seu nome: '))
        nomes.append(eleitor)
        if eleitor != 0:
            break

    while True:
        print('Candidatos para prefeito:')
        print('15 - Joãozinho / 17 - Maria / 10 - Fabio / 0 - Branco')
        prefeito = int(input('Seu voto: '))

        if prefeito == 15:
            print('Candidato: Joãozinho')
        elif prefeito == 17:
            print('Candidata: Maria')
        elif prefeito == 10:
            print('Candidato: Fabio')
        elif prefeito == 0:
            print('Voto em Branco')
        else:
            print('Candidato inexistente')
            continue

        confir = input('Confirma? [s/n] ').lower().strip()
        if confir == 's':
            if prefeito == 15:
                Joaozinho += 1
            elif prefeito == 17:
                Maria += 1
            elif prefeito == 10:
                Fabio += 1
            break
        elif confir == 'n':
            continue
    print()
# Loop para votação do vereador

    while True:
        print('Candidatos para Vereador:')
        print('100 - Esther / 200 - Nicole / 300 - Julio / 0 - Branco')
        vereador = int(input('Seu voto: '))

        if vereador == 100:
            print('Candidata: Esther')
        elif vereador == 200:
            print('Candidata: Nicole')
        elif vereador == 300:
            print('Candidato: Julio')
        elif vereador == 0:
            print('Voto em Branco')
        else:
            print('Candidato inexistente')
            continue

        confir = input('Confirma? [s/n] ').lower().strip()
        if confir == 's':
            if vereador == 100:
                Esther += 1
            elif vereador == 200:
                Nicole += 1
            elif vereador == 300:
                Julio += 1
            break
        elif confir == 'n':
            continue
    print()
    novo = str(input('Novo voto? [s] ')).lower().strip()
    if novo == "s":
        continue
    elif novo == "n":
        break
print()
# Exibição dos resultados
print("Eleitores: ")
print(nomes)
print(f'\nResultado para Prefeito:\nJoãozinho: {Joaozinho}\nMaria: {Maria}\nFabio: {Fabio}')
print('-'*30)
print(f'Resultado para Vereador:\nEsther: {Esther}\nNicole: {Nicole}\nJulio: {Julio}')























