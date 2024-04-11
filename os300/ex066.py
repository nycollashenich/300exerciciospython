num = (33, 1900, 2024)
dados = {'Nome': 'Uva', 'Profissão': 'Médico', 'Idade': 40}

def identificação(*args, **kwargs):
    print(args)
    print(kwargs)
identificação(*num, **dados)