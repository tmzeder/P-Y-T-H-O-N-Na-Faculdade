#3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.

def aumento_salarial(a, b):
    novo = a + (a*(b/100))
    return novo

def main():
    acrescimo = int(input('Informe a porcentagem de aumento: ')) 
    salario = float(input('Informe o salário atual: R$'))
    print(f'O salario reajustado será \33[32mR${aumento_salarial(salario, acrescimo)}\33[m')

main()