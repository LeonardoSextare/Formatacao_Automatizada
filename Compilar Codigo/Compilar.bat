@echo off

cd "C:\Users\Leonardo Sextare\Desktop\Formatacao_Automatizada\Compilar Codigo"

pyinstaller --noconfirm --onefile --console --icon "C:\Users\Leonardo Sextare\Desktop\Formatacao_Automatizada\Compilar Codigo\AutoFormat.ico" --name "Auto Format" --uac-admin "C:\Users\Leonardo Sextare\Desktop\Formatacao_Automatizada\Source Code\principal.py" --distpath "C:\Users\Leonardo Sextare\Desktop\Formatacao_Automatizada\Compilar Codigo"

timeout /t 1

move "./Auto Format.exe" "C:\Users\Leonardo Sextare\Documents\Ferramentas TI\!Pendrive\!!Pos Formatacao"

pause