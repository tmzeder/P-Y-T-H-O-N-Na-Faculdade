#3. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%

def reajustar(a):
    x = a * 1.09
    print(f'O valor reajustado é de: {x}')

def main():
    preco_produto = float(input('Informe o valor do Produto: '))
    reajustar(preco_produto)
    
main()