# 7. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.

def armazenamento():
    vetor_a = []
    vetor_b = []
    for i in range(1,6):
        numero = int(input(f"Informe o {i}º valor: "))
        vetor_a.append(numero)
        resultado = 1
        for c in range(1, numero+1):
            resultado *= c
        vetor_b.append(resultado)
    return f' Elementos do Vetor A {vetor_a}, Fatoriais Vetor B {vetor_b}'



def main():
    print(armazenamento())


main()
