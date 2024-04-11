def adicao(*args):
    num = 0 
    for somas in args:
        num += somas
    print(f'O resultado da soma é {num}')

soma = adicao(20, 30, 40, 50)
