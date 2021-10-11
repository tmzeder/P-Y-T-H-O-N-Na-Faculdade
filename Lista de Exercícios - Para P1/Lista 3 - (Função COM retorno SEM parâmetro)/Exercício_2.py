#2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.

def sub():
    num1 = int(input('INFORME o 1º valor: ')) 
    num2 = int(input('INFORME o 2º valor: ')) 
    res = num1 - num2
    
    return res

def main():
    print(f'A diferença entre os valores é de: {sub()}')
    
main()