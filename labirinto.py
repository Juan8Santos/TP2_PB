# Caminho do labirinto

CAMINHO = "/dados/labirinto.txt"


# percorrer o labirinto

def percorrer(labirinto, linha, coluna, visitados):

    # Verifica se chegou na saída

    if labirinto[linha][coluna] == "E":
        return True


    # Marca a posição como visitada

    visitados.add((linha, coluna))


    # Movimentos: baixo, direita, cima e esquerda

    movimentos = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]

    for movimento_linha, movimento_coluna in movimentos:

        nova_linha = linha + movimento_linha
        nova_coluna = coluna + movimento_coluna


        # Verifica se está dentro do labirinto

        if nova_linha < 0 or nova_linha >= len(labirinto):
            continue

        if nova_coluna < 0 or nova_coluna >= len(labirinto[0]):
            continue


        # Verifica se pode entrar na posição

        if labirinto[nova_linha][nova_coluna] == "#":
            continue
        
        
        # Verifica se a posição já foi visitada
        
        if (nova_linha, nova_coluna) in visitados:
            continue
        
        
        # Chamada recursiva
        
        if percorrer( labirinto, nova_linha, nova_coluna, visitados ):
            if labirinto[linha][coluna] == " ":
                labirinto[linha][coluna] = "."
            
            return True
    
    
    # Backtracking

    return False


# Leitura do labirinto

with open(CAMINHO, "r") as arquivo:

    labirinto = []

    for linha in arquivo:
        labirinto.append(list(linha.rstrip("\n")))


# Procura S e E

inicio = None
saida = None

for linha in range(len(labirinto)):

    for coluna in range(len(labirinto[linha])):
        
        if labirinto[linha][coluna] == "S":
            inicio = (linha, coluna)
        elif labirinto[linha][coluna] == "E":
            saida = (linha, coluna)


# Percorre o labirinto

visitados = set()

encontrou = percorrer( labirinto, inicio[0], inicio[1], visitados )


# Resultado

print("\n===== LABIRINTO =====")

for linha in labirinto:
    print("".join(linha))


if encontrou:
    print("\nCaminho encontrado!")
else:
    print("\nNenhum caminho encontrado!")

