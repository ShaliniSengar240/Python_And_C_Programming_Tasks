#include <stdio.h>

int main() {
    char name[50], branch[50];
    int rollNo, marks;

    // Input student details
    printf("Enter Name: ");
    scanf(" %[^\n]", name);

    printf("Enter Roll Number: ");
    scanf("%d", &rollNo);

    printf("Enter Branch: ");
    scanf("%s", branch);

    printf("Enter Marks: ");
    scanf("%d", &marks);

    // Write data to file
    FILE *fp = fopen("student_data.txt", "w");

    fprintf(fp, "Name: %s\n", name);
    fprintf(fp, "Roll No: %d\n", rollNo);
    fprintf(fp, "Branch: %s\n", branch);
    fprintf(fp, "Marks: %d\n", marks);

    fclose(fp);

    printf("\nStudent Record Saved Successfully\n");

    // Read and display file contents
    fp = fopen("student_data.txt", "r");

    char ch;
    printf("\nReading File...\n\n");

    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);

    return 0;
}