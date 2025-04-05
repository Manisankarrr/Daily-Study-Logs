#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    char s[100],r[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';

    fgets(r, 100, stdin);
    r[strcspn(r, "\n")] = '\0';

    char *found = strstr(s, r);
    if( found != NULL)
    {
        int index = found - s;
        printf("Substring found at index: %d %d\n", index);
    }
    else
    {
        printf("Substring not found\n");
    }

    
    
    
    
    
    
    
    
    
    
    return 0;
}