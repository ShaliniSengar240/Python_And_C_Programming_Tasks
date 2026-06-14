#include <stdio.h>

// Function to display student information
void displayStudent(char name[], int rollNo, char branch[], int semester)
{
    printf("\nStudent Information\n");
    printf("-------------------\n");
    printf("Name      : %s\n", name);
    printf("Roll No   : %d\n", rollNo);
    printf("Branch    : %s\n", branch);
    printf("Semester  : %d\n", semester);
}

int main()
{
    char name[50], branch[30];
    int rollNo, semester;

    printf("Enter Student Name: ");
    scanf(" %[^\n]", name);

    printf("Enter Roll Number: ");
    scanf("%d", &rollNo);

    printf("Enter Branch: ");
    scanf("%s", branch);

    printf("Enter Semester: ");
    scanf("%d", &semester);

    // Function call
    displayStudent(name, rollNo, branch, semester);

    return 0;
}