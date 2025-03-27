//Print the given string without alphabets eg: Input:Lenova123@#45 Output:123@#45

#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';
    int n = strlen(str);
    int i;
    for(int i = 0; i < n; i++)
    {
        if(isalpha(str[i]))
        {
            continue;
        }
        printf("%c", str[i]);
    }
    

    return 0;
}