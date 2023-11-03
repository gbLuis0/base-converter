from functions import *

condicao = 1

while condicao:
    print('\x1b[2J\x1b[1;1H')
    print('[ 1 ] > Binário\n[ 2 ] > Octal\n[ 3 ] > Hexadecimal\n\n[ 0 ] > Sair\n')
    opcao = int(input('>>> ').strip()[0])

    print('\x1b[2J\x1b[1;1H')
    if not opcao:
        break

    match opcao:
        case 1:
            print('[ 1 ] | Decimal -> Binário\n[ 2 ] | Binário -> Decimal\n\n[ 0 ] | Voltar\n')
            opcao2 = int(input('>>> ').strip()[0])
            if not opcao2:
                continue

            valor = int(input('Valor: ').strip())
            print(bin_dec(opcao2, valor))

        case 2:
            print('[ 1 ] | Decimal -> Octal\n[ 2 ] | Octal -> Decimal\n\n[ 0 ] | Voltar\n')
            opcao2 = int(input('>>> ').strip()[0])
            if not opcao2:
                continue

            valor = int(input('Valor: ').strip())
            print(oct_dec(opcao2, valor))

        case 3:
            print('[ 1 ] | Decimal -> Hexadecimal\n[ 2 ] | Hexadecimal -> Decimal\n\n[ 0 ] | Voltar\n')
            opcao2 = int(input('>>> ').strip()[0])
            if not opcao2:
                continue

            valor = input('Valor: ').strip().lower()
            print(hex_dec(opcao2, valor))

        case 0:
            break

    condicao = int(input('Deseja continuar? [1/0] ').strip()[0])
