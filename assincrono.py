import asyncio
import os
import time

CAMINHO_ARQUIVOS = "/dados/arquivos"

async def processar_arquivo(nome_arquivo):
    caminho = os.path.join(CAMINHO_ARQUIVOS, nome_arquivo)
    
    def ler_arquivo():
        with open(caminho, "r") as arquivo:
            linhas = 0
            palavras = 0
            
            for linha in arquivo:
                linhas += 1
                palavras += len(linha.split())
            
            return linhas, palavras
    
    linhas, palavras = await asyncio.to_thread(ler_arquivo)
    
    return nome_arquivo, linhas, palavras

async def main():
    arquivos = sorted(os.listdir(CAMINHO_ARQUIVOS))
    
    inicio = time.perf_counter()
    
    tarefas = []
    
    for arquivo in arquivos:
        tarefas.append(processar_arquivo(arquivo))
    
    resultados = await asyncio.gather(*tarefas)
    
    fim = time.perf_counter()
    
    for nome, linhas, palavras in resultados:
        print(f"\n{nome}")
        print(f"Qtd linhas: {linhas}")
        print(f"Qtd palavras: {palavras}")
    
    print(f"\nTempo de execução: {fim - inicio:.2f} s")

if __name__ == "__main__":
    asyncio.run(main())