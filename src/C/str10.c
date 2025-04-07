#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    printf("Enter a string: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';  // Remove trailing newline

    char *word[50];

    char *token = strtok(s, " ");
    int count =0;
    while(token != NULL){
        word[count++] = token;
        token = strtok(NULL, " ");
    }
    word[count] = '\0';
    
    for(int i=count-1;i>=0;i--)
    {
        printf("%s",word[i]);
        if(i!=0)
        {
            printf(" ");
        }
    }


    return 0;
}
