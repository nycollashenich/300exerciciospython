def dados(*args): # usado quando não se tem um parâmetro, para testes.
    print(f'Os parâmetros são: {args}')
ex = dados('nome = Nycollas', 'idade = 18', 'peso = 60')

# parâmentro temporario.

print(dados())
