//Print consecutive repeated characters
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';

    int n = strlen(str);
    int i, j,count;
    char temp;
    for(int i=0;i<n;i++)
    {
        count = 1;
        while(i<n-1 && str[i] == str[i+1]){
            count++;
            i++;
        }
        if(count > 1){
            printf("%c => %d times\n", toupper(str[i]), count);
        }
    
    }

    

    return 0;
}