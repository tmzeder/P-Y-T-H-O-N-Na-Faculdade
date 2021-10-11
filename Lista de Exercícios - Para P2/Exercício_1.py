'''1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.'''

class Tipo_Produto:
    codigo = 0
    nome = ''
    preco = 0.0
    
def mostrar_membros(p):
    print(f'\n Código: {p.codigo} \t Nome:{p.nome} \t R${p.preco:.2f}')
    
def main():
    #1º passo será apresentar uma variavel que representara a estrutura Tipo_Produto
    p1 = Tipo_Produto()
    p1.codigo = int(input('Informe o Código do Produto: '))
    p1.nome = str(input('Informe o Nome do Produto: '))
    p1.preco = float(input('Informe o Preço do Produto: '))
    mostrar_membros(p1)
    p1.preco = p1.preco + p1.preco * 10 / 100
    mostrar_membros(p1)
    
    p2 = Tipo_Produto()
    p2.codigo = int(input('Informe o Código do Produto: '))
    p2.nome = str(input('Informe o Nome do Produto: '))
    p2.preco = float(input('Informe o Preço do Produto: '))
    mostrar_membros(p2)
    p2.preco = p2.preco + p1.preco * 10 / 100
    mostrar_membros(p2)
    
    mostrar_membros(p1)
    mostrar_membros(p2)

main()