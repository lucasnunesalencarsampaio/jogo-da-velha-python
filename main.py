def verificar_vitoria(tabuleiro, jogador):

    if (tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) \
    or (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) \
    or (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) \
    or (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) \
    or (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) \
    or (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) \
    or (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) \
    or (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador):

        return True

    return False


tabuleiro = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

jogador = "X"

for rodada in range(9):

    print("Escolha uma posição de 1 a 9")
    posicao = int(input())

    if posicao >= 1 and posicao <= 9:

        if tabuleiro[posicao - 1] == str(posicao):

            tabuleiro[posicao - 1] = jogador

            print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
            print("---+---")
            print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
            print("---+---")
            print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

            if (tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) \
            or (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) \
            or (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) \
            or (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) \
            or (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) \
            or (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) \
            or (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) \
            or (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador):

                print(jogador, "venceu!")
                break

            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"

        else:
            print("Essa posição já está ocupada!")

    else:
        print("Posição inválida!")

