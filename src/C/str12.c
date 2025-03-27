#include <stdio.h>
#include <string.h>
int main() {
    char s[100];
    fgets(s, 100, stdin);
    s[strcspn(s, "\n")] = '\0';
    int n = strlen(s);
    for(int i = 0; i < n; i++)
    {
        if(s[i]!='\0')
        {
            for(int j=i+1; j < n; j++)
            {
                if(s[i] == s[j])
                {
                    s[j] = '\0';
                }
            }
            printf("%c", s[i]);
        }
    }    
}