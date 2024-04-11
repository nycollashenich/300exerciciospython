dicionario = {'Alto Nível': 'Python',
       'Médio Nível': 'C',
       'Baixo Nível': 'Assembly'}

for c in dicionario.values():
    if not c == 'Python':
        print('Python não costa na lista.')
    else:
        print('Python consta na lista.')
        break