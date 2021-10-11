#7. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.

def cal_media(nota1, nota2):
   media = (nota1+nota2) / 2
   print(f'Resultado da Média: {media}')
   
def passed (m):
    if m>= 6:
        print('Pass')
    else:
        print('Try Again!')
           
def main():
    p1 = float(input('Informe a 1º Nota:'))
    p2 = float(input('Informe a 2º Nota:'))
    cal_media(p1, p2)
    
main()