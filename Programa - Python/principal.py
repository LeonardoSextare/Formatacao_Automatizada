from Modulos import *
from programas import *
from complementos import *
from ativacao import *
from time import sleep


print(titulo('Auto Formatação by: Sextare'))
if compatibidade() == False:
    input('\nEncerrando o Programa...\nPressione enter para sair...')
    exit()

print('Sistema Compativel! Iniciando a Instalação...\n')
sleep(1)

versaoOFFC = perguntaOffice()
ativarWindows = perguntaAtivarWin()

print(titulo('Instalando Complementos'))

install(installJava(), 'Java')
