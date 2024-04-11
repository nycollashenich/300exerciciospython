primeiro_termo = int(input('Insira o primeiro valor: '))
razao = int(input('Insira a razão: '))

pa = primeiro_termo + (20 - 1) * razao

for i in range(primeiro_termo, pa + razao, razao):
    print(i)