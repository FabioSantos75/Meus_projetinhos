from datetime import datetime, timedelta

print('CONOGRAMA DE ESTUDOS')
inicio = input('Data de início: D/M/A ')
data_inicial = datetime.strptime(inicio, "%d/%m/%Y").date()

conteudo = ("Leitura, compreensão e interpretação de textos",
    "Estruturação do texto e dos parágrafos",
    "Articulação do texto: pronomes e expressões referenciais, nexos, operadores sequenciais",
    "Significação contextual de palavras e expressões",
    "Equivalência e transformação de estruturas",
    "Sintaxe: processos de coordenação e subordinação",
    "Emprego de tempos e modos verbais",
    "Pontuação",
    "Estrutura e formação de palavras",
    "Funções das classes de palavras",
    "Flexão nominal e verbal",
    "Pronomes: emprego, formas de tratamento e colocação",
    "Concordância nominal e verbal",
    "Regência nominal e verbal",
    "Ortografia oficial",
    "Acentuação gráfica")

for index, conteudo in enumerate(conteudo, start=1):
    nova = data_inicial + timedelta(days = index-1)
    print(nova.strftime("\033[31m%d/%m/%Y\033[0m"))
    print(f'\033[1mDia {index:02}:\033[0m \033[37m{conteudo}\033[0m')
    print('---------------------------')


"""
Um cronograma simples, inserindo o conteúdo para estudo e a data de início
ele é capaz de contar a progressão de dias e  data para cada assunto a ser estudado,
pode ser muito útil para quem quer fazer um cronograma de estudos de um jeito rápido.

"""
