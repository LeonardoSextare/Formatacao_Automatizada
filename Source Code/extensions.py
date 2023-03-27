from subprocess import run


def installDotNet35(version):
    if version == '0':
        return print('Sistema incompativel, instalação ignorada!')
    
    print('Instalando Net Framework 3.5...')
    arguments = ['DISM', '/Online', '/Enable-Feature', '/FeatureName:NetFx3', '/All',
               '/LimitAccess', f'/Source:1_Complementos\\.NetFramework_3.5\\{version}', '/NoRestart']

    command = run(arguments)
    if command.returncode != 0:
        print('Erro ao Instalar Net Framework 3.5')
        print(command.returncode)
    else:
        print('Net Framework 3.5 Instalado com Sucesso!\n')


def installDotNet7():
    print('Instalando .Net 7')
    programPath = '1_Complementos\\.Net_7.0.4_Runtime.exe'
    arguments = [programPath, '/s']

    command = run(arguments)

    if command.returncode != 0:
        print('Erro ao instalar .Net 7')
        print(command.returncode)
    else:
        print('.Net 7 instalado com sucesso!\n')


def installJava():
    print('Instalando Java 8...')
    programPath = '1_Complementos\\Java_Runtime.msi'
    arguments = ['msiexec', '/i', programPath, '/qn','AUTO_UPDATE=Disable', 'NOSTARTMENU=Enable']

    command = run(arguments)
    if command.returncode != 0:
        print('Erro ao instalar Java 8')
        print(command.returncode)
    else:
        print('Java 8 Instalado com sucesso!\n')


def installCRuntime():
    print('Instalando Visual C++ Runtimes(2005-2022)')
    programPath = '1_Complementos\\VisualC++_Runtime\\'
    errorList = []

    packages = [['vcredist2005_x86.exe', 'vcredist2005_x64.exe'],
                ['vcredist2008_x86.exe', 'vcredist2008_x64.exe'],
                ['vcredist2010_x86.exe', 'vcredist2010_x64.exe', 'vcredist2012_x86.exe', 'vcredist2012_x64.exe', 'vcredist2013_x64', 'vcredist2013_x86', 'vcredist2015_2017_2019_2022_x86.exe', 'vcredist2015_2017_2019_2022_x64.exe']]
    
    for c in packages:
        for x in c:
            if x in packages[0]:
                parameter = ['/q']
            elif x in packages[1]:
                parameter = ['/qb']
            elif x in packages[2]:
                parameter = ['/passive', '/norestart']
            arguments = [programPath + x]
            arguments.extend(parameter)
            
            command = run(arguments)

            if command.returncode != 0:
                errorList.append(x)

    if len(errorList) == 0:
        print('Visual C++ Runtimes Instalado com sucesso!\n')
    else:
        print('Erro ao instalar os pacotes: ')
        for c in (errorList):
            print(c)

def installDirectX():
    print('Instalando DirectX...')
    programPath = '1_Complementos\\DirectX\\DXSETUP.exe'
    arguments = [programPath, '/silent']
    
    command = run(arguments)
    
    if command.returncode != 0:
        print('Erro ao instalar DirectX')
        print(command.returncode)
    else:
        print('DirectX instalado com sucesso!\n')