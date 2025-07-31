#Implementação de jogo da velha em python para estudo 
import random
print("########################### \n")
print("Bem-vindo ao Jogo da Velha! \n")
print("########################### \n")

print("Instruções:")
print("----------")

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
    contadorJogadas = 0

    if jogador == jogador1:
        print("{} começa o jogo!".format(jogador1))
        jogadorX = jogador1
        jogadorO = jogador2
    else:
        print("{} começa o jogo!".format(jogador2))
        jogadorX = jogador2
        jogadorO = jogador1

    for rodada in range(9):
        limpar_console()
        exibir_tabuleiro(tabuleiro)
        casaJogadorX = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorX)))
        while casaJogadorX < 1 or casaJogadorX > 9 or tabuleiro[casaJogadorX - 1] != ' ':
            print("Casa inválida ou já ocupada. Tente novamente.")
            casaJogadorX = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorX)))
        tabuleiro[casaJogadorX - 1] = 'X'
        contadorJogadas = contadorJogadas + 1;
        ganhouX = verifica_vitoria(tabuleiro, contadorJogadas)

        #verifica se o jogador X ganhou, se sim, limpa a tela e exibe o tabuleiro com a mensagem de vitória:
        if ganhouX:
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            print("{} venceu o jogo!".format(jogadorX))
            input("Pressione Enter para continuar...")
            break

        validaEmpate = all(casa != ' ' for casa in tabuleiro)
        if validaEmpate:
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            input("Pressione Enter para continuar...")
            break   

        #se o jogador X não ganhou, é a vez do jogador O
        #limpar a tela e aparece novamente o tabuleito com a mensagem:
        limpar_console()
        exibir_tabuleiro(tabuleiro)
        casaJogadorO = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorO)))
        while casaJogadorO < 1 or casaJogadorO > 9 or casaJogadorO or tabuleiro[casaJogadorO - 1] != ' ':
            print("Casa inválida ou já ocupada. Tente novamente.")
            casaJogadorO = int(input("{} Escolha uma casa (1-9) para jogar: ".format(jogadorO)))
        tabuleiro[casaJogadorO - 1] = 'O'
        contadorJogadas = contadorJogadas + 1
        ganhouO = verifica_vitoria(tabuleiro, contadorJogadas)

        #verifica se o jogador O ganhou, se sim, limpa a tela e exibe o tabuleiro com a mensagem de vitória:
        #encerra o jogo

        if ganhouO:
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            print("---------")
            print("{} venceu o jogo!".format(jogadorO))
            print("---------")
            input("Pressione Enter para finalizar...")
            
        #fazer validação de empate, se todar as casa de tabuleito forem diferente de ' ' e nenhum jogador ganhou, então o jogo terminou em empate
        validaEmpate = all(casa != ' ' for casa in tabuleiro)
        if validaEmpate:
            limpar_console()
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            input("Pressione Enter para continuar...")
            break   

    #Agradecer a quem jogou, e finalizar jogo.
    limpar_console()
    print("Obrigado por jogar!")
    print("Até a próxima!")

        
#Função que valida se houve vitória, se jogada válida e se o jogo terminou em empate
def verifica_vitoria(tabuleiro, rodada):
    
    if rodada < 4:  # Menos de 5 jogadas, não é possível ter vencedor
        return False
    
    #Verifica se há vitória em linhas
    for i in range(3):
        if tabuleiro[i * 3] == tabuleiro[i * 3 + 1] == tabuleiro[i * 3 + 2] != ' ':
            return True
        
    #Verifica se há vitória em colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] != ' ':
            return True
        
    #Verifica se há vitória em diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ' or tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' ':
        return True

if __name__ == "__main__":
    start()