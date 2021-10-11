#8. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
'''a) Função para construir um menu de opções para uma calculadora:

*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 
b) Desenvolva uma função para cada opção de cálculo.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.'''


def menu():
    opcao = input("----------------------------"
    "\nMINHA CALCULADORA"
    "\n"
    "\n+ SOMA dois números"
    "\n- SUBTRAI dois números"
    "\n* MULTIPLICA doid números"
    "\n/ DIVIDE dois números"
    "\n(Digite qualquer outra tecla para sair)"
    "\n----------------------------"
    "\n"
    "\nQUAL A OPÇÃO DESEJADA?"
    "\n ")

    return opcao

def soma(num1, num2):
    return f"O resultado da soma é {num1 + num2}"

def subtracao(num1, num2):
    return f"O resultado da subtraçao é {num1 - num2}"

def multiplicacao(num1, num2):
    return f"O resultado da multiplição é {num1 * num2}"

def divisao(num1, num2):

    if num2 > 0:
        return f"O resultado da divisão é {num1 / num2}"

    else:
        return "O resultado esta fora do intervalo"

def main():
    a = menu()

    while a == '+' or a == '-' or a == '*' or a == '/':

        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))

        if a == '+':
            print(soma(n1, n2))
        if a == '-':
            print(subtracao(n1, n2))
        if a == '*':
            print(multiplicacao(n1,n2))
        if a == '/':
            print(divisao(n1, n2))
        a = menu()
    print('\nFIM DO PROGRAMA')
main()