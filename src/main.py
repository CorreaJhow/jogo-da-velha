#Implementação de jogo da velha em python para estudo 

print("Bem-vindo ao Jogo da Velha!")

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    for turno in range(9):
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez!")
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))
        
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                return
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição já ocupada, tente novamente.")
    exibir_tabuleiro(tabuleiro)
    print("Empate!")
if __name__ == "__main__":
    jogo_da_velha()

# Este é um jogo da velha simples em Python, onde dois jogadores podem jogar alternadamente.