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
        print(
            f'ERRO! Falha na execução do comando.\nCodigo:{error.returncode}\n')

    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}')

    else:
        if msg:
            print(f'{name} Instalado com sucesso!\n')

        return 1


def createRegKey(keyDir: str, keyName: str, keyType: int, keyValue):
    """
    Cria ou altera uma chave de registro do Windows com os valores
    especificados.

    Args:
        keyDir (str): O caminho da chave de registro.
        keyName (str): O nome da chave que deve ser criada ou alterada.
        keyType (int): O tipo de valor da chave.
                       0: REG_DWORD
                       1: REG_SZ
                       2: REG_BINARY
                       3: REG_QWORD
                       4: REG_MULTI_SZ
                       5: REG_EXPAND_SZ
        keyValue (str): O valor da chave que deve ser definido.

    Returns:
        None

    """
    validKeyTypes = ['REG_DWORD', 'REG_SZ', 'REG_BINARY',
                     'REG_QWORD', 'REG_MULTI_SZ', 'REG_EXPAND_SZ']

    if keyType < 0 or keyType >= len(validKeyTypes):
        print(f'ERRO: tipo de chave inválido ({keyType})')
        return

    command = ['reg', 'add', f'"{str(keyDir)}"', '/v', str(keyName),
               '/t', str(validKeyTypes[keyType]), '/d', str(keyValue), '/f']

    try:
        createKey = run(command)
    except Exception as error:
        print(f'ERRO! {error.__class__}')
    else:
        if createKey.returncode != 0:
            print(
                f'Falha ao alterar o registro:\n Cod. {createKey.returncode}\nChave: {keyDir}, {keyName}')


def titulo(msg, tam=60):
    tamanho = len(msg) + tam
    return ('=' * tamanho + f'\n{msg:^{tamanho}}\n' + '=' * tamanho)


def validate_Version():
    # System Requirements Compatible with Program
    SYSTEM_REQUERIMENTS = ['10.0.16299']
    SYSTEM_NAME = system()
    SYSTEM_BUILD = version()
    SYSTEM_ARCHTECTURE = architecture()[0]

    print('Verificando compatibidade...\n')
    print(f'Informações do Sistema Operacional: \n \
          {SYSTEM_NAME} {SYSTEM_BUILD} {SYSTEM_ARCHTECTURE}')

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
