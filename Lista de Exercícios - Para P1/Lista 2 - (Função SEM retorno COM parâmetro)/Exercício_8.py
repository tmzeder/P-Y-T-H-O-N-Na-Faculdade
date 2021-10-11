# 8. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.

def P_I(x):
    resto = x % 2
    resultado(resto)


def resultado(x):
    print('O valor informado é PAR' if x == 0 else 'O valor iformado é IMPAR')


def main():
    valor = int(input('Informe um valor inteiro: '))
    P_I(valor)


main()
