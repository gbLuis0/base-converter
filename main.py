def bin_to_dec(bina=0):
    # estas funções vão do bin para dec e vice versa,
    # com uma variável verificando quem será convertido
    pass


def oct_to_dec(octa=0):
    pass


def hex_to_dec(hexa=0):
    pass


condicao = 1

while condicao:
    print('[ 1 ] > Binário\n[ 2 ] > Octal\n[ 3 ] > Hexadecimal\n\n[ 0 ] > Sair\n')
    opcao = int(input('>>> ').strip()[0])

    if not opcao:
        break
    decimal = int(input('Número decimal: ').strip())

    match opcao:
        case 1:
            print('Em binário:', bin(decimal)[2:])
        case 2:
            print('Em octal:', oct(decimal)[2:])
        case 3:
            print('Em hexadecimal:', hex(decimal)[2:])
        case 0:
            break

    condicao = int(input('Deseja continuar? [1/0] ').strip()[0])
