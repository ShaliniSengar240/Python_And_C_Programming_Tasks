#include <stdio.h>
#include <string.h>

int main() {
    char password[] = "admin123";   // Predefined password
    char input[50];
    int attempts;

    for (attempts = 1; attempts <= 3; attempts++) {
        printf("Enter password: ");
        scanf("%s", input);

        if (strcmp(input, password) == 0) {
            printf("Access Granted\n");
            return 0;
        } else {
            printf("Incorrect Password!\n");
        }
    }

    printf("Account Locked\n");

    return 0;
}