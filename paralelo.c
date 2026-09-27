#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <omp.h>

#define CAMINHO_ARQUIVOS "/dados/arquivos"
#define MAX_ARQUIVOS 12

typedef struct {
    char nome[256];
    long linhas;
    long palavras;
} Resultado;

int contar_palavras(char *linha) {
    int palavras = 0;
    int dentro_palavra = 0;

    for (int i = 0; linha[i] != '\0'; i++) {
        if (linha[i] != ' ' && linha[i] != '\n' && linha[i] != '\t' && linha[i] != '\r') {
            if (!dentro_palavra) {
                palavras++;
                dentro_palavra = 1;
            }
        } else {
            dentro_palavra = 0;
        }
    }

    return palavras;
}

void processar_arquivo(const char *nome, Resultado *resultado) {
    char caminho[512];

    snprintf(caminho, sizeof(caminho), "%s/%s", CAMINHO_ARQUIVOS, nome);

    FILE *arquivo = fopen(caminho, "r");

    char linha[4096];

    resultado->linhas = 0;
    resultado->palavras = 0;

    while (fgets(linha, sizeof(linha), arquivo) != NULL) {
        resultado->linhas++;
        resultado->palavras += contar_palavras(linha);
    }

    fclose(arquivo);
}

int main() {
    DIR *diretorio;
    struct dirent *entrada;

    Resultado resultados[MAX_ARQUIVOS];

    int quantidade = 0;

    diretorio = opendir(CAMINHO_ARQUIVOS);

    while ((entrada = readdir(diretorio)) != NULL) {
        if (strstr(entrada->d_name, ".txt") != NULL) {
            strcpy(resultados[quantidade].nome, entrada->d_name);
            quantidade++;
        }
    }

    closedir(diretorio);

    double inicio = omp_get_wtime();

    #pragma omp parallel for
    for (int i = 0; i < quantidade; i++) {
        processar_arquivo(resultados[i].nome, &resultados[i]);
    }

    double fim = omp_get_wtime();

    for (int i = 0; i < quantidade; i++) {
        printf("\n%s\n", resultados[i].nome);
        printf("Qtd linhas: %ld\n", resultados[i].linhas);
        printf("Qtd palavras: %ld\n", resultados[i].palavras);
    }

    printf("\nTempo de execucao: %.2f s\n", fim - inicio);
    printf("Threads utilizadas: %d\n", omp_get_max_threads());

    return 0;
}