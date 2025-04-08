#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    char s[100],r[100];
    fgets(s, sizeof(s), stdin); // Read a line of input
    s[strcspn(s,"\n")] = '\0'; // Remove the newline character if present
    int i = 0, j = 0, n = strlen(s),sum=0,res = 0,k=0;
    
    char *token = strtok(s," ");
    while(token != NULL)
    {
        if(strstr(r,token) == NULL){ // Check if the word is the same as the token
            strcat(r,token); // Copy the word to r
            strcat(r," "); // Add a space after the word
        }
        token = strtok(NULL, " "); // Get the next token
    }
    r[strcspn(r,"\n")] = '\0'; // Remove the newline character if present
    printf("%s",r); // Print the result
}