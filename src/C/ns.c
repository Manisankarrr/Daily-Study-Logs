#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

int main()
{
    char s[100];
    fgets(s, sizeof(s), stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0'; // Remove the newline character if present
    int i = 0, j = 0, n = strlen(s),sum=0,res = 0,k=0;
    char ans[100] = {0};
    for(int i=0;i<n;i++)
    {
        k = 0;
        while(isdigit(s[i]))
        {
            ans[k++] = s[i];
            i++;
        }
        ans[k] = '\0'; // Null-terminate the string
        if(k > 0)
        {
            int num = atoi(ans);
            sum += num; // Print the number
        }
    }
    printf("%d\n",sum); // Print the sum of the numbers
}