#9. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta.

def igual(x):
    print('\33[32mTrue\33[m' if x == "Ana" else "\33[31mFalse\33[m")
def main():
    nome = str(input('Informe o Nome: '))
    igual(nome)
main()