# 8. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo).
# Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

# 1º número perfeito: 6

# 2º número perfeito: 28

# 3º número perfeito: 486

def n_perfeito():
    perfeito = []
    for c in range(1, 497):
        soma = 0
        for c2 in range(1, c):
            if c % c2 == 0:
                soma += c2
            if c == soma:
                perfeito.append(soma)
    return perfeito


def main():
    print(n_perfeito())

main()
