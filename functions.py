def bin_dec(convert=0, valor=0):
    match convert:
        case 1:
            return bin(valor)[2:]
        case 2:
            decimal = p = 0
            binStr = str(valor)[::-1]

            for i in binStr:
                decimal += int(i) * 2 ** p
                p += 1
            return decimal
            

def oct_dec(convert=0, valor=0):
    match convert:
        case 1:
            return oct(valor)[2:]
        case 2:
            decimal = p = 0
            octStr = str(valor)[::-1]

            for i in octStr:
                decimal += int(i) * 8 ** p
                p += 1
            return decimal


def hex_dec(convert=0, valor=''):
    match convert:
        case 1:
            return str(hex(int(valor)))[2:]
        case 2:
            letras = {
                'a': 10,
                'b': 11,
                'c': 12,
                'd': 13,
                'e': 14,
                'f': 15
            }
            decimal = p = 0
            hexStr = valor[::-1]

            for i in hexStr:
                if i.isalpha():
                    i = letras[i]

                decimal += int(i) * 16 ** p
                p += 1
            return decimal
