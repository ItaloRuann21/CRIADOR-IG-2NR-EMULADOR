import random


def gerar_senha_perfil():
    caracteres = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0'
    ]

    c1 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c2 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c3 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c4 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c5 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c6 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c7 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c8 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c9 = caracteres[random.randint(1, int(len(caracteres)) - 1)]
    c10 = caracteres[random.randint(1, int(len(caracteres)) - 1)]

    senha = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
    
    return senha