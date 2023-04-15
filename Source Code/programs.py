from subprocess import run
from functions import *


def installChrome():
    initializeProgram(2, 'Google Chrome', [
                      '/qn'], msi=True, subFolder='Google Chrome')
    run(['2_Programas\\Google Chrome\\SetDefaultBrowser.exe', 'chrome'])


def installFirefox():
    initializeProgram(2, 'Firefox', ['/qn'], msi=True)


def install_Anydesk():
    start_executable('Anydesk', '2_Programas\\AnyDesk.exe',
                     ['--install', 'C:\\Program Files (x86)\\AnyDesk', '--silent', '--create-desktop-icon'], msg=True)


def installTeamviewer():
    run(['2_Programas\\EdgeWebview.exe', '/silent', '/install'])
    initializeProgram(2, 'TeamViewer', ['/S'])


def install_Adobe():
    start_executable(
        'Adobe Reader', '2_Programas\\Adobe Reader\\Adobe Reader.exe', [], msg=True)

    print('Definindo como leitor de PDF padrão...')
    set_Default = start_executable('Leitor', '2_Programas\\Adobe Reader\\SetUserFTA.exe',
                                   ['.pdf', 'AcroExch.Document.DC'])
    if set_Default == 0:
        print('Adobe Reader definido como leitor padrão!')


def install_Winrar():
    start_executable('Winrar', '2_Programas\\Winrar.exe', ['/S'], msg=True)


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
