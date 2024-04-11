nome = str(input('Digite seu nome: '))
idade = int(input('Digite a sua idade: '))
sexo = str(input('Digite seu sexo: '))
estado_civil = str(input('Digite seu estado civil: '))
nacionalidade = str(input('Digite sua nacionalidade: '))
escolaridade = str(input('Digite sua escolaridade: '))

cadastro = {'Nome': nome, 
            'Idade': idade, 
            'Sexo': sexo, 
            'Estado Civil': estado_civil, 
            'Nacionalidade': nacionalidade, 
            'Escolaridade': escolaridade}           
print(cadastro)
print(cadastro.keys())
print(cadastro.values())
print(cadastro.clear())


