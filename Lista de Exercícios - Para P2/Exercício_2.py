'''2. Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço.'''


class Tipo_Produto:
    codigo = 0
    nome = ''
    preco = 0.0
    
def mostrar_membros(p):
    print(f'Código: {p.codigo} \t Nome:{p.nome} \t R${p.preco:.2f}')
    
def main():
    vetor_produtos = []
    for c in range(2):
        p1 = Tipo_Produto()
        p1.codigo = int(input('Informe o Código do Produto: '))
        p1.nome = str(input('Informe o Nome do Produto: '))
        p1.preco = float(input('Informe o Preço do Produto: '))
        p1.preco = p1.preco + p1.preco * 10 / 100
        vetor_produtos.append(p1)
    for c in range(len(vetor_produtos)):
        mostrar_membros(vetor_produtos[c])
        
main()
        