def computador_escolhe_jogada(n, m):
    pcRemove = 1

    while pcRemove != m:
        if (n - pcRemove) % (m+1) == 0:
            return pcRemove

        else:
            pcRemove += 1

    return pcRemove


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        usuarioRemove = int(input('Quantas peças você vai tirar? '))
        if usuarioRemove > m or usuarioRemove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogadaValida = True

    return usuarioRemove


def campeonato():
    nRodada = 1
    while nRodada <= 3:
        print()
        print('**** Rodada', nRodada, '****')
        print()
        partida()
        nRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            pcRemove = computador_escolhe_jogada(n, m)
            n = n - pcRemove
            if pcRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', pcRemove, 'peças')

            vezDoPC = False
        else:
            usuarioRemove = usuario_escolhe_jogada(n, m)
            n = n - usuarioRemove
            if usuarioRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', usuarioRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

definePartida = int(input('2 - para jogar um campeonato '))

if definePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if definePartida == 1:
        print()
        partida()
