# trabalhando com funções, dando novos 'parametros'.

def dados(nome, peso = '75', idade = '18'):
    print(f'{nome}\n{peso}\n{idade}')

nome = str(input('Digite seu nome: '))
exx = dados(nome)

peso = input('Digite seu peso: ')
exxx = dados(nome, peso)

idade = input('Digite sua idade: ')
exxxx = dados(nome, peso, idade)


def boas_vindas(nome, nacionalidade = 'Alemão'):
    print(f'{nome} é {nacionalidade}')

nome = input('Seu nome: ')
ex = boas_vindas(nome)

nacionalidade = input('Sua nacionalidade: ')
ex2 = boas_vindas(nome, nacionalidade)