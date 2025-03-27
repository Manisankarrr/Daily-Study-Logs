//Replace space with %20

#include <stdio.h>
#include <string.h>

int main()
{
    char s[100];
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int length = strlen(s);
    int i, j;
    for (i = 0; i < length; i++)
    {
        if (s[i] ==' ')
        {
            printf("%%20");
        }
        else
        {
            printf("%c", s[i]);
        }
    }
}
