from datetime import datetime
from dateutil.relativedelta import relativedelta  # Para manipular meses facilmente

# Entrada de dados
valortot = float(input("Digite o valor total: "))
parcela = int(input("Quantidade de parcelas: "))
valparc = valortot / parcela

primeiropag = input("Data do primeiro pagamento (DD/MM/AAAA): ")
data_inicial = datetime.strptime(primeiropag, "%d/%m/%Y").date()

# Exibição geral
print(f"\nValor total: R${valortot:.2f}")
print(f"Quantidade de parcelas: {parcela}")
print(f"Valor de cada parcela: R${valparc:.2f}")
print(f"\nDetalhes das parcelas:")

# Loop para exibir detalhes de cada parcela
for i in range(parcela):
    # Incrementa os meses, mas mantém o mesmo dia do mês
    data_parcela = data_inicial + relativedelta(months=i)
    print(f"Parcela {i + 1}: R${valparc:.2f} - Vencimento: {data_parcela.strftime('%d/%m/%Y')}")






