import requests

# API do NewsAPI:
api_key = '4d73512ca2ff4c9aae523d4616f5497d'

# Função para buscar notícias com base nas palavras-chave
def buscar_noticias(palavras_chave):
    # Usando uma combinação de operadores para flexibilizar a busca
    query = f'{palavras_chave}'
    url = f'https://newsapi.org/v2/everything?q={query}&sortBy=relevancy&language=pt&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        noticias = response.json()['articles']
        if not noticias:  # Se não houver notícias, tentar outra busca mais genérica
            print(f"Nenhum resultado encontrado para '{palavras_chave}'. Tentando uma busca mais genérica.")
            url = f'https://newsapi.org/v2/everything?q={palavras_chave.split()[0]}&language=pt&apiKey={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                noticias = response.json()['articles']
        return noticias
    else:
        print(f"Erro ao buscar notícias: {response.status_code}")
        return None

# Função para exibir as notícias
def exibir_noticias(noticias, top=3):
    if noticias:
        for i, noticia in enumerate(noticias[:top], start=1):
            # Formatando a data para uma leitura mais amigável
            data_publicacao = noticia['publishedAt']
            data_formatada = data_publicacao[:10]  # Pegando apenas a parte da data (YYYY-MM-DD)
            print(f"{i}. {noticia['title']}")
            print(f"Fonte: {noticia['source']['name']}")
            print(f"Data: {data_formatada}")
            print(f"Subtítulo: {noticia['description']}")
            print(f"Link: {noticia['url']}")
            print("-" * 40)
    else:
        print("Nenhuma notícia encontrada.")

# Palavras-chave personalizadas
palavras_chave = ['Arsenal']

# Buscando e exibindo notícias para cada palavra-chave
for palavra in palavras_chave:
    print(f"\nBuscando notícias sobre: {palavra}\n")
    noticias = buscar_noticias(palavra)
    exibir_noticias(noticias)
