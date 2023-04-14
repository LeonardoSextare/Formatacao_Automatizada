from subprocess import run
from functions import *


def disableWindowsUpdate():
    run(['powershell', 'Expand-Archive', '-Path', '"3_Configuracoes\\Win_Update_Blocker\\Win_Update_Blocker.zip"',
        '-DestinationPath', '"3_Configuracoes\\Win_Update_Blocker\\."', '-Force'])

    try:
        disable = run(
            ['3_Configuracoes\\Win_Update_Blocker\\Win_Update_Blocker.exe', '/D', '/P'])
    except FileNotFoundError:
        print('Programa não encontrado')
    except Exception as error:
        print(f'ERRO! {error}')
    else:
        if disable.returncode == 0:
            print('Windows Update Desativado')
        else:
            print(
                f'Ocorreu um erro ao Desativar os Updates\nCodigo: {disable.returncode}')


def configWindows1709():
    disableWindowsUpdate()
    # Disable Background Apps
    createRegKey('HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications',
                 'GlobalUserDisabled', 0, '1')

    # Disable Auto Repair
    run(['bcdedit', '/set', '{default}', 'recoveryenabled', 'no'])

    # Disable UAC
    createRegKey('HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System',
                 'EnableLUA', 0, '0')

    # Shows "This Computer" on open Explorer Files
    createRegKey(
        'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'LaunchTo', 0, '1')

    # Hide "Task Viewer" from taskbar
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'ShowTaskViewButton', 0, '0')

    # Hide "People" from taskbar
    createRegKey(
        'HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\People', 'PeopleBand', 0, '0')

    # Disable Web Search on Start Menu
    createRegKey('HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search',
                 'DisableWebSearch', 0, '1')
    createRegKey('HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search',
                 'BingSearchEnabled', 0, '0')

    # Search Bar Mode
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search',
                 'SearchboxTaskbarMode', 0, '1')

    # Disable Transparency
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize',
                 'EnableTransparency', 0, '0')

    # Adjust Perfomance and Aparency
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects',
                    'VisualFXSetting', 0, '3')
    createRegKey('HKEY_CURRENT_USER\Control Panel\Desktop',
                    'UserPreferencesMask', 2, '9012038010000000')
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced',
                    'TaskbarAnimations', 0, '0')
    createRegKey('HKEY_CURRENT_USER\Control Panel\Desktop\WindowMetrics',
                    'MinAnimate', 1, '0')
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\DWM',
                    'EnableAeroPeek', 0, '0')
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced',
                    'ListviewAlphaSelect', 0, '0')
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\DWM',
                    'AlwaysHibernateThumbnails', 0, '0')

    # Disable Telemetry
    createRegKey('HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection',
                'AllowTelemetry', 0, '0')
    createRegKey('HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection',
                'MaxTelemetryAllowed', 0, '0')
    createRegKey('HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection',
                'AllowTelemetry', 0, '0')
    createRegKey('HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\DataCollection',
                'AllowTelemetry', 0, '0')
    createRegKey('HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\DataCollection',
                'MaxTelemetryAllowed', 0, '0')

    # Disable Wifi Reporting e Auto-Connect in Public Hotspots
    createRegKey('HKLM\SOFTWARE\Microsoft\PolicyManager\default\WiFi',
                'AllowWiFiHotSpotReporting', 'Value', 0, '0')
    createRegKey('HKLM\SOFTWARE\Microsoft\PolicyManager\default\WiFi',
                'AllowAutoConnectToWiFiSenseHotspots', 'Value', 0, '0')

    # Disable Xbox Game Bar
    createRegKey('HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR',
                'AppCaptureEnabled', 0, '0')
    createRegKey('HKEY_CURRENT_USER\System\GameConfigStore',
                'GameDVR_Enabled', 0, '0')
    createRegKey('HKEY_CURRENT_USER\System\GameConfigStore',
                'GameDVR_FSEBehavior', 0, '0')
