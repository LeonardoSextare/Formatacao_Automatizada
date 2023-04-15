from subprocess import run
from functions import *


def installChrome():
    success = program_install('Google Chrome', '2_Programas\\Google Chrome\\Google Chrome.msi',
                              ['/qn'], msg=True, msi=True)
    if success:
        set_Default = program_install(
            'Navegador', '2_Programas\\Google Chrome\\SetDefaultBrowser.exe', ['chrome'])
        if set_Default:
            print('Google Chrome definido como navegador padrão!\n')


def installFirefox():
    program_install('Firefox', '2_Programas\\Firefox.msi',
                    ['/qn'], msg=True, msi=True)


def install_Anydesk():
    program_install('Anydesk', '2_Programas\\AnyDesk.exe',
                    ['--install', 'C:\\Program Files (x86)\\AnyDesk', '--silent', '--create-desktop-icon'], msg=True)


def install_Adobe():
    success = program_install(
        'Adobe Reader', '2_Programas\\Adobe Reader\\Adobe Reader.exe', [], msg=True)
    if success:
        set_Default = program_install('Leitor', '2_Programas\\Adobe Reader\\SetUserFTA.exe',
                                      ['.pdf', 'AcroExch.Document.DC'])
        if set_Default:
            print('Adobe Reader definido como leitor padrão!\n')


def install_Winrar():
    program_install('Winrar', '2_Programas\\Winrar.exe', ['/S'], msg=True)


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


def install_JavaRuntime():
    program_install('Java 8', '1_Complementos\\Java_Runtime.msi',
                    ['/qn', 'AUTO_UPDATE=Disable', 'NOSTARTMENU=Enable'], msg=True, msi=True)
