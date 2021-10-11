#6. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário.

def tabuada(tab):
    for c in range(1, 11):
        print(f"{tab} x {c:2} = {tab * c}")
        
def main():
    tab = int(input('Informe o Nº que deseja saber a Tabuada: '))
    tabuada(tab)
main()