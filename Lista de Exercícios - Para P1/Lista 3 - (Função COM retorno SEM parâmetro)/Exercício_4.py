#4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².

def quadrado():
    square = float(input('Informe um valor: '))
    area = square ** 2
    return area
def main():
    print(f'O valor da Área é de: {quadrado()}')

main()