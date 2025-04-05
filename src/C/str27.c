#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compareVersion(char* v1,  char* v2) {
    char* token = strtok(v1, ".");
    char* token2 = strtok(v2, ".");

    while(token != NULL || token2 || NULL)
    {
        int num  = token ? atoi(token) : 0;
        int num2 = token2 ? atoi(token2) : 0;

        if(num > num2)
        {
            return 1;
        }
        else if(num < num2)
        {
            return -1;
        }
        token = strtok(NULL, ".");
        token2 = strtok(NULL, ".");
    }
    return 0;
}

int main() {
    char version1[50], version2[50];
    printf("Enter version 1: ");
    scanf("%s", version1);
    printf("Enter version 2: ");
    scanf("%s", version2);

    // Make a copy because strtok modifies original string
    char v1[50], v2[50];
    strcpy(v1, version1);
    strcpy(v2, version2);

    int result = compareVersion(v1, v2);
    if (result == 1)
        printf("Version 1 is higher\n");
    else if (result == -1)
        printf("Version 2 is higher\n");
    else
        printf("Both versions are equal\n");

    return 0;
}
