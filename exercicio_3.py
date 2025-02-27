# 3) Faturamento Diário com JSON
import json

with open('dados.json', 'r') as file:
    dados_json = json.load(file)

faturamento = [dia['valor'] for dia in dados_json if dia['valor'] > 0]

menor = min(faturamento)
maior = max(faturamento)
media = sum(faturamento) / len(faturamento)
dias_acima_media = len([dia for dia in faturamento if dia > media])

print(f"3) Menor valor de faturamento: {menor:.2f}")
print(f"   Maior valor de faturamento: {maior:.2f}")
print(f"   Dias com faturamento acima da média: {dias_acima_media}")