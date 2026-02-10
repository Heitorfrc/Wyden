#include <stdio.h>


int main() {
    int num1, num2, soma;

    // lendo dois numeros do usuario
    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero: ");
    scanf("%d", &num2);

    // fazendo a soma
    soma = num1 + num2;

    // mostrando o resultado
    printf("A soma de %d e %d eh: %d\n", num1, num2, soma);

    return 0;

}
