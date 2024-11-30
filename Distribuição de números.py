import random

# distribuição de números para quatro jogadores, mas sem repetir.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

conjunto1 = random.sample(lista, 4)
conjunto2 = random.sample([x for x in lista if x not in conjunto1], 4)
conjunto3 = random.sample([x for x in lista if x not in conjunto1 + conjunto2],4)
conjunto4 = random.sample([x for x in lista if x not in conjunto1 + conjunto2 + conjunto3],4)

prim1, seg1, ter1, qua1 = conjunto1

prim2, seg2, ter2, qua2 = conjunto2

prim3, seg3, ter3, qua3 = conjunto3

prim4, seg4, ter4, qua4 = conjunto4

print('\033[36mJOGADOR 01:\033[0m')
print(prim1, " / ",seg1, " / ", ter1, " / ", qua1)
print(" ")
print('\033[34mJOGADOR 02:\033[0m')
print(prim2, " / ",seg2, " / ", ter2, " / ", qua2)
print(" ")
print('\033[31mJOGADOR 03:\033[0m')
print(prim3, " / ", seg3, " / ", ter3, " / ", qua3)
print(" ")
print('\033[35mJOGADOR 04:\033[0m')
print(prim4, " / ", seg4, " / ", ter4, " / ", qua4)
