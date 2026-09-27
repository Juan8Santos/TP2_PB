import time

CAMINHO = "/dados/numeros.txt"


# QuickSort

def partition(arr, inicio, fim, contador=None):

    pivo = arr[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        
        if contador is not None:
            contador[0] += 1
        
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    
    return i + 1


def quicksort(arr, inicio, fim, contador):

    if inicio < fim:
        contador[1] += 1
        posicao = partition( arr, inicio, fim, contador )
        
        quicksort( arr, inicio, posicao - 1, contador )
        quicksort( arr, posicao + 1, fim, contador )


# QuickSelect

def quickselect(arr, inicio, fim, k):
    
    if inicio == fim:
        return arr[inicio]
    
    posicao = partition( arr, inicio, fim )
    
    if k == posicao:
        return arr[posicao]
    
    if k < posicao:
        return quickselect( arr, inicio, posicao - 1, k )
    
    return quickselect( arr, posicao + 1, fim, k )


# Leitura dos números

with open(CAMINHO, "r") as arquivo:
    
    numeros = []
    
    for linha in arquivo:
        numeros.append(int(linha.strip()))


# QuickSort tempo de execução

arr_quicksort = numeros.copy()

contador = [0, 0]

inicio = time.perf_counter()

quicksort( arr_quicksort, 0, len(arr_quicksort) - 1, contador )

fim = time.perf_counter()

tempo_quicksort = fim - inicio

milésimo = arr_quicksort[999]


# QuickSelect tempo de execução

arr_quickselect = numeros.copy()

inicio = time.perf_counter()

resultado = quickselect( arr_quickselect, 0, len(arr_quickselect) - 1, 999 )

fim = time.perf_counter()

tempo_quickselect = fim - inicio


# Resultados

print("\n===== QUICKSORT =====")

print(f"1000º menor número: {milésimo}")
print(f"Comparações: {contador[0]}")
print(f"Chamadas recursivas: {contador[1]}")
print(f"Tempo: {tempo_quicksort:.6f} s")


print("\n===== QUICKSELECT =====")

print(f"1000º menor número: {resultado}")
print(f"Tempo: {tempo_quickselect:.6f} s")


print("\n===== COMPARAÇÃO =====")

print(f"QuickSort:   {tempo_quicksort:.6f} s")
print(f"QuickSelect: {tempo_quickselect:.6f} s")