def bin_dec(convert=0, valor=0):
    match convert:
        case 1:
            return bin(valor)[2:]
        case 2:
            decimal = p = 0
            binStr = str(valor)[::-1]

            for i in binStr:
                i = int(i) * 2
                if i == 0:
                    p += 1
                    continue
                decimal += i ** p
                p += 1
            return decimal
            

def oct_dec(convert=0, valor=0):
    match convert:
        case 1:
            return oct(valor)[2:]


def hex_dec(convert=0, valor=0):
    match convert:
        case 1:
            return hex(valor)[2:]


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

            valor = int(input('Valor: ').strip())
            print(hex_dec(opcao2, valor))

        case 0:
            break

    condicao = int(input('Deseja continuar? [1/0] ').strip()[0])
