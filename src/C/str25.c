#include <stdio.h>
#include <string.h>

int main() {
    char str[200], result[200] = "";
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';  // Remove trailing newline
    char maxi[100], mini[100];
    int max = 0, min = 10000;  // Assuming the maximum and minimum lengths are 10000
    char *token = strtok(str, " ");

    while (token != NULL) {
        int len = strlen(token);
        if(len > max)
        {
            max = len;
        strcpy(maxi, token);        }
        if(len < min)
        {
            min = len;
            strcpy(mini, token);        }

        token  = strtok(NULL, " ");
        }
    printf("Max word %s length: %d\n", maxi,max);
    printf("Min word %s length: %d\n", mini, min);

    
    return 0;
}



