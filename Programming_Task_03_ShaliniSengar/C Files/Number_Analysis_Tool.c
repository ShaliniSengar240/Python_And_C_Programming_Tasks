#include <stdio.h>

int main() {
    int N, i;
    int sum = 0, evenCount = 0, oddCount = 0;

    printf("Enter a number: ");
    scanf("%d", &N);

    for(i = 1; i <= N; i++) {
        sum += i;

        if(i % 2 == 0)
            evenCount++;
        else
            oddCount++;
    }

    printf("Sum = %d\n", sum);
    printf("Even Numbers = %d\n", evenCount);
    printf("Odd Numbers = %d\n", oddCount);

    return 0;
}