#5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.

def aumento(salario_hoje, percentual):
    novo = salario_hoje + (salario_hoje * percentual / 100)
    return novo + novo

def main():
    porcentagem = int(input('Informe o percentual de aumento: '))
    soma_hoje = soma_novo = 0
    for c in range(1, 11):
        salario = float(input(f'Informe o salário do {c}º Funcionário: '))
        novo = aumento(salario, porcentagem)
        soma_novo += novo
        soma_hoje += salario
        print(f'Será gasto no salário do {c}º Funcionário: \33[32mR${novo - salario:.2f}\33[m!')
    print(f'Após o aumento a diferença será de : \33[32mR${soma_novo - soma_hoje:.2f}\33[m!')
    
main()
        