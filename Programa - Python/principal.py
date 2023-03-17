from functions import *
from extensions import *
from getpass import getpass

senha = getpass('Senha: \n')
if senha != 'e2g3d1j10j0':
    exit()

print(titulo('Auto Formatação by: Sextare'))

# Validate system requirements
winVersion = validateVersion()
if winVersion == False:
    input('\nEncerrando o Programa...\nPressione enter para sair...')
    exit()
else:
    print('\nSistema Compativel! Iniciando a Instalação...\n')
    sleep(1)

# Defines a Microsoft Office version to install
ofcVersion = officeSelection()

# Defines if windows will be activated
winActivate = activateWindows()

print(titulo('Instalando Complementos'))

installDotNet35(winVersion)

installDotNet7()

installJava()

installCRuntime()

installDirectX()

input('Pressione enter para sair...')
