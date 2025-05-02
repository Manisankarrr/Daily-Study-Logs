//Reverse a string and print characters in odd index
#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main() {
    char str[100], reversed[100];
    int length, i, j = 0;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';

    length = strlen(str);
    for (i = length - 1; i >= 0; i--) {
        reversed[j++] = str[i];
    }
    reversed[j] = '\0'; 
    printf("Reversed string: %s\n", reversed);
    
    printf("Characters at odd indices: ");
    for (i = 1; i < length; i += 2) {
        printf("%c ", reversed[i]);
    }
    printf("\n");

    return 0;
}