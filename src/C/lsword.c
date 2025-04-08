#include<string.h>
#include<ctype.h>
#include<stdio.h>

int main()
{
    char s[100],r[100];
    fgets(s,100,stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0'; // Remove the newline character if present
    int i = 0, j = 0, n = strlen(s),sum=0,res = 0,k=0;
    char maxi[100]="",mini[100]="";
    int max = 0, min = 1000000;

    char * token = strtok(s," ");
    while(token != NULL)
    {
        int len = strlen(token);
        if(max < len)
        {
            max =  len;
            strcpy(maxi,token);
         } // Copy the longest word to maxi}
        if(min > len)
        {
            min = len;
            strcpy(mini,token); // Copy the shortest word to mini
        }
        token = strtok(NULL, " ");
    }
    printf("%s\n",maxi); // Print the longest word
    printf("%s\n",mini); // Print the shortest word
}