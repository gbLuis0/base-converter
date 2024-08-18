from functions import *
from colorama import Fore, Style

f = Style.RESET_ALL
ng = Style.BRIGHT
verde_ng = Fore.GREEN + ng
amare = Fore.YELLOW
verme = Fore.RED
azul_ng = Fore.BLUE + ng

condicao = 1

while condicao:
    print('\x1b[2J\x1b[1;1H')
    print(f'[ {azul_ng}1{f} ] > {azul_ng}Binário{f}\n[ {azul_ng}2{f} ] > {azul_ng}Octal{f}\n[ {azul_ng}3{f} ] > {azul_ng}Hexadecimal{f}\n\n[ {verme}0{f} ] {verme}Sair{f}\n')
    opcao = int(input('>>> ').strip()[0])

    print('\x1b[2J\x1b[1;1H')
    if not opcao:
        break

    match opcao:
        case 1:
            print(f'[ {verde_ng}1{f} ] | {amare}Decimal{f} -> {verde_ng}Binário{f}\n[ {verde_ng}2{f} ] | {amare}Binário{f} -> {verde_ng}Decimal{f}\n\n[ {verme}0{f} ] {verme}Voltar{f}\n')
            opcao2 = int(input('>>> ').strip()[0])
            if not opcao2:
                continue

            valor = int(input('Valor: ').strip())
            print(bin_dec(opcao2, valor))

        case 2:
            print(f'[ {verde_ng}1{f} ] | {amare}Decimal{f} -> {verde_ng}Octal{f}\n[ {verde_ng}2{f} ] | {amare}Octal{f} -> {verde_ng}Decimal{f}\n\n[ {verme}0{f} ] {verme}Voltar{f}\n')
            opcao2 = int(input('>>> ').strip()[0])
            if not opcao2:
                continue

            valor = int(input('Valor: ').strip())
            print(oct_dec(opcao2, valor))

        case 3:
            print(f'[ {verde_ng}1{f} ] | {amare}Decimal{f} -> {verde_ng}Hexadecimal{f}\n[ {verde_ng}2{f} ] | {amare}Hexadecimal{f} -> {verde_ng}Decimal{f}\n\n[ {verme}0{f} ] {verme}Voltar{f}\n')
            opcao2 = int(input('>>> ').strip()[0])
            if not opcao2:
                continue

            valor = input('Valor: ').strip().lower()
            print(hex_dec(opcao2, valor))

        case 0:
            break

    condicao = int(input('Deseja continuar? [1/0] ').strip()[0])
