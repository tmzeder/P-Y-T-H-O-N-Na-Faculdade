# 5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.

def numeros():
    num = int(input('Informe um número: '))
    res = num % 2
    return res
def main():
    total = ['O valor informado É Par' if numeros() == 0 else 'O valor informado É Impar.']
    print(total)
main()


