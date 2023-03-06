def perguntaAtivarWin():
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
