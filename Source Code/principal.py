from functions import *
from extensions import *
from programs import *
from getpass import getpass

# senha = getpass('Senha: \n')
# if senha != 'e2g3d1j10j0':
#     exit()

print(titulo('Auto Formatação by: Sextare'))
# Validate system requirements
winVersion = validateVersion()
if winVersion == False:
    input('\nEncerrando o Programa...\nPressione enter para sair...')
    exit()
else:
    print('\nIniciando a Instalação...\n')
    sleep(1)

# Defines a Microsoft Office version to install
ofcVersion = officeSelection()

# Defines if windows will be activatede
winActivate = activateWindows()


print(titulo('Instalando Complementos'))
installDotNet35(winVersion)
installDotNet7()
installJava()
installDirectX()
installCRuntime()


print(titulo('Instalando Programas'))
installChrome()
installFirefox()
installOffice(ofcVersion)

input('Pressione enter para sair...')
