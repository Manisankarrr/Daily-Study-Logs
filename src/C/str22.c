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
    int n = strlen(s),k=0;
    char reverse[100];

    // char *token = strtok(s, " ");
    // while(token!=NULL)
    // {
    //     int len = strlen(token);
    //     for(int i=len-1;i>=0;i--)
    //     {
            
    //         reverse[k++] = token[i];
            
    //     }
    //     reverse[k++] = ' ';
    //     token = strtok(NULL," ");
    // }
    // reverse[k-1] = '\0';
    // printf("Reversed string: %s\n", reverse);
    char *token  = strtok(s, " ");
    while(token != NULL)
    {

        int len = strlen(token);
        for(int i=len-1;i>=0;i--)
        {
            reverse[k++] = token[i];
        }
        reverse[k++] = ' ';
        token = strtok(NULL, " ");        
    }
    reverse[k-1] = '\0';
    printf("Reversed string: %s\n", reverse);

    return 0;
    

}