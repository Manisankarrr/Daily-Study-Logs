#include<string.h>
#include<ctype.h>
#include<stdio.h>

int main()
{
    char s[100],r[100];
    fgets(s,100,stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0'; // Remove the newline character if present
    int i = 0, j = 0, n = strlen(s),sum=0,res = 0,k=0;

    char *token = strtok(s," ");
    while(token != NULL)
    {
        int len  = strlen(token);
        for(int i=len-1; i>=0; i--)
        {
            r[k++] = token[i];
        }
        r[k++] = ' '; // Add a space after each word
        token = strtok(NULL, " ");
    }
    r[k-1] = '\0'; // Null-terminate the reversed string
    printf("%s\n",r); // Print the reversed string
}