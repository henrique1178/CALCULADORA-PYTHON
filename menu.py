from funcoes import *

def menu():
    print('Bem-vindo à Calculadora!')
    print('Escolha uma opção:')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Potência')
    print('6. Raiz')
    print('7. Logaritmo')
    print('8. Fatorial')
    print('9. Sair')

def calcular(opcao):
    if opcao == 1:
        print(soma())
    elif opcao == 2:
        print(subt())
    elif opcao == 3:
        print(multiplicar())
    elif opcao == 4:
        print(dividir())
    elif opcao == 5:
        print(potencia())
    elif opcao == 6:
        print(raiz())
    elif opcao == 7:
        print(log())
    elif opcao == 8:
        print(fatorial())
    else:
        print('Opção inválida. Tente novamente!')

def mostrar_menu():
    while True:
        menu()
        opcao = int(input('Digite o número da opção desejada: '))
        calcular(opcao)
        if opcao == 9:
            break

if __name__ == "__main__":
    mostrar_menu()