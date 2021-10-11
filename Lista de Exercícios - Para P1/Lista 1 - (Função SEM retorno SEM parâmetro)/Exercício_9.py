# 9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.

def numerais():
    for c in range(1, 6):
        valor = int(input(f'Informe o  {c}º valor: '))
        if c == 1:
            maiorvalor = valor
            menorvalor = valor
        else:
            if valor > maiorvalor:
                maiorvalor = valor
            if valor < menorvalor:
                menorvalor = valor
    print(f'O Menor valor lido foi: \33[32m{menorvalor}\33[m e o Maior valor lido foi: \33[32m{maiorvalor}\33[m')


def main():
    numerais()


main()
