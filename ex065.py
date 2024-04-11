import medicos
import cadastros_saude
from time import sleep

usuario = str(input('Digite seu número de usuário: '))
if usuario in cadastros_saude.clientes.keys():
    if usuario == '001':
        usuario = 'Caqui'
        print(f'Bem vindo(a)! {usuario}.')
    if usuario == '002':
        usuario = 'Abacaxi'
        print(f'Bem vindo(a)! {usuario}.')
else:
    print('Usuário não cadastrado, favor entrar em contado!')

# menu de atendimento:
menu = str(input('Você deseja agender uma consulta[S/N]: ')).upper()
sleep(1)
if menu == 'S':
    print('Escolha o médico que você deseja: ')
    print('1 - Dr. Sebastião\n2 - Dr.Gorila')
    medico = int(input('Informe: '))
    sleep(2)
    if medico == 1:
        print(f'{usuario}, sua consulta está agendada com o Dr.{medicos.medicos[0]}.')
    if medico == 2:
        print(f'{usuario}, sua consulta está agendada com o Dr. {medicos.medicos[1]}.')
    else:
        print('Agradecemos seu contado, até uma próxima.') 

else:
    print('Agendamento cancelado.')
