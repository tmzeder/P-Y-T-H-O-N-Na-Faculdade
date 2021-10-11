#2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.

def sub(x, y):
    sub = x - y
    print(f'A subtração entre os valores é de: {sub}')

def main():
    a = int(input('Informe um valor: '))
    b= int(input('Informe outro valor: '))
    sub(a, b)

main()