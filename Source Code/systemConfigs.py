from subprocess import run
from functions import *
from shutil import *


def configWindows1709():
    disable_WindowsUpdate()
    disable_autoRepair()
    change_wallpaper()

    # Configures system by windows regkeys
    regImport(1709)
    ...


def configWindows22H2():
    disable_WindowsUpdate()
    disable_autoRepair()
    ...


def disable_WindowsUpdate():
    print('Desabilitando Windows Update...')

    try:
        extractZip('3_Configuracoes\\Win_Update_Blocker\\Win_Update_Blocker.zip',
                   '3_Configuracoes\\Win_Update_Blocker\\.')
        program_install('Desativar Update',
                        '3_Configuracoes\\Win_Update_Blocker\\Win_Update_Blocker.exe', ['/D', '/P'])
    except:
        print('Ocorreu um erro ao desabilitar o Windows Update!\n')
    else:
        print('Windows Update desabilitado!\n')


def disable_autoRepair():
    command = ['bcdedit', '/set', '{default}', 'recoveryenabled', 'no']

    try:
        run(command, check=True, stdout=DEVNULL)
    except CalledProcessError as error:
        print(f'ERRO! Falha ao alterar o registro.\n \
        Codigo:{error.returncode}\n')

    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}')
    else:
        print(f'Reparo Automatico desabilitado com sucesso!\n')


def regImport(version):

    try:
        run(['reg', 'import',
            f'3_Configuracoes\\Configs_{version}.reg'], stdout=DEVNULL)
    except FileNotFoundError:
        print('ERRO! Arquivo não encontrado\n')
    except CalledProcessError as error:
        print(f'ERRO! Falha na execução do comando.\n \
              Codigo: {error.__class__}')
    except Exception as error:
        print(f'ERRO desconhecido! Tipo: {error.__class__}')
    else:
        print('Registro importado com sucesso!\n')


def change_wallpaper():
    try:
        copy('3_Configuracoes\\Wallpaper.jpg',
             'C:\\Windows\\Web\\Wallpaper\\Windows')
        
        if create_RegKey('HKEY_CURRENT_USER\Control Panel\Desktop',
                         'Wallpaper', 'REG_SZ', 'C:\\Windows\\Web\\Wallpaper\\Windows\\Wallpaper.jpg') is True:
            
            run(['RUNDLL32.EXE', 'user32.dll,UpdatePerUserSystemParameters'])
            print('Papel de Parede trocado com sucesso!\n')
        else:
            print('Falha ao trocar o papel de parede!')
    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}')
    
