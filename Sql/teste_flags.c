#include <stdio.h>
#include <fcntl.h>

void imprimir_flags_open(FILE *arquivo, unsigned long flags);

int main() {
    FILE *saida = stdout;

    unsigned long flags = O_CREAT | O_WRONLY | O_TRUNC | O_CLOEXEC;
    fprintf(saida, "Flags: ");
    imprimir_flags_open(saida, flags);
    fprintf(saida, "\n");

    return 0;
}