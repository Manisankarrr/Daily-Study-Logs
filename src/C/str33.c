#include <stdio.h>
#include <string.h>

int main() {
    char str[200], result[200] = "";
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';  // Remove newline

    char* token = strtok(str, " ");
    while(token != NULL) {
        // Check if the word already exists in result
        char temp[200];
        strcpy(temp, result);
        int duplicate = 0;

        char* word = strtok(temp, " ");
        while(word != NULL) {
            if(strcmp(word, token) == 0) {
                duplicate = 1;
                break;
            }
            word = strtok(NULL, " ");
        }

        // If not duplicate, append to result
        if(!duplicate) {
            strcat(result, token);
            strcat(result, " ");
        }

        token = strtok(NULL, " ");
    }

    // Remove trailing space
    int len = strlen(result);
    if(len > 0 && result[len - 1] == ' ')
        result[len - 1] = '\0';

    printf("String after removing duplicates: %s\n", result);
    return 0;
}
