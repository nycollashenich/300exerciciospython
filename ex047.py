# AQUI AINDA SÃO LISTAS
itens = ['Caderno', 'Lápis', 'Borracha', 'Apontador']  # criação das listas
valores = ['R$25,00', 'R$0,50', 'R$0,25', 'R$2,00']  # criação das listas

# AQUI JÁ é UM DICIONARIO, pegamos a lista e tornamos um dicionario
dicionario = dict(chaves_keys = itens, valores_values = valores)
# usando dict(), é como se fosse um dicionario, com chave e valores, soq de forma mais simples.

print(dicionario)
print(type(dicionario))

# Aqui é um dicionario normal, com chaves e valores
teste = {'Nome': 'Nycollas', 'Idade': 18, 'Altura': 1.80, 'Peso': 75}
print(teste.keys()) # mostra as chaves, nome, idade e etc...
print(teste.values()) # mostra os valores, Nycollas, 18 e etc...