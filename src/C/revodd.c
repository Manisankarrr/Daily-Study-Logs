#include <string.h>
#include <stdio.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';
    int n = strlen(str);
    for(int i = n-1; i >= 0; i-=2) {
        printf("%c", str[i]);
    }

}