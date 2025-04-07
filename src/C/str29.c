#include <string.h>
#include <stdio.h>    
#include <ctype.h>

int main()
{
    int k;
    scanf("%d", &k);
    getchar(); // Consume the newline character after the integer input
    char s[1000];
    fgets(s, 1000, stdin);
    s[strcspn(s, "\n")] = 0; // Remove newline character from input
    int n = strlen(s);
    char temp;
    for (int i=0;i<k;i++)
    {
        temp = s[n-1];
        for(int j=n-1;j>0;j--)
        {
            s[j] = s[j-1];

        }
        s[0] = temp;
    }
    printf("%s\n", s);
}