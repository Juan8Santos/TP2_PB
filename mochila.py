import time


CAMINHO = "/dados/mochila.txt"


# Solução com recursividade

def mochila_recursiva(itens, indice, capacidade, contador):

    contador[0] += 1

    if indice == len(itens) or capacidade == 0:
        return 0

    _, peso, valor = itens[indice]

    if peso > capacidade:
        return mochila_recursiva( itens, indice + 1, capacidade, contador )

    sem_item = mochila_recursiva( itens, indice + 1, capacidade, contador )

    com_item = valor + mochila_recursiva( itens, indice + 1, capacidade - peso, contador )

    return max(sem_item, com_item)


# Solução de Programação dinâmica

def mochila_dinamica(itens, capacidade):

    estados_calculados = 0

    quantidade = len(itens)

    tabela = [ [0] * (capacidade + 1) for _ in range(quantidade + 1) ]

    for i in range(1, quantidade + 1):
        
        _, peso, valor = itens[i - 1]

        for capacidade_atual in range(capacidade + 1):
            
            estados_calculados += 1

            if peso > capacidade_atual:
                tabela[i][capacidade_atual] = tabela[i - 1][capacidade_atual]
            else:
                sem_item = tabela[i - 1][capacidade_atual]
                com_item = ( valor + tabela[i - 1][capacidade_atual - peso] )
                tabela[i][capacidade_atual] = max( sem_item, com_item )

    return tabela[quantidade][capacidade], estados_calculados


# Leitura dos itens

with open(CAMINHO, "r") as arquivo:

    primeira_linha = arquivo.readline().split()

    quantidade_itens = int(primeira_linha[0])

    capacidade = int(primeira_linha[1])

    itens = []

    for linha in arquivo:
        dados = linha.split()

        nome = dados[0]
        peso = int(dados[1])
        valor = int(dados[2])

        itens.append((nome, peso, valor))


# Recursiva tempo de execução

contador = [0]

inicio = time.perf_counter()

valor_recursivo = mochila_recursiva( itens, 0, capacidade, contador )

fim = time.perf_counter()

tempo_recursivo = fim - inicio


# Programação Dinâmica tempo de execução

inicio = time.perf_counter()

valor_dinamico, estados = mochila_dinamica( itens, capacidade )

fim = time.perf_counter()

tempo_dinamico = fim - inicio


# Resultados

print("\n===== RECURSIVA =====")

print(f"Valor máximo: {valor_recursivo}")
print(f"Chamadas recursivas: {contador[0]}")
print(f"Tempo: {tempo_recursivo:.6f} s")


print("\n===== PROGRAMAÇÃO DINÂMICA =====")

print(f"Valor máximo: {valor_dinamico}")
print(f"Estados calculados: {estados}")
print(f"Tempo: {tempo_dinamico:.6f} s")


print("\n===== COMPARAÇÃO DE TEMPO =====")

print(f"Recursiva: {tempo_recursivo:.6f} s")
print(f"Dinâmica:  {tempo_dinamico:.6f} s")