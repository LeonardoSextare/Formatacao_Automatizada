from functions import *
from extensions import *
from programs import *
from getpass import getpass

senha = getpass('Senha: \n')
if senha != 'palmeirasrocha1':
    exit()

print(titulo('Auto Formatação by: Sextare'))
# Validate system requirements
winVersion = validateVersion()
if winVersion == False:
    input('\nEncerrando o Programa...\nPressione enter para sair...')
    exit()
elif winVersion == '0':
    print('Sistema incopativel\nIniciando instalação limitada...')
else:
    print('Sistema Compativel\nIniciando instalação completa...')

# Defines a Microsoft Office version to install
ofcVersion = officeSelection()

# Defines if windows will be activated
winActivate = activateWindows()


print(titulo('Instalando Complementos'))
installDotNet35(winVersion)
initializeProgram(1, '.Net_7.0.4_Runtime', ['/s'])
installJava()
initializeProgram(1, 'DXSETUP', ['/silent'], subFolder='DirectX')
installCRuntime()


print(titulo('Instalando Programas'))
installChrome()
installFirefox()
installOffice(ofcVersion)
#installAnydesk()
initializeProgram(2, 'Anydesk', ['--install',
                  'C:\Program Files (x86)\AnyDesk', '--silent'])
installTeamviewer()
initialize(2, 'Winrar', ['/S'])
installDeluge()
installAdobe()

input('Pressione enter para sair...')
