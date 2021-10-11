# 2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive). Exemplo:
#a = 2
#b = 8
#soma = 35

def somando():
    soma = 0
    
    num1 = int(input('Informe um valor: '))
    num2 = int(input('Informe um valor: '))
    for c in range(num1, num2 +1):
        soma += c
        
    print(f'Os valores informados foram: {num1,num2}.\nSomando os N números existentes entre eles temos o total de: {soma}')

def main():
    somando()
    
main()
