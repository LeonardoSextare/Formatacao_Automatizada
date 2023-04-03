from platform import version, system, architecture
from time import sleep
from subprocess import run


def initializeProgram(folder: int, name: str, arguments: list[str], subFolder: str=None,msi=False):
    """
    Executa um programa a partir do caminho e do nome especificado.

    Args:
        folder (int): O índice da pasta onde o programa está localizado.
        name (str): O nome do arquivo .exe que será executado.
        arguments (List[str]): Uma lista de argumentos que serão passados ​​para o programa.
        msi (bool): Se True, o arquivo é um MSI e deve ser executado com msiexec.exe. Defa
        ult é False.

    Returns:
        None

    """
    dir = ['0_Drivers','1_Complementos','2_Programas', '3_Configuracoes', '4_Ativacao', '5_Finalizacao']

    if subFolder != None:
        programPath = f'{dir[folder]}\\{subFolder}\\{name}.exe'
    else:
        programPath = f'{dir[folder]}\\{name}.exe'

    
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


def titulo(msg, tam=60):
    tamanho = len(msg) + tam
    return ('=' * tamanho + f'\n{msg:^{tamanho}}\n' + '=' * tamanho)


def validateVersion():
    sysRequeriments = ['10.0.16299']

    print('Verificando compatibidade...\n')
    print('Versão do Sistema:\n' + system(),
          version(), architecture()[0])

    if system() != 'Windows':
        print('Sistema Operacional não Suportado')
        return False
    elif version() not in sysRequeriments:
        print('Versão do Windows não Suportada')
        if str(input('Deseja continuar a instalação de forma limitada? [S/N]')[0].lower()) in 's':
            return '0'
        else:
            return False
    elif architecture()[0] != '64bit':
        print('Arquitetura não Suportada')
        return False
    else:
        if version() == sysRequeriments[0]:
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
                    return '0'
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
