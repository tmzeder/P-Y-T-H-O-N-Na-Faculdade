# 5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor.
# Exemplo:
#    a = 2
#    b = 8
#    // 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
#    r = 35

def soma_num(x, y):
    acumulo = 0
    while x <= y:
        x += 1
    print(f'O total é de: {acumulo}')


def main():
    a = int(input('Informe um Número: '))
    b = int(input('Informe outro Número: '))
    soma_num(a, b)


main()
