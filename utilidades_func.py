def formatar_potencia(base, expoente):

    expoentes_unicode = {
        0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 
        5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'
    }
    
    expoente_str = ''.join(expoentes_unicode[int(digit)] for digit in str(abs(expoente)))
    
    if expoente < 0:
        expoente_str = f'⁻{expoente_str}'

    return f'{base}{expoente_str}'

def formatar_raiz(base, indice):
    return f'√{base} (índice {indice})'


def formatar_log(base, valor):
    base_str = f'₁{base}' if base != 10 else ''
    return f'log{base_str}({valor})'


def log_natural(x, n=1000):
    resultado = 0
    termo = (x - 1) / (x + 1)
    for i in range(n):
        resultado += (termo ** (2 * i + 1)) / (2 * i + 1)
    return 2 * resultado