 #include <stdio.h>

int main() {
    int num1, num2, soma;
    float div1, div2, divisao;

    // comentario
    // lendo dois numeros do usuario
    printf("Digite o primeiro numero da soma: ");
    scanf("%d", &num1);

    printf("Digite o segundo numero da soma: ");
    scanf("%d", &num2);

    // fazendo a soma
    soma = num1 + num2;

    // mostrando o resultado
    printf("A soma de %d e %d eh: %d\n", num1, num2, soma);

    //adicionando divisao agora
    printf("Digite o primeiro numero para a divisao: ");
    scanf("%f", &div1);

    printf("Digite o denominador para a divisao: ");
    scanf("%f", &div2);

    // testando if
    if (div2 == 0) {
        printf ("O denominador nao pode ser zero.\n");
    } else {
    divisao = div1 / div2;
    printf("O resultado da divisao de %f e %f eh: %f\n", div1, div2, divisao);
    }


    return 0;
}
