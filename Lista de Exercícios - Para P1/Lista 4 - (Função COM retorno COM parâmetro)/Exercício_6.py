#6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
'''a) Função para construir um menu de opções para uma calculadora:

Menu de cálculos
1.   Número ao quadrado
2.   Número ao cubo
3.   Raiz do número
4.   Raiz cúbica do número
Qual é a opção desejada?

b) Desenvolva uma função para cada opção de cálculo.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

A função de desenho/construção do menu, esta chamará todas as outras passando a elas o valor digitado.'''

def funcao(menu, num):

        if menu == "1":
            resultado = num * num
            return resultado

        elif menu == "2":
            result = num ** 3
            return result

        elif menu == "3":
            resul = num ** 1/2
            return resul

        elif menu == "4":
            r = num ** 1/3
            return r

    
def menu():
    opcao = input("----------------------------"
    "\nMENU DE CÁLCULOS"
    "\n"
    "\n1. Número ao quadrado"
    "\n2. Número ao cubo"
    "\n3. Raiz quadrada"
    "\n4. Raiz cubica do número"
    "\n(Digite qualquer outra tecla para sair)"
    "\n----------------------------"
    "\n"
    "\nQUAL A OPÇÃO DESEJADA?"
    "\n ")

    return opcao


def main():

    a = menu()

    if a in ["1","2","3","4"]:
        numero = float(input("Digite um número: \n"))
        print("O resultado da sua conta é de", funcao(a, numero),"\n")

        main()
    
    else:
        print("FIM DO PROGRAMA")
    
main()