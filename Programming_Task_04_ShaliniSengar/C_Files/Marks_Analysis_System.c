#include <stdio.h>

int main() {
    int marks[5];
    int total = 0;
    float percentage;
    char grade;

    printf("Enter marks for 5 subjects:\n");

    for (int i = 0; i < 5; i++) {
        printf("Subject %d: ", i + 1);
        scanf("%d", &marks[i]);
        total += marks[i];
    }

    percentage = total / 5.0;

    if (percentage >= 90)
        grade = 'A';
    else if (percentage >= 80)
        grade = 'B';
    else if (percentage >= 70)
        grade = 'C';
    else if (percentage >= 60)
        grade = 'D';
    else
        grade = 'F';

    printf("\n----- Result -----\n");
    printf("Total Marks = %d\n", total);
    printf("Percentage = %.2f%%\n", percentage);
    printf("Grade = %c\n", grade);

    return 0;
}