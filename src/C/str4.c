//highest frequency

#include <stdio.h>
#include <string.h>
int main()
{
    char s[100];
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int i, j,max=0;
    char c;
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
            if( max < count)
            {
                max  = count;
                c = s[i];
            }

        }
        
    }
    if(max > 1)
        {
            printf("%c occurs %d times\n", c, max);
            
        }
}