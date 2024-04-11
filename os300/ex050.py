base1 = {
    'Primeira pergunta':
         {'pergunta': 'Quanto é 10 dividido por 2?', 
          'alternativas': {'a': '0', 'b': '5', 'c': '0', 'd': '0'},
          'resposta correta': 'b'}
          } # aqui são armazenadas a pergunta junto das alternativas e da resposta.

# usando o for, mostramos o dicionario completo.
# damos 'valores' as keys e valeus, mostramos os items.
for pkeys, pvalues in base1.items():
    print(f'{pkeys}\n{pvalues['pergunta']}')

print('='*20)

for rkeys, rvalues in pvalues['alternativas'].items():
    print(f'[{rkeys}]: {rvalues}')

print('='*20)

# coletamos a resposta, logo em seguida, vemos se ele acertou, ou não.
resposta = str(input('Alternativas:\n[a] [b] [c] [d]\n'))

if resposta == pvalues['resposta correta']:
    print(f'Parabéns, você acertou! a metade de 10 é 2')
else:
    print('Resposta errada!')





base02 = {'Segunda pergunta':
         {'perg': 'Qual é a metade de dois, mais dois?',
           'alter': {'A': '0', 'B': '0', 'C': '3', 'D': '0'},
            'resposta certa': 'C'}
            }
        
print('='*20)

for pekeys, pevalues in base02.items():
    print(f'{pekeys}\n{pevalues['perg']}')
for rekeys, revalues in pevalues['alter'].items():
    print(f'[{rekeys}]: {revalues}')

print('='*20)

resp = str(input('Digite sua resposta:\n[A] [B] [C] [D]\n')).upper()

if resp == pevalues['resposta certa']:
    print('Resposta correta, parabéns! a metade de dois, mais dois é 3.')
else:
    print('Resposta errada.')
