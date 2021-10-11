#10. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras a tem numa frase. Não use NENHUMA função pronta da linguagem Python.

def frase(x):
    soma = 0
    tamanho = len(x)
    
    for c in range(tamanho):
        if x[c] == 'a':
            soma += 1
    print(f'A letra \33[34m"A" \33[m foi encontrada {soma} Vezes na frase → \33[32m{x}\33[m')

def main():
    Sua_Frase = str(input('Escreva a Frase: ')) 
    frase(Sua_Frase)
    
main()