#9.(Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).
#- Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
#- Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
#- Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
#- Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.

idade = []
sexo = []
olho = []
cabelo = []

def cadastro():
    for c1 in range(3):
        idade.append(int(input('Informe a idade: ')))
        sexo.append(input('Digite M para masculino ou F para feminino: '))
        olho.append(input('Digite A para azul ou C para castanho: '))
        cabelo.append(input('Digite L para louros P para pretos ou C para castanhos: '))
        
def media_idade():
    med_idade = 0
    cont = 0
    for c2 in range(len(idade)):
        if olho[c2] == 'C' or olho[c2] == 'c' and cabelo[c2] == 'P' or cabelo[c2] == 'p':
            med_idade += idade[c2]
            cont += 1
    if cont > 0:
        med_idade /= cont
    return med_idade

def maior_idade():
    maior = 0
    for c3 in range(len(idade)):
        if idade[c3] > maior:
            maior = idade[c3]
    return maior

def idade_feminino():
    cont = 0
    for c4 in range(len(idade)):
        if idade[c4] > 18 and idade[c4] < 35:
            if sexo[c4] == 'F' or sexo[c4] == 'f':
                if olho[c4] == 'A or O' or olho[c4] =='a':
                    if cabelo[c4] == 'L' or cabelo[c4] == 'l':
                        cont += 1
    print(cont,'Contador')
    
    return cont

def sair():
    return print('Até a proxima!')

def menu():
    print('\nMENU DE OPÇÕES:')
    print('0 - Para Sair ')
    print('1 - Cadastrar Pesquisa ')
    print('2 - Media de Idade, Olhos Castanhos e Olhos Pretos ')
    print('3 - Maior Idade ')
    print('4 - Quantidade de pessoas com Olhos Azuis e Cabelos Louros ')
    print('DIGITE A OPÇÃO DESEJADA ')
    opção = int(input(''))
    print('')
    
    if opção == 0:
        sair()
    elif opção == 1:
        cadastro()
        menu()
    elif opção == 2:
        media_idade()
        print(f' A media de idade das mulheres de olhos castanhos e cabelos pretos é: {media_idade()}')
        menu()
    elif opção == 3:
        print(f'A maior idade entre os cadastrados é: {maior_idade()}')
        main()
    elif opção == 4:
        idade_feminino()
        menu()
def main():
    menu()
main()
         


