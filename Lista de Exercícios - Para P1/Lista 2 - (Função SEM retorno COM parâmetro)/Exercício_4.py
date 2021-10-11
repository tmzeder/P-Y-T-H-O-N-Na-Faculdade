#4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário.

def reajuste(pre, porc):
    novo = pre + ( pre * porc / 100)
    print(f'O novo valor do produto é de: R${novo:.2f}')

def main():
    preco = float(input('Informe o valor do Produto: '))
    porcentagem = float(input('Informe a porcentagem de aumento: '))
    reajuste(preco, porcentagem)
    
main()