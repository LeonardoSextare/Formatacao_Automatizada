from platform import version, system, architecture
from subprocess import *


def start_executable(name: str, exe_path: str, arguments: list[str], msg=False):
    print(name, exe_path, arguments)
    command = [exe_path, *arguments]

    if msg:
        print(f'Instalando {name}...')

    try:
        executable = run(command)
    except CalledProcessError as error:
        print(f'ERRO! Erro durante a execução do comando.\nCodigo:{error}')
    except FileNotFoundError:
        print(f'ERRO! Arquivo não encontrado')
    except Exception as error:
        print(f'ERRO desconhecido! {error.__class__}')
    else:
        if msg:
            print(f'{name} Instalado com sucesso!')


def start_msi():
    ...


def initializeProgram(folder: int, name: str, arguments: list[str], subFolder: str = None, msi=False):
    """
    Executa um programa a partir do caminho e do nome especificado.

    Args:
        folder (int): O índice da pasta onde o programa está localizado.
        name (str): O nome do arquivo .exe que será executado.
        arguments (List[str]): Uma lista de argumentos que serão passados para o programa.
        msi (bool): Se o arquivo é um MSI defina commo True para ser executado com msiexec.exe. Default é False.

    Returns:
        None

    """
    dir = ['0_Drivers', '1_Complementos', '2_Programas',
           '3_Configuracoes', '4_Ativacao', '5_Finalizacao']

    programPath = f'{dir[folder]}\\'
    if subFolder != None:
        programPath += f'{subFolder}\\'

    if msi == True:
        programPath += f'{name}.msi'
        command = ['msiexec.exe', '/i', programPath, *arguments]
    else:
        programPath += f'{name}.exe'
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
    print(f'Informações do Sistema Operacional:\n \
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
