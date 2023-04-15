from subprocess import run
from functions import *

def install_DotNet35(version):
    if not version:
        return print('Sistema incompativel, instalação ignorada!\n')

    print('Instalando Net Framework 3.5...')
    command = ['DISM', '/Online', '/Enable-Feature', '/FeatureName:NetFx3', '/All',
               '/LimitAccess', f'/Source:1_Complementos\\.NetFramework_3.5\\{version}', '/NoRestart']

    try:
        install = run(command)

        if install.returncode != 0:
            print('Erro ao Instalar Net Framework 3.5')
            print(install.returncode)
        else:
            print('Net Framework 3.5 Instalado com Sucesso!\n')
    except Exception as error:
        print(error.__class__)
        

def install_CRuntime():
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


def install_dotNet7():
    program_install('.Net 7', '1_Complementos\\.Net_7.0.4_Runtime.exe', ['/s'], msg=True)

def install_DirectX():
    program_install('Direct X', '1_Complementos\\DirectX\\DXSETUP.exe', ['/silent'], msg=True)