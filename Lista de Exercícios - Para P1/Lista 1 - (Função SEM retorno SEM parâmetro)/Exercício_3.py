# 3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.Exemplo:
# a = 5
# b = 1
# c = 10
# qtde = 2
# Números divisíveis 5, 10

def divisão():
   num1 = int(input('Informe o 1º valor: '))
   num2 = int(input('Informe o 2º valor: '))
   num3 = int(input('Informe o 3º valor: '))
   cont = 0
   valores = ''
   for c in range(num2, num3 + 1):
      if c % num1 == 0:
         cont += 1  
         valores += str(c) + ' → ' 
   print(f'Temos {cont} valores divisiveis por {num1} que são: {valores}')

def main():
    divisão()
    
main()