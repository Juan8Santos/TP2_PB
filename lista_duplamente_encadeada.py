import time


# Nó da lista duplamente encadeada

class No:

    def __init__(self, dado):
        self.ant = None
        self.dado = dado
        self.prox = None


# Lista duplamente encadeada

class ListaDupla:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    
    # Inserir no início
    
    def inserir_inicio(self, dado):
        
        novo = No(dado)
        
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.prox = self.inicio
            self.inicio.ant = novo
            self.inicio = novo
        
        self.tamanho += 1
    
    
    # Inserir no final
    
    def inserir_final(self, dado):
        
        novo = No(dado)
        
        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.ant = self.fim
            self.fim.prox = novo
            self.fim = novo
        
        self.tamanho += 1
    
    
    # Buscar
    
    def buscar(self, valor):
        
        atual = self.inicio
        
        while atual is not None:
            if atual.dado == valor:
                return atual
            
            atual = atual.prox
        
        return None


    # Remover

    def remover(self, valor):
        
        atual = self.buscar(valor)
        
        if atual is None:
            return False
        
        if atual.ant is None:
            self.inicio = atual.prox
        else:
            atual.ant.prox = atual.prox
        
        if atual.prox is None:
            self.fim = atual.ant
        else:
            atual.prox.ant = atual.ant
        
        self.tamanho -= 1
        
        return True
    
    
    # Listar do início para o fim
    
    def listar_inicio(self):
        
        atual = self.inicio
        
        while atual is not None:
            print(f"{atual.dado} ->", end=" ")
            atual = atual.prox
        
        print("Fim")
    
    
    # Listar do fim para o início
    
    def listar_fim(self):
        
        atual = self.fim
        
        while atual is not None:
            print(f"{atual.dado} ->", end=" ")
            atual = atual.ant
        
        print("Fim")
    
    # Medir tempo da busca
    
    def buscar_tempo(self, valor):
        
        inicio = time.perf_counter()
        
        resultado = self.buscar(valor)
        
        fim = time.perf_counter()
        
        tempo = fim - inicio
        
        return resultado, tempo


# Teste da lista

lista = ListaDupla()

lista.inserir_final(10)
lista.inserir_final(20)
lista.inserir_final(30)
lista.inserir_final(40)
lista.inserir_final(50)

lista.remover(30)


print("\n===== LISTA DO INÍCIO PARA O FIM =====")

lista.listar_inicio()


print("\n===== LISTA DO FIM PARA O INÍCIO =====")

lista.listar_fim()


# Teste com 100.000 elementos

lista_teste = ListaDupla()

inicio = time.perf_counter()

for i in range(100000):
    lista_teste.inserir_final(i)

fim = time.perf_counter()


print("\n===== TESTE COM 100.000 ELEMENTOS =====")

print(f"Quantidade de elementos: {lista_teste.tamanho}")
print(f"Tempo de inserção: {fim - inicio:.6f} s")


# Busca próximo ao início

resultado_inicio, tempo_inicio = lista_teste.buscar_tempo(100)

print("\nBusca próximo ao início")
print(f"Elemento buscado: 100")
print(f"Encontrado: {resultado_inicio.dado}")
print(f"Tempo: {tempo_inicio:.6f} s")


# Busca próximo ao meio

resultado_meio, tempo_meio = lista_teste.buscar_tempo(50000)

print("\nBusca próximo ao meio")
print(f"Elemento buscado: 50000")
print(f"Encontrado: {resultado_meio.dado}")
print(f"Tempo: {tempo_meio:.6f} s")


# Busca próximo ao final

resultado_final, tempo_final = lista_teste.buscar_tempo(99900)

print("\nBusca próximo ao final")
print(f"Elemento buscado: 99900")
print(f"Encontrado: {resultado_final.dado}")
print(f"Tempo: {tempo_final:.6f} s")