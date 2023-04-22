from subprocess import *
from functions import *
from shutil import *
from os import path, remove
from time import sleep
import keyboard



def configWindows1709():
    disable_WindowsUpdate()
    disable_autoRepair()
    change_wallpaper()
    regImport(1709) # Configures system by windows regkeys
    config_Powerplan()
    clean_StartMenuTiles()
    ...


def configWindows22H2():
    disable_WindowsUpdate()
    disable_autoRepair()
    change_wallpaper()
    config_Powerplan()
    clean_StartMenuTiles()
    ...


def disable_WindowsUpdate():
    try:
        print('Desabilitando Windows Update...')

        extractZip('3_Configuracoes\\Win_Update_Blocker\\Win_Update_Blocker.zip',
                   '3_Configuracoes\\Win_Update_Blocker\\.')
        program_install('Desativar Update',
                        '3_Configuracoes\\Win_Update_Blocker\\Win_Update_Blocker.exe', ['/D', '/P'])
    except:
        print('Ocorreu um erro ao desabilitar o Windows Update!\n')
    else:
        print('Windows Update desabilitado!\n')


def disable_autoRepair():
    command = ['bcdedit', '/set', '{default}', 'recoveryenabled', 'no']

    try:
        print('Desabilitando reparo automatico...')
        run(command, check=True, stdout=DEVNULL)
    except CalledProcessError as error:
        print(f'ERRO! Falha ao alterar o registro.\n \
        Codigo:{error.returncode}\n')

    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}')
    else:
        print(f'Reparo Automatico desabilitado com sucesso!\n')


def regImport(version):
    try:
        print('Alterando as conigurações...')
        run(['reg', 'import',
            f'3_Configuracoes\\Configs_{version}.reg'], stdout=DEVNULL)
    except FileNotFoundError:
        print('ERRO! Arquivo não encontrado\n')
    except CalledProcessError as error:
        print(f'ERRO! Falha na execução do comando.\n \
              Codigo: {error.__class__}')
    except Exception as error:
        print(f'ERRO desconhecido! Tipo: {error.__class__}\n')
    else:
        print('Registro importado com sucesso!\n')


def change_wallpaper():
    try:
        print('Trocando o papel de parede...')
        copy('3_Configuracoes\\Wallpaper.jpg',
             'C:\\Windows\\Web\\Wallpaper\\Windows')
        
        if create_RegKey('HKEY_CURRENT_USER\Control Panel\Desktop',
                         'Wallpaper', 'REG_SZ', 'C:\\Windows\\Web\\Wallpaper\\Windows\\Wallpaper.jpg') is True:
            sleep(2)
            run(['RUNDLL32.EXE', 'user32.dll,UpdatePerUserSystemParameters'])
            print('Papel de Parede trocado com sucesso!\n')
        else:
            print('Falha ao trocar o papel de parede!\n')
    except Exception as error:
        print(f'ERRO desconhecido! Tipo:{error.__class__}\n')
    

def config_Powerplan():
    POWER_PLAN = '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'
    COMMAND = [['powercfg', '-setacvalueindex', POWER_PLAN], 
               ['powercfg', '-setdcvalueindex', POWER_PLAN]]
    
    CONFIGS = [
            ("fea3413e-7e05-4911-9a71-700331f1c294", "0e796bdb-100d-47d6-a2d5-f7d2daa51f51", '0'),
            ("fea3413e-7e05-4911-9a71-700331f1c294", "0e796bdb-100d-47d6-a2d5-f7d2daa51f51", '0'),
            ("0012ee47-9041-4b5d-9b77-535fba8b1442", "6738e2c4-e8a5-4a42-b16a-e040e769756e", '0'),
            ("0012ee47-9041-4b5d-9b77-535fba8b1442", "6738e2c4-e8a5-4a42-b16a-e040e769756e", '300'),
            ("02f815b5-a5cf-4c84-bf20-649d1f75d3d8", "4c793e7d-a264-42e1-87d3-7a0d2f523ccd", '1'),
            ("02f815b5-a5cf-4c84-bf20-649d1f75d3d8", "4c793e7d-a264-42e1-87d3-7a0d2f523ccd", '0'),
            ("0d7dbae2-4294-402a-ba8e-26777e8488cd", "309dce9b-bef4-4119-9921-a851fb12f0f4", '0'),
            ("0d7dbae2-4294-402a-ba8e-26777e8488cd", "309dce9b-bef4-4119-9921-a851fb12f0f4", '1'),
            ("19cbb8fa-5279-450e-9fac-8a3d5fedd0c1", "12bbebe6-58d6-4636-95bb-3217ef867c1a", '0'),
            ("19cbb8fa-5279-450e-9fac-8a3d5fedd0c1", "12bbebe6-58d6-4636-95bb-3217ef867c1a", '1'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "29f6c1db-86da-48c5-9fdb-f2b67b1f44da", '0'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "29f6c1db-86da-48c5-9fdb-f2b67b1f44da", '0'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "94ac6d29-73ce-41a6-809f-6363ba21b47e", '0'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "94ac6d29-73ce-41a6-809f-6363ba21b47e", '0'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "9d7815a6-7ee4-497e-8888-515a05f02364", '0'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "9d7815a6-7ee4-497e-8888-515a05f02364", '900'),
            ("238c9fa8-0aad-41ed-83f4-97be242c8f20", "bd3b718a-0680-4d9d-8ab2-e1d2b4ac806d", '1'),
            ('238c9fa8-0aad-41ed-83f4-97be242c8f20', 'bd3b718a-0680-4d9d-8ab2-e1d2b4ac806d', '1'),
            ('2a737441-1930-4402-8d77-b2bebba308a3', '48e6b7a6-50f5-4782-a5d4-53bb8f07e226', '0'),
            ('2a737441-1930-4402-8d77-b2bebba308a3', '48e6b7a6-50f5-4782-a5d4-53bb8f07e226', '1'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', '5ca83367-6e45-459f-a27b-476b1d01c936', '2'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', '5ca83367-6e45-459f-a27b-476b1d01c936', '2'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', '7648efa3-dd9c-4e3e-b566-50f929386280', '3'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', '7648efa3-dd9c-4e3e-b566-50f929386280', '3'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', '96996bc0-ad50-47ec-923b-6f41874dd9eb', '1'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', '96996bc0-ad50-47ec-923b-6f41874dd9eb', '1'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', 'a7066653-8d6c-40a8-910e-a1f54b84c7e5', '2'),
            ('4f971e89-eebd-4455-a8de-9e59040e7347', 'a7066653-8d6c-40a8-910e-a1f54b84c7e5', '2'),
            ('501a4d13-42af-4429-9fd1-a8218c268e20', 'ee12f906-d277-404b-b6da-e5fa1a576df5', '0'),
            ('501a4d13-42af-4429-9fd1-a8218c268e20', 'ee12f906-d277-404b-b6da-e5fa1a576df5', '1'),
            ('54533251-82be-4824-96c1-47b60b740d00', '893dee8e-2bef-41e0-89c6-b55d0929964c', '99'),
            ('54533251-82be-4824-96c1-47b60b740d00', '893dee8e-2bef-41e0-89c6-b55d0929964c', '1'),
            ('54533251-82be-4824-96c1-47b60b740d00', 'bc5038f7-23e0-4960-96da-33abaf5935ec', '100'),
            ('54533251-82be-4824-96c1-47b60b740d00', 'bc5038f7-23e0-4960-96da-33abaf5935ec', '80'),
            ('54533251-82be-4824-96c1-47b60b740d00', '94d3a615-a899-4ac5-ae2b-e4d8f634367f', '1'),
            ('54533251-82be-4824-96c1-47b60b740d00', '94d3a615-a899-4ac5-ae2b-e4d8f634367f', '1'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', 'fbd9aa66-9553-4097-ba44-ed6e9d65eab8', '1'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', 'fbd9aa66-9553-4097-ba44-ed6e9d65eab8', '1'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', '17aaa29b-8b43-4b94-aafe-35f64daaf1ee', '0'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', '17aaa29b-8b43-4b94-aafe-35f64daaf1ee', '300'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', '3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e', '900'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', '3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e', '300'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', 'aded5e82-b909-4619-9949-f5d71dac0bcb', '100'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', 'aded5e82-b909-4619-9949-f5d71dac0bcb', '75'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', 'f1fbfde2-a960-4165-9f88-50667911ce96', '75'),
            ('7516b95f-f776-4464-8c53-06167f40cc99', 'f1fbfde2-a960-4165-9f88-50667911ce96', '50'),
            ('9596fb26-9850-41fd-ac3e-f7c3c00afd4b', '03680956-93bc-4294-bba6-4e0f09bb717f', '1'),
            ('9596fb26-9850-41fd-ac3e-f7c3c00afd4b', '03680956-93bc-4294-bba6-4e0f09bb717f', '1'),
            ('9596fb26-9850-41fd-ac3e-f7c3c00afd4b', '34c7b99f-9a6d-4b3c-8dc7-b6693b78cef4', '0'),
            ('9596fb26-9850-41fd-ac3e-f7c3c00afd4b', '34c7b99f-9a6d-4b3c-8dc7-b6693b78cef4', '1'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', '637ea02f-bbcb-4015-8e2c-a1c7b9c0b546', '3'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', '637ea02f-bbcb-4015-8e2c-a1c7b9c0b546', '3'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', '9a66d8d7-4ff7-4ef9-b5a2-5a326ca2a469', '5'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', '9a66d8d7-4ff7-4ef9-b5a2-5a326ca2a469', '5'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', '8183ba9a-e910-48da-8769-14ae6dc1170a', '15'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', '8183ba9a-e910-48da-8769-14ae6dc1170a', '15'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', 'bcded951-187b-4d05-bccc-f7e51960c258', '1'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', 'bcded951-187b-4d05-bccc-f7e51960c258', '1'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', 'd8742dcb-3e6a-4b3c-b3fe-374623cdcf06', '0'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', 'd8742dcb-3e6a-4b3c-b3fe-374623cdcf06', '0'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', 'f3c5027d-cd16-4930-aa6b-90db844a8f00', '4'),
            ('e73a048d-bf27-4f12-9731-8b2076e8891f', 'f3c5027d-cd16-4930-aa6b-90db844a8f00', '4')
            ]

    try:
        print('Configurando o plano de energia...')
        hibernate = run(['powercfg', '-setactive', POWER_PLAN])
        print(hibernate.returncode)
        run(['powercfg', '-h', 'on'])

        for i in range(0,len(CONFIGS), 2):
            run([*COMMAND[0], *CONFIGS[i]])
            run([*COMMAND[1], *CONFIGS[i+1]])
        
    except Exception as error:
        print(f'ERRO desconhecido{error.__class__}\n')
    else:
        print('Plano de Energia configurado com sucesso!\n')


def clean_StartMenuTiles():
    LAYOUT_FILE_PATH = 'C:\\Windows\\StartMenuLayout.xml'
    LAYOUT_FILE = """<LayoutModificationTemplate xmlns:defaultlayout="http://schemas.microsoft.com/Start/2014/FullDefaultLayout" xmlns:start="http://schemas.microsoft.com/Start/2014/StartLayout" Version="1" xmlns:taskbar="http://schemas.microsoft.com/Start/2014/TaskbarLayout" xmlns="http://schemas.microsoft.com/Start/2014/LayoutModification">
    <LayoutOptions StartTileGroupCellWidth="6" />
    <DefaultLayoutOverride>
        <StartLayoutCollection>
            <defaultlayout:StartLayout GroupCellWidth="6" />
        </StartLayoutCollection>
    </DefaultLayoutOverride>
</LayoutModificationTemplate>
"""
    try:
        print('Removendo Tiles do menu iniciar...')
        if path.exists(LAYOUT_FILE_PATH):
            remove(LAYOUT_FILE_PATH)

        with open(LAYOUT_FILE_PATH, mode='x') as file:
            file.write(LAYOUT_FILE)

        for i in ('HKLM', 'HKCU'):
            create_RegKey(f'{i}\SOFTWARE\Policies\Microsoft\Windows\Explorer', 'LockedStartLayout', 'REG_DWORD' , '1')
            create_RegKey(f'{i}\SOFTWARE\Policies\Microsoft\Windows\Explorer', 'StartLayoutFile', 'REG_SZ' , LAYOUT_FILE_PATH)

        for i in range(2):
            run(['taskkill', '/f', '/im', 'explorer.exe'], stdout=DEVNULL)
            sleep(2)
            run(['explorer.exe'])
            sleep(5)
            keyboard.press_and_release('win')
            sleep(5)

            if i == 0:
                for i in ('HKLM', 'HKCU'):
                    create_RegKey(f'{i}\SOFTWARE\Policies\Microsoft\Windows\Explorer', 'LockedStartLayout', 'REG_DWORD' , '0')
            
                remove(LAYOUT_FILE_PATH)
    except Exception as error:
        print(f'ERRO desconhecido\nTipo: {error.__class__}\n')
    else:
        print('Tiles removidos com sucesso!\n')
    

