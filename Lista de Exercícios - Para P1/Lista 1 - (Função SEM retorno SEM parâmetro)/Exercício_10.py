# 10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
# S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
# Observvação: Não pode usar vetor e função pronta da linguagem Python.

# S = 1 + 1 + 1/2! + 1/3!
# S = 1 + 1 + 0.5 + 0.16
# S = 2.66


def valores_de_S():
    valor = int(input('Informe um valor Inteiro: '))
    s = 1

    for c in range(1, valor + 1):
        fatorial = 1

        for i in range(1, c + 1):
            fatorial *= i
        s += 1/fatorial
    print(f'O valor de S é: \33[32m{s:.2f}\33[m')


def main():
    valores_de_S()


main()

#Abaixo está como o Fernando Fez: Ficou Excelente!
'''def fatorial():
    n = (int(input("Digite um número inteiro e positivo: ")))
    fat = 1
    s = 0

    for i in range (1, n + 1):
        fat *= i
        s += (1/fat)

    s += 1

    print(f"{s:.2f}")

def main():
    fatorial()

main()'''