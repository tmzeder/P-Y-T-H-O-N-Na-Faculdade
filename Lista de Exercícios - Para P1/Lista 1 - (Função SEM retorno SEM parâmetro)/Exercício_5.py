#5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.
#r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo


def preços():
    preço1 = float(input('Informe o Preço Antigo!: R$'))
    preço2 = float(input('Informe o Preço Atual!: R$'))
    
    r = (100 * preço2 - 100 * preço1) / preço1
    
    print(f'O percetual de aumento entre os valores \33[32m{preço1}\33[m e \33[32m{preço2}\33[m é de \33[33mR${r:.2f}\33[m')

def main():
    preços()

main()