from subprocess import run


def initialize(folder: int, name: str, arguments: list[str], subFolder: str=None,msi=False):
    """
    Executa um programa a partir do caminho e do nome especificado.

    Args:
        folder (int): O índice da pasta onde o programa está localizado.
        name (str): O nome do arquivo .exe que será executado.
        arguments (List[str]): Uma lista de argumentos que serão passados ​​para o programa.
        msi (bool): Se True, o arquivo é um MSI e deve ser executado com msiexec.exe. Defa
        ult é False.

    Returns:
        None

    """
    dir = ['0_Drivers','1_Complementos','2_Programas', '3_Configuracoes', '4_Ativacao', '5_Finalizacao']

    if subFolder != None:
        programPath = f'{dir[folder]}\\{subFolder}\\{name}.exe'
    else:
        programPath = f'{dir[folder]}\\{name}.exe'

    
    command = [programPath, *arguments]
    
    print(f'Instalando {name}...')
    try:
        install = run(command)
    except FileNotFoundError:
        print('ERRO! Arquivo não encontrado!')
    except Exception as error:
        print(error.__class__)
    else:
        if install.returncode != 0:
            print(f'Erro ao instalar {name}')
            print(install.returncode)
        else:
            print(f'{name} instalado com sucesso!\n')

def installChrome():
    print('Instalando Google Chrome...')
    programPath = '2_Programas\\GoogleChrome.msi'
    arguments = ['msiexec', '/i', programPath, '/qn']
    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar Google Chrome')
        print(command.returncode)
    else:
        print('Google Chrome instalado com sucesso!\n')


def installFirefox():
    print('Instalando Firefox...')
    programPath = '2_Programas\\Firefox.msi'
    arguments = ['msiexec', '/i', programPath, '/qn']
    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar Firefox')
        print(command.returncode)
    else:
        print('Firefox instalado com sucesso!\n')


def installOffice(version):
    if version == 0:
        return

    print('Instalando Office...')
    programPath = f'2_Programas\\Office\\{version}\\setup.exe'
    arguments = [programPath]
    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar Firefox')
        print(command.returncode)
    else:
        print('Firefox instalado com sucesso!\n')

# def installAnydesk():
#     print('Instalando Anydesk...')
#     programPath = '2_Programas\\Anydesk.exe'
#     arguments = [programPath, '--install',
#                  'C:\Program Files (x86)\AnyDesk', '--silent']
#     command = run(arguments)

#     if command.returncode != 0:
#         print('Erro ao instalar Anydesk')
#         print(command.returncode)
#     else:
#         print('Anydesk instalado com sucesso!\n')


def installTeamviewer():
    print('Instalando Teamviewer...')
    run(['2_Programas\\EdgeWebview.exe', '/silent', '/install'])
    programPath = '2_Programas\\TeamViewer.exe'
    arguments = [programPath, '/S']
    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar Teamviewer')
        print(command.returncode)
    else:
        print('Teamviewer instalado com sucesso!\n')


def installAdobe():
    print('Instalando Adobe Reader...')
    programPath = '2_Programas\\Adobe Reader\\setup.exe'
    arguments = [programPath]
    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar Adobe Reader')
        print(command.returncode)
    else:
        print('Adobe Reader instalado com sucesso!\n')


def installDeluge():
    print('Instalando Deluge...')
    programPath = '2_Programas\\Deluge.exe'
    arguments = [programPath, '/S']
    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar Deluge')
        print(command.returncode)
    else:
        print('Deluge instalado com sucesso!\n')
