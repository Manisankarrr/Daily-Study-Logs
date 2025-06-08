//FREQUENCY OF THE FIRST NON-REPEATING CHARACTER

#include <stdio.h>
#include <string.h>
int main()
{
    char s[100];
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int i, j;
    int n = strlen(s);
    int count;
    for (i=0;i<n;i++)
    {
        count = 1;
        if(s[i] != '\0' ){
        for(j=i+1;j<n;j++)
        {
            if(s[i] == s[j])
            {
                count++;
                s[j] = '\0';
            }
        }
        if(count == 1)
        {
            printf("%c occurs %d times\n", s[i], count);
            return 0;
            
        }        
    }    
}
printf("Not found");
}