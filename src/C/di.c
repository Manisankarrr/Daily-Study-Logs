#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main()
{
    char s[100];
    fgets(s, sizeof(s), stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0';
    int i = 0, j = 0, n = strlen(s),sum=0,res = 0;

    for(int i=0;i<n;i++)
    {
        if(isdigit(s[i]))
        {
            sum += s[i] - '0'; 
        }
    }
    printf("%d\n",sum); // Print the sum of digits
    int rem =0;
    while(sum>0)
    {
        rem  =sum % 10;
        res = res * 10 + rem;
        sum = sum/10;
    }

}