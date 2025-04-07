//reverse the word in string output: i am good input: good am i

#include<stdio.h>
#include<string.h>

int main()
{
    char s[100],r[100],text;
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';
    int n = strlen(s)-1,start=0,end=n,k=0;
    while(n>=0)
    {
        if(s[n]==' ')
        {
            start = n+1;
            for(int i=start;i<=end;i++)
            {
                r[k++] = s[i];
            }
            r[k++] =' ';
            end = n-1;
        }
        n--;
    }

    for(int i=0;i<=end;i++)
    {
        
        r[k++] = s[i];
    }
    r[k] = '\0';
    printf("%s",r);

}