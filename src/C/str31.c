#include <string.h>
#include <stdio.h>  
#include <ctype.h>

int main()

{
    int n;
    scanf("%d", &n);
    getchar(); // Consume the newline character after the integer input
    char s[100][100];
    
    for(int i=0;i<n;i++)
    {
        printf("Enter a string: ");
        fgets(s[i], 100, stdin);
        s[i][strcspn(s[i], "\n")] = 0; // Remove newline character from input
    }
    for(int i=0;i<n;i+2)
    {
            int len = strlen(s[i]);
            for(int j = len-1; j >= 0; j--)
            {
                printf("%c", s[i][j]);
            }     
            printf("\n");
    }
}