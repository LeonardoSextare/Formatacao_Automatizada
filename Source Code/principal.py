from functions import *
from extensions import *
from programs import *
from systemConfig import *

print(titulo('Auto Formatação by: Sextare'))

# Validate system requirements
WIN_VERSION = validate_Version()
if WIN_VERSION:
    print('Sistema Compativel\nIniciando instalação completa...\n')
elif WIN_VERSION is None:
    print('\nVersão não suportada!! Iniciando instalação com limitações...\n')
else:
    input('\nEncerrando o Programa...\nPressione enter para sair...')
    exit()


# Defines a Microsoft Office version to install
OFFICE_VERSION = officeSelection()

# Defines if windows will be activated
# winActivate = activateWindows()


print(titulo('Instalando Complementos'))
install_DotNet35(WIN_VERSION)
install_CRuntime()
install_dotNet7()
initializeProgram(1, 'Java_Runtime', [
                   '/qn', 'AUTO_UPDATE=Disable', 'NOSTARTMENU=Enable'], msi=True)
install_DirectX()



print(titulo('Instalando Programas'))
installChrome()
installFirefox()
installOffice(OFFICE_VERSION)
install_Anydesk()
install_Winrar()
install_Adobe()

# print(titulo('Configurando o Sistema'))
# if WIN_VERSION == '1709':
#     configWindows1709()
# else:
#     print('Sistema Incopativel, etapa ignorada')


input('Pressione enter para sair...')
