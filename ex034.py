soma = 0
contador = 0

for c in range(1, 100+1):    
    if c % 3 == 0:
        print(c)
        soma += c
        contador += 1
print(f'Soma: {soma}, Contador: {contador}')
