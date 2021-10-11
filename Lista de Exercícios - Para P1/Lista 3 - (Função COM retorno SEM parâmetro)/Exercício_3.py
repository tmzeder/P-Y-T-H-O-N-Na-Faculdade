#3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.

def calculo_triangular():
    base = float(input('Informe a Base: '))
    altura = float(input('Informe a Altura: '))
    resposta = base*altura/2
    return resposta
def main():
    print(f'Baseados nos valores informados, a Area é: {calculo_triangular()}')
    
main()