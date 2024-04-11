frase_entrada = str(input('Digite uma palavra ou frase: ')).strip().upper()
# strip = remove os espaços, antes e depois.
# upper = deixa tudo em MAIÚSCULO.

divisao_palavras = frase_entrada.split()
# split = separa os caracteres

remover_espacos_junta = ''.join(divisao_palavras)
# join = juntar as palavras

frase_invertida = ''

for i in range(len(remover_espacos_junta)-1, -1, -1):
    frase_invertida += remover_espacos_junta[i]
  
print(remover_espacos_junta, frase_invertida)

if frase_invertida == remover_espacos_junta:
    print(f'É um palíndromo.')
else:
    print('Não é im palíndromo.')