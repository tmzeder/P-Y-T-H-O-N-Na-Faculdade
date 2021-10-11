#2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.

def atribuir(num, num1):
    soma = num+num1
    return soma

def main():
    num = int(input('Informe um valor: '))
    num1 = int(input('Informe outro valor:  '))
    print(f'O resultado da soma entre os valores será: {atribuir(num, num1)}')
    
main()