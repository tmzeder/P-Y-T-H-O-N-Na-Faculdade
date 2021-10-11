# 8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.

# se m_f < m_i
#    m_f = m_f + 60
#    h_f = h_f - 1
# se h_f < h_i
#    h_f = h_f + 24
# tot_m = m_f - m_i
# tot_h = h_f - h_i
# total = tot_h * 60 + tot_m

def jogo():
    HoraInicial = int(input('Informe o Início do jogo: '))
    HoraFinal = int(input('Informe o Término do jogo: '))
    MinInicial = int(input('Informe os Minutos Iniciais: '))
    MinFinal = int(input('Informe os Minutos Finais: '))

    if MinFinal < MinInicial:
        MinFinal = MinFinal + 60
        HoraFinal = HoraFinal - 1
    if HoraFinal < HoraInicial:
        HoraFinal = HoraFinal + 24
        TotalHoras = HoraFinal - HoraInicial
        TotalMin = MinFinal - MinInicial
        Total = TotalHoras * 60 + TotalMin
    print(f'O Total em horas é de: {TotalHoras}Hrs, de minutos é de {TotalMin}Min')
    print(f'E a Duração do Jogo foi de: \033[32m{Total}\033[m Minutos.')


def main():
    jogo()


main()
