// this s my friend is => this my friend


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char s[100];
    printf("Enter a string: ");
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';

    int i, j;
    char temp[100];
    fgets(temp, 100, stdin);
    temp[strcspn(temp, "\n")] = '\0';
    int n = strlen(s),k=0;
    char reverse[100],res[100];

    char *token  = strtok(s, " ");
    while(token != NULL)
    {
        if (strcmp(token, temp)!=0)
        {
            strcat(res, token);
            strcat(res, " ");
        }

        token = strtok(NULL, " ");        
    }
    printf("%s\n", res);

    return 0;
    

}