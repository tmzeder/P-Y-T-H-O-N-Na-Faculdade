#1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.


def atribuir(num):
    mult = num*2
    return mult

def main():
    num = int(input('Informe um valor: '))
    
    print(f'O resultado da multiplicação será: {atribuir(num)}')
    
main()