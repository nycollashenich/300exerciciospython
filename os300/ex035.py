num = int(input('Digite um número qualquer: '))


# saber se é primo 
divisao = 0 

for i in range(1, num + 1):
    if num % 2 == 0:
        divisao += 1
if divisao == 2:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo.')