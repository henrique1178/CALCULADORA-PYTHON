from utilidades_func import *

def soma():
    a = int(input('Digite um número para a soma: '))
    b = int(input('Digite outro número para a soma: '))
    somar = a + b
    return f'{a} + {b} = {somar}'


def subt():
    a = int(input('Digite um número para subtrair: '))
    b = int(input('Digite outro número para subtrair: '))
    subtrair = a - b
    return f'{a} - {b} = {subtrair}'


def multiplicar():
    a = int(input('Digite um número para multiplicar: '))
    b = int(input('Digite outro número para multiplicar: '))
    multiplicar = a * b
    return f'{a} × {b} = {multiplicar}'


def dividir():
    a = int(input('Digite um número para dividir: '))
    b = int(input('Digite outro número para dividir: '))
    
    if b == 0:
        return 'Erro: Divisão por 0 não é permitida!'
    
    dividir = a / b
    return f'{a} ÷ {b} = {dividir:.2f}'


def potencia():
    a = int(input('Digite um número para a base: '))
    b = int(input('Digite outro número para o expoente: '))
    potencia = a ** b
    expoente_formatado = formatar_potencia(a,b)
    return f'{expoente_formatado} = {potencia:.2f}'


def raiz():
    a = int(input('Digite um número para calcular a raiz: '))
    b = int(input('Digite outro número para o índice da raiz: '))

    if b == 0:
        return 'Erro: Não é possivel calcular raiz de índice ZERO.'
    
    raiz = a ** (1 / b)
    raiz_formatada = formatar_raiz(a,b)
    return f'{raiz_formatada} = {raiz:.2f}'


def log():
    a = int(input('Digite um número para calcular o log: '))
    b = int(input('Digite outro número para a base do log: '))

    if a <= 0 or b <= 0 or b == 1:
        return f'Erro: O valor deve ser positivo e a base deve ser maior que 0 e diferente de 1.'
    
    log_a = log_natural(a)
    log_b = log_natural(b)

    log_result = log_a / log_b
    log_formatado = formatar_log(b,a)
    return f'{log_formatado} = {log_result:.2f}'


def fatorial():
    a = int(input('Digite um número para calcular seu fatorial: '))

    if a < 0:
        return "Erro: Fatorial não é definido para números negativos."
    
    log = 1
    for i in range(2, a + 1):
        log *= i

    return f'{a}! = {log}'