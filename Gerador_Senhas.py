import random
maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
              'W', 'X', 'Y', 'Z']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z']
simbolos = ['!', '@', '#', '$', '&', '*', '<', '>', '?', '+']

senhas = [random.choice(maiusculas), random.randint(0, 9),      # Quantidade de caracteres
          random.randint(0, 9), random.choice(minusculas),
          random.choice(minusculas), random.choice(simbolos),
          random.choice(simbolos), random.randint(0, 9),
          random.choice(simbolos)]

random.shuffle(senhas)                                              # Embaralha

print('SENHA:')

for i in senhas:                                                    # Lista
    print(i, end=' ')






