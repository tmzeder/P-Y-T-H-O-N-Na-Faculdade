# 4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.
# h = segundos / 3600
# r = resto(segundos / 3600)
# m = r / 60
# s = resto(r / 60)
# Observação 1: resto de uma divisão em Python %.
# Observação 2: a hora, o minuto e o segundo devem ser apresentados como números inteiros.

def conversor():
    valor = int(input('Informe um valor em segundos (sec): '))
    
    hora = valor / 3600
    r = valor % 3600
    minu = r / 60
    sec = r % 60
    
    print(f'O valor informado em horas é: \33[34m{int(hora)}Hr\33[m em minutos é: \33[35m{int(minu)} min\33[m e em segundos é: \33[32m{int(sec)}seg\33[m ')

def main():
    conversor()
    
main()
