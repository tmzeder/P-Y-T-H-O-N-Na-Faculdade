#7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.
#N1, N2 e N3 são notas.
#
#P1, P2 e P3 são pesos.
#
#Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)

def medias_alunos():
    N1 = float(input('Informe a 1ª Nota: '))
    N2 = float(input('Informe a 2ª Nota: '))
    N3 = float(input('Informe a 3ª Nota: '))
    letras = str(input('[A] Para Media Aritmetica ou [P] para Média ponderada: ')).upper()
     

    if letras == 'A':
        media = (N1+N2+N3) / 3
        print(f'A Media Aritmética das notas informadas é: \33[32m{media:.2f}\33[m')
    elif letras == 'P':
        media = (N1 * 5 + N2 * 3 + N3 * 2 ) / (5 + 3 + 2)
        print(f'A Média Ponderada das notas informadas é: \33[32m{media:.2f} \33[m')
    
        
    
    
    
    
def main():
    medias_alunos()

main()
    
