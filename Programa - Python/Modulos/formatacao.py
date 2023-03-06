def titulo(msg, tam=60):
    tamanho = len(msg) + tam
    return ('=' * tamanho  + f'\n{msg:^{tamanho}}\n' + '=' * tamanho)
