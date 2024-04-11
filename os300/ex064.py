import medicos
from time import sleep

menu = str(input('Você deseja agendar uma consulta [S/N]: ')).upper()

if menu == 'S':
    nome_paciente = str(input('Informe seu nome completo: '))
    print('-'*20)
    print(f'{nome_paciente}, com qual médico você deseja consultar: ')
    print('1- Dr.Sebastião\n2- Dr.Gorila')
    print('-'*20)
    
    medico = int(input('Com qual médico deseja agendar a consulta? '))
    sleep(1)
    if medico == 1:
        print(f'O seu agendamento está marcado com o Dr.{medicos.medicos[0]}!')
    if medico == 2:
        print(f'O seu agendamento está marcado com o Dr.{medicos.medicos[1]}!')
else:
    print('Agendamento cancelado.')