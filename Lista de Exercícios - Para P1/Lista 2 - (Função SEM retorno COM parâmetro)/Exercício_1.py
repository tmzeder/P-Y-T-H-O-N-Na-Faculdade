#1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.

def mult (num): #Variavel nomeada com parametro, num = qualquer
    resposta = num * 2
    print(f'O resultado da multiplicação do valor informado é: {resposta}')
    
def main():
    qualquer = int(input('Informe um nº qualquer: '))
    mult(qualquer)
    
main()