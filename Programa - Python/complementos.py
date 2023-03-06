from subprocess import *


def installDotNet35():
    print()


def installJava():
    programPath = '1_Complementos\Java.exe'
    installComand = f'start /wait {programPath} /s'
    result = run(installComand, shell=True)

    return result.returncode

