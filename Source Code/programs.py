from subprocess import run


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
