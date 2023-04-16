from platform import version, system, architecture
from subprocess import *


def program_install(name: str, path: str, arguments: list[str], msg=False, msi=False):
    """
    Installs a program from an executable or msi file.

    Args:
        name: The name of the program to be installed.
        path: The path to the file of the program.
        arguments: A list of optional arguments to execute during installation.
        msg: If True, displays progress messages.
        msi: If True, runs the file as a Microsoft Installer package.

    Returns:
        int: Returns 1 if the installation was successful. Otherwise, returns None.
    >>> program_install('Program Name', 'path\\program.msi', ['/qn'], msg=True, msi=True)
    """
    command = [path, *arguments]
    if msi:
        command.insert(0, 'msiexec.exe')
        command.insert(1, '/i')

    if msg:
        print(f'Instalando {name}...')

    try:
        run(command, check=True)

    except FileNotFoundError:
        print(f'ERRO! Arquivo não encontrado\n')

    except CalledProcessError as error:
        print(f'ERRO! Falha na execução do comando.\n \
        Codigo: {error.returncode}\n')

    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}')

    else:
        if msg:
            print(f'{name} Instalado com sucesso!\n')

        return 1


def create_RegKey(keyDir: str, keyName: str, keyType: str, keyValue):
    command = ['reg', 'add', keyDir, '/v',
               keyName, '/t', keyType, '/d', keyValue, '/f']

    try:
        run(command, check=True, stdout=DEVNULL, stderr=DEVNULL)

    except CalledProcessError as error:
        print('ERRO! Falha ao alterar o registro.\n')
        print(f'Codigo:{error.returncode}\nChave: {keyName} Caminho: {keyDir} \n')

    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}')

    else:
        return 1


def extractZip(path: str, outputPath: str):
    """
    Extracts a compressed file to the specified directory.

    Args:
        path: Path to the compressed file to be extracted.
        outputPath: Destination path where the contents of the file will be extracted.

    Returns:
        int: 1 if the operation was successful.
    """
    command = ['powershell', 'Expand-Archive', '-Path',
               path, '-DestinationPath', outputPath, '-Force']

    try:
        run(command)

    except FileNotFoundError:
        print(f'ERRO! Arquivo zip não encontrado\n')

    except CalledProcessError as error:
        print(f'ERRO! Falha na execução do comando.\n \
        Codigo: {error.returncode}\n')
    else:
        return 1


def titulo(msg, tam=60):
    tamanho = len(msg) + tam
    return ('=' * tamanho + f'\n{msg:^{tamanho}}\n' + '=' * tamanho)


def validate_Version():
    SYSTEM_REQUERIMENTS = ['10.0.16299']
    SYSTEM_NAME = system()
    SYSTEM_BUILD = version()
    SYSTEM_ARCHTECTURE = architecture()[0]

    print('Verificando compatibidade...\nInformações do Sistema Operacional:')
    print(f'{SYSTEM_NAME} {SYSTEM_BUILD} {SYSTEM_ARCHTECTURE}\n')

    if SYSTEM_NAME not in 'Windows':
        print('Sistema Operacional não Suportado')
        return False

    elif SYSTEM_ARCHTECTURE not in '64bit':
        print('Arquitetura não Suportada')
        return False

    elif SYSTEM_BUILD not in SYSTEM_REQUERIMENTS:
        print('Versão do Windows não Suportada')

        install_choice = str(
            input('Deseja continuar a instalação de forma limitada? [S/N]')[0].lower())
        if install_choice in 's':
            return None
        else:
            return False

    else:
        if SYSTEM_BUILD == SYSTEM_REQUERIMENTS[0]:
            return '1709'


def officeSelection():
    print('Selecione a versão do Office:')
    print('[0] Nenhuma\n[1] Office 2013\n[2] Office 2016')

    while True:
        try:
            resposta = int(input('>'))
        except ValueError:
            print('ERRO! Digite um número')
        else:
            if resposta in range(3):
                if resposta == 0:
                    return None
                if resposta == 1:
                    return '2013'
                if resposta == 2:
                    return '2016'
            else:
                print('Opção Invalida.')


def activateWindows():
    print('Ativar o Windows? [S/N]')

    while True:
        try:
            escolha = str(input('>'))[0].lower()
        except IndexError:
            print('Opção Invalida')
        except Exception as erro:
            print(f'ERRO! {erro}')
        else:
            if escolha not in 'sn':
                print('Opção Invalida')
            elif escolha == 's':
                return True
            elif escolha == 'n':
                return False
