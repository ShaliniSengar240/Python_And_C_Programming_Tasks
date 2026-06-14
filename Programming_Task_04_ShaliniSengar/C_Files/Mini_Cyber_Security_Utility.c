#include <stdio.h>

int main() {
    char website[50], username[50], password[50];

    printf("Enter Website Name: ");
    scanf("%s", website);

    printf("Enter Username: ");
    scanf("%s", username);

    printf("Enter Password: ");
    scanf("%s", password);

    // Save data to file
    FILE *fp = fopen("vault.txt", "a");

    fprintf(fp, "Website: %s\n", website);
    fprintf(fp, "Username: %s\n", username);
    fprintf(fp, "Password: %s\n\n", password);

    fclose(fp);

    printf("\nRecord Saved Successfully!\n");

    // Display all saved records
    fp = fopen("vault.txt", "r");

    char ch;
    printf("\n--- Saved Records ---\n\n");

    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);

    return 0;
}