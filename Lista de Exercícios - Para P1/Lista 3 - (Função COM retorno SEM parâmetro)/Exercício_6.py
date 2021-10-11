#6. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor bool True para par e False para ímpar.

def numeros():
    num = int(input('Informe um número: '))
    res = num % 2
    return res
def main():
    total = [ True if numeros() == 0  else False ]
    print(total)
main()