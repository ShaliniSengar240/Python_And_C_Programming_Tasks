#include <stdio.h>

// Functions
float addition(float a, float b)
{
    return a + b;
}

float subtraction(float a, float b)
{
    return a - b;
}

float multiplication(float a, float b)
{
    return a * b;
}

float division(float a, float b)
{
    return a / b;
}

int main()
{
    int choice;
    float num1, num2;

    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");

    printf("Enter Choice: ");
    scanf("%d", &choice);

    printf("Enter First Number: ");
    scanf("%f", &num1);

    printf("Enter Second Number: ");
    scanf("%f", &num2);

    switch(choice)
    {
        case 1:
            printf("Result: %.2f\n", addition(num1, num2));
            break;

        case 2:
            printf("Result: %.2f\n", subtraction(num1, num2));
            break;

        case 3:
            printf("Result: %.2f\n", multiplication(num1, num2));
            break;

        case 4:
            if(num2 == 0)
                printf("Division by zero is not allowed\n");
            else
                printf("Result: %.2f\n", division(num1, num2));
            break;

        default:
            printf("Invalid Choice\n");
    }

    return 0;
}