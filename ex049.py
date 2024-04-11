nome_aluno = str(input('informe o nome do aluno: '))

nota1 = float(input('Insira a 1° nota: '))
nota2 = float(input('Insira a 2° nota: '))
nota3 = float(input('Insira a 3° nota: '))

media = (nota1 + nota2 + nota3) / 3

nome_notas = {'Nome: ': nome_aluno, 
              '1° Nota: ': nota1, 
              '2° Nota: ': nota2, 
              '3° Nota: ': nota3}

nome_notas['Média'] = media # prestar a atenção, pois aq criei uma nova chave e valor

print(nome_notas)