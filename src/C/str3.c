//FREQUENCY OFTHEFIRSTREPEATING CHARACTER

#include <stdio.h>
#include <string.h>
int main()
{
    char s[100];
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int i, j;
    int n = strlen(s);
    for (i=0;i<n;i++)
    {
        int count = 1;
        for(j=i+1;j<n;j++)
        {
            if(s[i] == s[j])
            {
                count++;
            }

        }
        if(count > 1)
        {
            printf("%c occurs %d times\n", s[i], count);
            break;
        }
        
    }
}