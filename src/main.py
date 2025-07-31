#Implementação de jogo da velha em python para estudo 
import random
print("########################### \n")
print("Bem-vindo ao Jogo da Velha! \n")
print("########################### \n")

print("Instruções:")

def start():
    print("1. O tabuleiro é numerado de 0 a 8, como abaixo:")
    print("   0 | 1 | 2")
    print("   ---------")
    print("   3 | 4 | 5")
    print("   ---------")
    print("   6 | 7 | 8")
    print("2.  Cada jogador escolhe um número para marcar sua jogada.")
    print("3.  Dois jogadores jogam alternadamente, escolhendo uma casa para marcar.")
    print("4.  O jogo termina quando um jogador marca três casas em linha, coluna ou diagonal, ou se todas as casas forem preenchidas sem vencedor (empate).")
    print("5.  O jogador que começa e a sua peça (X ou O) é escolhido aleatoriamente.")
    
    jogador1 = input("Digite o nome do jogador 1: ")
    jogador1 = verificar_nome_jogador(jogador1)
    
    jogador2 = input("Digite o nome do jogador 2: ")
    jogador2 = verificar_nome_jogador(jogador2)

    jogador = random.choice([jogador1, jogador2])

    print("Bem-vindos: {} e {}".format(jogador1, jogador2))
    esperar_entrada()
    limpar_console()
    jogo_da_velha(jogador1, jogador2, jogador)

#Verifica nome de jogador 
def verificar_nome_jogador(nome):
    while nome == "" or nome == " ":
        print("Nome inválido. Por favor, digite um nome válido.")
        nome = input("Digite o nome do jogador: ")
    return nome

#função para pessoa clicar em qualquer tecla para iniciar o jogo
def esperar_entrada():
    input("Pressione Enter para começar o jogo...")

#função para limpar o console 
def limpar_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    
def exibir_tabuleiro(tabuleiro): 
    print("   ---------")
    print("  {} | {} | {}    1 | 2 | 3".format(tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print("   ---------")
    print("  {} | {} | {}    4 | 5 | 6".format(tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print("   ---------")
    print("  {} | {} | {}    7 | 8 | 9".format(tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print("   ---------")
    print("")

def jogo_da_velha(jogador1, jogador2, jogador): 
    tabuleiro = [' ' for _ in range(9)]
    if jogador == jogador1:
        print("{} começa o jogo!".format(jogador1))
        jogadorX = jogador1
        jogadorO = jogador2
    else:
        print("{} começa o jogo!".format(jogador2))
        jogadorX = jogador2
        jogadorO = jogador1

    exibir_tabuleiro(tabuleiro)


    for rodada in range(9):
        casaJogadorX = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorX)))
        while casaJogadorX < 1 or casaJogadorX > 9 or tabuleiro[casa - 1] != ' ':
            print("Casa inválida ou já ocupada. Tente novamente.")
            casa = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorX)))
        tabuleiro[casa - 1] = 'X'
        ganhou = verifica_vitoria(tabuleiro, rodada)

        if ganhou == True and rodada < 8: 
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            print("O jogador {} ganhou!".format(jogadorX))
            input("Pressione Enter para continuar...")
            break;
        else:
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            if rodada == 8:  # Se todas as casas foram preenchidas  
                print("O jogo terminou em empate!")
                input("Pressione Enter para continuar...")
                break;
        #limpar a tela e aparece novamente o tabuleito com a mensagem: Vez do jogador: 
        limpar_console()
        exibir_tabuleiro(tabuleiro)
        casaJogadorO = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorO)))
        while casaJogadorO < 1 or casaJogadorO > 9 or tabuleiro[casa - 1] != ' ':
            print("Casa inválida ou já ocupada. Tente novamente.")
            casa = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorO)))
        tabuleiro[casa - 1] = 'O'
        ganhou = verifica_vitoria(tabuleiro)

        if ganhou == True and rodada < 8: 
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            print("O jogador {} ganhou!".format(jogadorO))
            input("Pressione Enter para continuar...")
            break;
        else:
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            if rodada == 8:  # Se todas as casas foram preenchidas  
                print("O jogo terminou em empate!")
                input("Pressione Enter para continuar...")
                break;

        
#Função que valida se houve vitória, se jogada válida e se o jogo terminou em empate
def verifica_vitoria(tabuleiro, rodada):
    #Verifica se houve vitória
    if rodada < 4:  # Menos de 5 jogadas, não é possível ter vencedor
        return False
    vitoria = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
               [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
               [0, 4, 8], [2, 4, 6]] # Diagonais
    for linha in vitoria:
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] != ' ':
            return True
    # Verifica se o jogo terminou em empate
    if rodada == 8:  # Se todas as casas foram preenchidas
        print("O jogo terminou em empate!")
        return True
    return False  # Jogo ainda não terminou


if __name__ == "__main__":
    start()

# Este é um jogo da velha simples em Python, onde dois jogadores podem jogar alternadamente.