#6. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação
#Neste exemplo foi escolhido o número 9.
#1    
#2     4
#3     6     9
#4     8    12    16
#5    10    15    20    25
#6    12    18    24    30    36
#7    14    21    28    35    42    49
#8    16    24    32    40    48    56    64   
#9    18    27    36    45    54    63    72    81
#for i = 1 até n
#   for j = 1 até i
# 
#Observação: configure o print para não pular linha


def calculo():
    num = int(input('Informe um valor entre 1 e 9: '))
    
    for c in range(1, num + 1):
        for c2 in range (1, c + 1):
            resultado =  c * c2
            print(resultado, end=' →\t ')
        print()
            
def main():
    calculo()

main()