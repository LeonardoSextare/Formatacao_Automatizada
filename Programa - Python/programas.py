def perguntaOffice():
    print('Selecione a versão do Office:')
    print('[0] Nenhuma\n[1] Office 2013\n[2] Office 2016')

    while True:
        try:
            resposta = int(input('>'))
        except ValueError:
            print('ERRO! Digite um número')
        else:
            if resposta in range(0, 3):
                if resposta == 0:
                    return 0
                if resposta == 1:
                    return 2013
                if resposta == 2:
                    return 2016
            else:
                print('Opção Invalida.')



