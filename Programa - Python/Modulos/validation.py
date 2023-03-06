import platform


def compatibidade(ignorar=False):
    if ignorar == True:
        print('Verificação ignorada')
        return True

    infos = [platform.system(), platform.version(), platform.architecture()[0]]
    requisitos = ['10.0.22621']

    print('Verificando compatibidade...\n')
    for c in infos:
        print(c, end=' ')
    print('\n')

    if infos[0] != 'Windows':
        print('Sistema Operacional não Suportado')
        return False

    if infos[1] not in requisitos:
        print('Versão do Windows não Suportada')
        return False

    if infos[2] != '64bit':
        print('Arquitetura não Suportada')
        return False

    return True


def install(program, name='Programa'):
    x = program
    print(f'Instalando {name}...')
    if x == 0:
        print(f'{name} Instalado com sucesso!\n')
    else:
        print(f'Erro ao instalar.\n Codigo: {x}\n')
