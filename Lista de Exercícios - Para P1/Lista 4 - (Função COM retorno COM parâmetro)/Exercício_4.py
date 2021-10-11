#4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.

def media(a, b):
    media_prova = (a + b) / 2
    return media_prova

def resultado(a):
    if a > 6:
        return 'Aprovado!'
    else: return 'Reprovado!'

def main():
    prova_a = float(input('Nota da 1º Prova: '))
    prova_b = float(input('Nota da 2ª Prova: '))
    res = media(prova_a, prova_b)
    print(f'A média do Aluno foi de : {res:.1f} e ele foi: {resultado(res)}')

main()