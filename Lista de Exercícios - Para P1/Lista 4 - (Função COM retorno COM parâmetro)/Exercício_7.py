# 7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
'''a) Função para construir um menu de opções para uma calculadora:

*** Minha Calculadora ***
Digite um número.....:
Digite outro número..:
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja?
b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.'''


def menu():
    print('\n*** Minha Calculadora *** ')
    print('+ Soma dois números ')
    print('- Subtrai dois números ')
    print('* Multiplica dois números ')
    print('/ Divide dois números ')
    alternativas = input('Qual opção deseja? ')
    return alternativas

def soma(num, num1):
    print(f'O produto da soma é: {num+num1}')
def subtracao(num, num1):
    print(f'O produto da subtracao é: {num-num1}')
def multiplicacao(num, num1):
    print(f'O produto da multiplicacao é: {num*num1}')
def divisao(num, num1):
    if num1 > 0:
        print(f'O produto da divisao é: {num/num1:.2f}')
    else: print('Inpossivel realizar a divisão! ')

def main():
    opcao = menu()
    while opcao == '+' or opcao == '-' or opcao == '*' or opcao == '/':
        numero_1 = int(input('Informe um numero: '))
        numero_2 = int(input('Informe outro numero: '))
        if opcao == '+':
            soma(numero_1, numero_2)
        if opcao == '-':
            subtracao(numero_1, numero_2)    
        if opcao == '*':
            multiplicacao(numero_1, numero_2)
        if opcao == '/':
            divisao(numero_1, numero_2)
        opcao = menu()
    print('FIM DO PROGRAMA!')

main()
        