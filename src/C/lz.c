#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    char s[100],r[100];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0'; // Remove the newline character if present

    printf("Enter a substring: ");
    fgets(r, sizeof(r), stdin); // Read a line of input
    r[strcspn(r,"\n")] = '\0'; 
    
    char *token1 = strtok(s,".");
    token1 = strtok(NULL, " "); // Get the first token from s
    char *token2 = strtok(r,".");
    token2 = strtok(NULL, " "); // Get the first token from r
    int res = strcmp(token1,token2); // Compare the two tokens
    if(res == 0) // If the tokens are equal
    {
        printf("The two strings are equal\n");
    }
    else if(res > 0) // If the tokens are not equal
    {
        printf("greater ");
    }
    else if(res < 0) // If the tokens are not equal
    {
        printf("lesser\n");
    }
    else // If the tokens are not equal
    {
        printf("The two strings are not equal\n");
    }




    return 0;
}