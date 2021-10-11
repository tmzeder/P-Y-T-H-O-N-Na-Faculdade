#1. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2 retornando o resultado e o apresente.

def multiplique():
    num = int(input('Informe um valor: '))
    res = num * 2
    return res

def main():
    resultado = multiplique()
    if resultado > 5:
        print(f'O resultado é: {resultado}')
    w = 1000 + multiplique()
    print(f'O resultado é : {w}')
    
main()