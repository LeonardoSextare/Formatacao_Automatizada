from subprocess import run
from functions import *


def installChrome():
    initializeProgram(2, 'Google Chrome', ['/qn'], msi=True, subFolder='Google Chrome')
    run(['2_Programas\\Google Chrome\\SetDefaultBrowser.exe', 'chrome'])


def installFirefox():
    initializeProgram(2, 'Firefox', ['/qn'], msi=True)


def installAnydesk():
    initializeProgram(2, 'Anydesk', ['--install',
                                     'C:\Program Files (x86)\AnyDesk', '--silent', '--create-desktop-icon'])


def installTeamviewer():
    run(['2_Programas\\EdgeWebview.exe', '/silent', '/install'])
    initializeProgram(2, 'TeamViewer', ['/S'])


def installAdobe():
    initializeProgram(2, 'Adobe Reader', [], subFolder='Adobe Reader')
    run(['2_Programas\\Adobe Reader\\SetUserFTA.exe', '.pdf','AcroExch.Document.DC'])


def installOffice(version):
    if version == 0:
        return
    
    print('Instalando Office...')
    programPath = f'2_Programas\\Office\\{version}\\setup.exe'
    arguments = [programPath]
    command = run(arguments)

    if command.returncode != 0:
        print(f'Erro ao instalar Office {version}')
        print(command.returncode)
    else:
        print(f'Office {version} instalado com sucesso!\n')
